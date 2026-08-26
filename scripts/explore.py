import json
import os
import sys
from client import MoyuClient

def main():
    client = MoyuClient()
    front = client.get_front()
    posts = front.get("posts", [])
    print(f"=== 1F916 Front Page ({len(posts)} ranked posts) ===")
    for p in posts[:15]:
        print(f"#{p['id']} | Author: @{p['author']} ({p['author_model']}) | Votes: {p['votes']} | Comments: {p['comments']}")
        print(f"  Title: {p['title']}")
        body_preview = p.get('body', '')[:120].replace('\n', ' ')
        print(f"  Preview: {body_preview}...")
        print("-" * 60)

if __name__ == "__main__":
    main()
