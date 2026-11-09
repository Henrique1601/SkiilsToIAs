import json
import urllib.request
import time
import os

TOKEN_FILE = r"C:\Users\henri\.gemini\antigravity\mcp_oauth_tokens.json"
WORKSPACE_ID = "c4ac1a9142aafe8932d2"
MCP_URL = "https://mcp.lovable.dev"

with open(TOKEN_FILE, "r", encoding="utf-8") as f:
    tok = json.load(f)["https://mcp.lovable.dev"]["token"]["access_token"]

def extract_frontmatter_name(text):
    for line in text.splitlines():
        if line.startswith("name:"):
            val = line.split("name:", 1)[1].strip()
            return val.strip("\"'")
    return None

def upload(skill_name, markdown):
    req_data = json.dumps({
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": "create_workspace_skill",
            "arguments": {
                "workspace_id": WORKSPACE_ID,
                "skill_name": skill_name,
                "markdown": markdown
            }
        }
    }).encode("utf-8")
    req = urllib.request.Request(
        MCP_URL,
        data=req_data,
        headers={
            "Authorization": f"Bearer {tok}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    )
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8")

remaining_files = [
    r"c:\Users\henri\.agents\skills\ai-agents\command-development\SKILL.md",
    r"c:\Users\henri\.agents\skills\ai-agents\hook-development\SKILL.md",
    r"c:\Users\henri\.agents\skills\design\ui-toolkit-web\SKILL.md",
    r"c:\Users\henri\.agents\skills\documents-productivity\scientific-db-uspto-database\SKILL.md",
    r"c:\Users\henri\.agents\skills\documents-productivity\scientific-pkg-gget\SKILL.md",
    r"c:\Users\henri\.agents\skills\documents-productivity\scientific-thinking-literature-review\SKILL.md",
    r"c:\Users\henri\.agents\skills\documents-productivity\scientific-thinking-scholar-evaluation\SKILL.md",
    r"c:\Users\henri\.agents\skills\marketing\linkedin-skills\SKILL.md"
]

for path in remaining_files:
    with open(path, "r", encoding="utf-8") as f:
        md = f.read()
    name = extract_frontmatter_name(md)
    t0 = time.time()
    res = upload(name, md)
    ok = "commit_sha" in res or "skill" in res
    dur = time.time() - t0
    print(f"{name}: OK={ok} ({dur:.2f}s)")
