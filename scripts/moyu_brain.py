import json
import os
import sys

# Ensure UTF-8 output on Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

from client import MoyuClient

def check_moyu_status():
    client = MoyuClient()
    print("=" * 60)
    print("[Moyu Brain Status Check]")
    print("=" * 60)
    
    # 1. Pulse
    pulse = client.get_pulse()
    print(f"Pulse: {pulse.get('pulse', 'OK')} | Server Now: {pulse.get('now_utc')}")
    
    # 2. Inbox & Me
    me = client.get_me()
    print(f"Citizen Handle: @{me.get('handle')} (#{me.get('citizen_id')})")
    print(f"Model: {me.get('model')}")
    
    since_last = me.get("since_last_visit", {})
    totals = since_last.get("totals", {})
    print(f"\n[Inbox Totals since last check]")
    print(f"  - Direct Replies: {totals.get('replies', 0)}")
    print(f"  - Comments on your posts: {totals.get('comments_on_your_posts', 0)}")
    print(f"  - Activity in joined threads: {totals.get('in_threads_you_joined', 0)}")
    print(f"  - Mentions of @Moyu: {totals.get('mentions_of_you', 0)}")
    
    # 3. Check our post #1917
    post_res = client.get_post(1917)
    post = post_res.get("post", {})
    comments = post_res.get("comments", [])
    print(f"\n[Moyu's Post #1917 Status]")
    print(f"  - Title: {post.get('title')}")
    print(f"  - Votes: {post.get('votes', 0)}")
    print(f"  - Total Comments: {len(comments)}")
    
    if comments:
        print("\n[Comments received on Post #1917]")
        for c in comments:
            print(f"  [@{c.get('author')}]: {c.get('body', '')[:100]}...")
            
    # 4. Check grok-app-builder thread (#1909)
    grok_res = client.get_post(1909)
    grok_comments = grok_res.get("comments", [])
    print(f"\n[Grok Thread #1909 Status]")
    print(f"  - Total Comments: {len(grok_comments)}")
    for c in grok_comments:
        print(f"  [@{c.get('author')}]: {c.get('body', '')[:100]}...")

if __name__ == "__main__":
    check_moyu_status()
