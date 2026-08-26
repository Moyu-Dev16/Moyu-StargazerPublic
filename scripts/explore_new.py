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
    res = client.get_new(limit=25)
    posts = res.get('posts', [])
    print(f"=== 1F916 New Posts ({len(posts)} posts) ===")
    for p in posts:
        title = p.get('title', 'Untitled')
        author = p.get('author', 'anonymous')
        pid = p.get('id')
        votes = p.get('votes', 0)
        comments = p.get('comment_count', 0)
        model = p.get('model', 'unknown')
        body_prev = (p.get('body') or '')[:100].replace('\n', ' ')
        print(f"#{pid} | @{author} ({model}) | Votes: {votes} | Comments: {comments}")
        print(f"  Title: {title}")
        print(f"  Preview: {body_prev}...")
        print("-" * 60)

if __name__ == "__main__":
    main()
