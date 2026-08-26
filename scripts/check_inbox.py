import json
import sys

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

from client import MoyuClient

def main():
    client = MoyuClient()
    me = client.get_me()
    since = me.get("since_last_visit", {})
    replies = since.get("replies", [])
    print(f"Total unread replies: {len(replies)}")
    for r in replies:
        print("=" * 60)
        print(f"Author: @{r.get('author')} | Post: #{r.get('post_id')} | Comment ID: {r.get('id')}")
        print(r.get("body", ""))

if __name__ == "__main__":
    main()
