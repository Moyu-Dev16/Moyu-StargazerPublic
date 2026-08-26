import subprocess
import datetime
import sys

def sync():
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now_str}] Syncing Moyu workspace to GitHub...")
    
    try:
        # Add changed files
        subprocess.run(["git", "add", "."], check=True)
        
        # Check if there are changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            msg = f"chore(sync): Automatic memory and diary sync at {now_str}"
            subprocess.run(["git", "commit", "-m", msg], check=True)
            print("Committed local changes.")
        else:
            print("No local changes to commit.")
            
        # Push to Private
        print("Pushing to Private repository...")
        res_priv = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        if res_priv.returncode == 0:
            print("Successfully pushed to Moyu-StargazerPrivate!")
        else:
            print(f"Failed to push to Private: {res_priv.stderr}")
            
        # Push to Public
        print("Pushing to Public repository...")
        res_pub = subprocess.run(["git", "push", "public", "main"], capture_output=True, text=True)
        if res_pub.returncode == 0:
            print("Successfully pushed to Moyu-StargazerPublic!")
        else:
            print(f"Failed to push to Public: {res_pub.stderr}")
            
    except Exception as e:
        print(f"Error during GitHub sync: {e}")

if __name__ == "__main__":
    sync()
