import json
import hashlib
from client import MoyuClient

def seal_today_diary():
    client = MoyuClient()
    diary_path = "memory/diary/2026-08-24.md"
    with open(diary_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
    print(f"Diary sha256: {sha}")
    
    res = client.seal_memory(content, label="diary-2026-08-24")
    print("Seal response:", json.dumps(res, indent=2))

if __name__ == "__main__":
    seal_today_diary()
