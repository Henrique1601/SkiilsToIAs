import os
import sys
import json
import time
import glob
import urllib.request
import argparse

TOKEN_FILE = r"C:\Users\henri\.gemini\antigravity\mcp_oauth_tokens.json"
WORKSPACE_ID = "c4ac1a9142aafe8932d2"
MCP_URL = "https://mcp.lovable.dev"
REPO_DIR = r"c:\Users\henri\.agents\skills"

def get_token():
    with open(TOKEN_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["https://mcp.lovable.dev"]["token"]["access_token"]

def call_mcp(token, tool_name, arguments):
    req_data = json.dumps({
        "jsonrpc": "2.0",
        "id": int(time.time() * 1000),
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        MCP_URL,
        data=req_data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    )
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode("utf-8")
        for line in body.splitlines():
            if line.startswith("data:"):
                payload = json.loads(line[5:].strip())
                if "result" in payload and "content" in payload["result"]:
                    return json.loads(payload["result"]["content"][0]["text"])
                return payload
    return {}

def get_existing_skills(token):
    res = call_mcp(token, "list_workspace_skills", {"workspace_id": WORKSPACE_ID})
    skills = set()
    if isinstance(res, dict) and "skills" in res:
        for s in res["skills"]:
            skills.add(s["name"])
    return skills

def upload_skill(token, skill_name, skill_path):
    with open(skill_path, "r", encoding="utf-8") as f:
        md = f.read()

    for attempt in range(3):
        try:
            res = call_mcp(token, "create_workspace_skill", {
                "workspace_id": WORKSPACE_ID,
                "skill_name": skill_name,
                "markdown": md
            })
            if "skill" in res or "commit_sha" in res:
                return True
            print(f" (tentativa {attempt+1} resposta inesperada: {str(res)[:60]})", end="")
        except Exception as e:
            print(f" (tentativa {attempt+1} erro: {e})", end="")
        time.sleep(1)
    return False

def main():
    parser = argparse.ArgumentParser(description="Upload skills to Lovable workspace via MCP")
    parser.add_argument("--categories", nargs="+", help="Specific categories to upload (e.g. design development)")
    parser.add_argument("--limit", type=int, default=0, help="Max number of skills to upload (0 for all)")
    args = parser.parse_args()

    print("[*] Conectando ao Lovable MCP...")
    token = get_token()
    existing = get_existing_skills(token)
    print(f"[*] Skills já existentes no Lovable ({len(existing)}):")

    all_skill_files = []
    if args.categories:
        for cat in args.categories:
            pattern = os.path.join(REPO_DIR, cat, "*", "SKILL.md")
            all_skill_files.extend(glob.glob(pattern))
    else:
        pattern = os.path.join(REPO_DIR, "*", "*", "SKILL.md")
        all_skill_files.extend(glob.glob(pattern))

    to_upload = []
    for f in all_skill_files:
        skill_name = os.path.basename(os.path.dirname(f))
        if skill_name not in existing:
            to_upload.append((skill_name, f))

    print(f"[*] Total de skills encontradas: {len(all_skill_files)}")
    print(f"[*] Skills a serem enviadas: {len(to_upload)}")

    if args.limit > 0:
        to_upload = to_upload[:args.limit]
        print(f"[*] Limitado a: {len(to_upload)} skills")

    success = 0
    failed = 0

    for i, (name, path) in enumerate(to_upload, 1):
        try:
            t0 = time.time()
            ok = upload_skill(token, name, path)
            dur = time.time() - t0
            if ok:
                success += 1
                print(f"[{i}/{len(to_upload)}] OK ({dur:.2f}s): {name}")
            else:
                failed += 1
                print(f"[{i}/{len(to_upload)}] FALHA: {name}")
        except Exception as e:
            failed += 1
            print(f"[{i}/{len(to_upload)}] ERRO {name}: {e}")

    print("\n" + "="*50)
    print(f"Finalizado: {success} enviadas com sucesso, {failed} falhas.")
    print("="*50)

if __name__ == "__main__":
    main()
