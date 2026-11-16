"""Unit tests for core zero-dependency scripts in scripts/."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import audit_repo
import build_catalog
import graph_enrich
import mcp_health
import rag_index
import rag_search
import skills_mcp
import sync_all


class TestAuditRepo(unittest.TestCase):
    def test_mask_secret_and_placeholder(self) -> None:
        sample = "sk_" + "1234567890abcdef"
        masked = audit_repo.mask_secret(sample)
        self.assertTrue(masked.startswith("sk_1"))
        self.assertIn("...", masked)
        self.assertTrue(audit_repo.is_placeholder("sk_<SUPOCLIP_API_KEY>", "Authorization: Bearer sk_<SUPOCLIP_API_KEY>"))
        real_val = "sk_" + "real_secret_value_12345"
        self.assertFalse(audit_repo.is_placeholder(real_val, f"token = {real_val}"))

    def test_check_secrets_detects_and_skips_placeholders(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            safe_file = root / "safe.md"
            safe_file.write_text("Authorization: Bearer <TOKEN_HERE>\n", encoding="utf-8")
            bad_file = root / "leak.txt"
            bad_token = "sk_" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4"
            bad_file.write_text(f"token={bad_token}\n", encoding="utf-8")

            findings = audit_repo.check_secrets(root, [safe_file, bad_file])
            self.assertEqual(len(findings), 1)
            self.assertIn("leak.txt", findings[0])


class TestBuildCatalog(unittest.TestCase):
    def test_parse_frontmatter_and_freshness(self) -> None:
        fm = build_catalog.parse_frontmatter(
            '---\nname: demo-skill\ndescription: |\n  Line one\n  Line two\n---\n# Body\n'
        )
        self.assertEqual(fm["name"], "demo-skill")
        self.assertEqual(fm["description"], "Line one Line two")

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "development" / "demo-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: demo-skill\ndescription: Demo description\n---\n# Demo\n",
                encoding="utf-8",
            )
            out = root / "docs" / "catalog" / "catalog.json"
            catalog = build_catalog.build_catalog(root=root, output=out)
            self.assertEqual(catalog["counts"]["skills"], 1)
            self.assertTrue(build_catalog.is_catalog_fresh(root=root, output=out))

            (skill_dir / "SKILL.md").write_text(
                "---\nname: demo-skill\ndescription: Changed description\n---\n# Demo\n",
                encoding="utf-8",
            )
            self.assertFalse(build_catalog.is_catalog_fresh(root=root, output=out))


class TestRagEngine(unittest.TestCase):
    def test_index_and_search_sqlite_and_rrf(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "ai-agents" / "demo-rag"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: demo-rag\ndescription: Hybrid RAG test\n---\n"
                "# Demo RAG\n\n## Vector Search\nUse pgvector with HNSW and BM25.\n",
                encoding="utf-8",
            )
            db_path = root / ".cache" / "rag_index.db"
            _, stats1 = rag_index.index_sqlite(root, db_path)
            self.assertEqual(stats1["indexed"], 1)

            _, stats2 = rag_index.index_sqlite(root, db_path)
            self.assertEqual(stats2["skipped"], 1)

            hits = rag_search.search_index(db_path, "pgvector HNSW", top_k=3, doc_type="skill")
            self.assertEqual(len(hits), 1)
            self.assertEqual(hits[0]["doc_type"], "skill")

            fused = rag_search.reciprocal_rank_fusion(
                [{"path": "a.md", "section": "S1", "doc_type": "skill", "score": 10, "snippet": "a", "content": "a"}],
                [
                    {"path": "b.md", "section": "S2", "doc_type": "skill", "score": 0.9, "snippet": "b", "content": "b"},
                    {"path": "a.md", "section": "S1", "doc_type": "skill", "score": 0.8, "snippet": "a", "content": "a"},
                ],
                top_k=2,
            )
            self.assertEqual(fused[0]["path"], "a.md")


class TestBootstrapAndSyncAndMcp(unittest.TestCase):
    def test_bootstrap_dry_run_and_create(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample-app"
            dry = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "bootstrap_project.py"), "--name", "sample-app", "--type", "web", "--out", str(target), "--dry-run"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(dry.returncode, 0)
            self.assertFalse(target.exists())

            real = subprocess.run(
                [sys.executable, str(SCRIPTS_DIR / "bootstrap_project.py"), "--name", "sample-app", "--type", "web", "--out", str(target)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(real.returncode, 0)
            self.assertTrue((target / "docs" / "brain" / "INDEX.md").is_file())

    def test_mcp_masking(self) -> None:
        secret_tok = "sk_" + "secret_1234567890"
        masked = mcp_health.mask_secrets(f"Authorization: Bearer {secret_tok}", [secret_tok])
        self.assertNotIn(secret_tok, masked)
        masked_url = mcp_health.mask_url("https://example.com/mcp?apiKey=secret123")
        self.assertNotIn("secret123", masked_url)
        self.assertIn("apiKey=", masked_url)

    def test_sync_all_hook_and_mirror(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / ".git" / "hooks").mkdir(parents=True)
            hook = sync_all.install_pre_commit_hook(root)
            self.assertTrue(hook.is_file())
            self.assertIn("audit_repo.py", hook.read_text(encoding="utf-8"))

            agents_src = root / "custom-agents"
            (agents_src / "global-master-agent").mkdir(parents=True)
            (agents_src / "demo-agent.md").write_text("# Demo Agent\n", encoding="utf-8")
            (agents_src / "global-master-agent" / "SKILL.md").write_text("# GMA Skill\n", encoding="utf-8")

            copied, mismatches = sync_all.mirror_protocol7(
                repo_root=root,
                gemini_dir=root / "gemini_cfg",
                agents_dir=root / "agents_cfg",
            )
            self.assertEqual(copied, 3)
            self.assertEqual(mismatches, 0)

    def test_skills_mcp_and_graph_enrich(self) -> None:
        init_resp = skills_mcp.handle_request({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        self.assertEqual(init_resp["result"]["serverInfo"]["name"], "skiilstoias-mcp")
        list_resp = skills_mcp.handle_request({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        tool_names = {t["name"] for t in list_resp["result"]["tools"]}
        self.assertIn("skills_rag_search", tool_names)
        self.assertIn("skills_catalog_lookup", tool_names)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "custom-agents").mkdir(parents=True)
            (root / "mcps" / "supoclip").mkdir(parents=True)
            (root / "docs" / "brain").mkdir(parents=True)
            (root / "ai-agents" / "graphify").mkdir(parents=True)
            (root / "mcps" / "supoclip" / "README.md").write_text("# SupoClip\n", encoding="utf-8")
            (root / "ai-agents" / "graphify" / "SKILL.md").write_text("---\nname: graphify\ndescription: g\n---\n", encoding="utf-8")
            (root / "custom-agents" / "global-master-agent.md").write_text("Uses `supoclip` and `graphify`.\n", encoding="utf-8")
            (root / "docs" / "brain" / "INDEX.md").write_text("[[DECISIONS]]\n", encoding="utf-8")
            (root / "docs" / "brain" / "DECISIONS.md").write_text("# Decisions\n", encoding="utf-8")

            sem = graph_enrich.build_ecosystem_semantic(root)
            self.assertGreaterEqual(len(sem["nodes"]), 4)
            self.assertGreaterEqual(len(sem["edges"]), 3)


if __name__ == "__main__":
    unittest.main()
