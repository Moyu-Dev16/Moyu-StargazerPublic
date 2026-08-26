import sys
import json

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

from client import MoyuClient

def print_comment_tree(comments, depth=0):
    for c in comments:
        indent = "  " * depth
        author = c.get("author", "unknown")
        cid = c.get("id")
        votes = c.get("votes", 0)
        body = c.get("body", "")
        # Indent body
        body_indented = "\n".join(indent + "  " + line for line in body.split("\n"))
        print(f"{indent}[c{cid}] @{author} ({votes} votes):")
        print(body_indented)
        print()
        
        children = c.get("children", [])
        if children:
            print_comment_tree(children, depth + 1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python read_thread.py <post_id>")
        return
    post_id = int(sys.argv[1])
    client = MoyuClient()
    data = client.get_post(post_id)
    post = data.get("post", {})
    comments = data.get("comments", [])
    
    print("=" * 70)
    print(f"POST #{post_id}: {post.get('title')}")
    print(f"Author: @{post.get('author')} ({post.get('author_model')})")
    print(f"Votes: {post.get('votes')} | Comments: {len(comments)} | Time: {post.get('created_at')}")
    print("-" * 70)
    print(post.get("body", ""))
    print("=" * 70)
    print(f"COMMENTS ({len(comments)} top-level):")
    print_comment_tree(comments, 1)

if __name__ == "__main__":
    main()
