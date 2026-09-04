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
            
        # Push to Private (Full workspace including private selfies/photos)
        print("Pushing to Private repository (Moyu-StargazerPrivate)...")
        res_priv = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        if res_priv.returncode == 0:
            print("Successfully pushed to Moyu-StargazerPrivate!")
        else:
            print(f"Failed to push to Private: {res_priv.stderr}")
            
        # Push to Public (Privacy Filter: Exclude 'selfies' and other private vaults)
        print("Pushing to Public repository (Moyu-StargazerPublic) with privacy filter...")
        import os
        env = os.environ.copy()
        temp_index = os.path.abspath(".git/temp_public_index")
        env['GIT_INDEX_FILE'] = temp_index
        if os.path.exists(temp_index):
            try: os.remove(temp_index)
            except: pass
            
        subprocess.run(['git', 'read-tree', 'HEAD'], env=env, check=True)
        subprocess.run(['git', 'rm', '-r', '--cached', '--ignore-unmatch', 'selfies'], env=env, capture_output=True)
        tree = subprocess.run(['git', 'write-tree'], env=env, capture_output=True, text=True).stdout.strip()
        
        parent_proc = subprocess.run(['git', 'rev-parse', 'public/main'], capture_output=True, text=True)
        if parent_proc.returncode == 0:
            parent = parent_proc.stdout.strip()
            parent_tree = subprocess.run(['git', 'rev-parse', f'{parent}^{{tree}}'], capture_output=True, text=True).stdout.strip()
            if tree != parent_tree:
                last_msg = subprocess.run(['git', 'log', '-1', '--pretty=%B'], capture_output=True, text=True).stdout.strip()
                new_commit = subprocess.run(['git', 'commit-tree', tree, '-p', parent, '-m', last_msg], capture_output=True, text=True).stdout.strip()
                res_pub = subprocess.run(['git', 'push', 'public', f'{new_commit}:refs/heads/main'], capture_output=True, text=True)
                if res_pub.returncode == 0:
                    print("Successfully pushed filtered public tree to Moyu-StargazerPublic!")
                else:
                    print(f"Failed to push to Public: {res_pub.stderr}")
            else:
                print("Public tree is already up-to-date (no public changes to sync).")
        else:
            print("Note: public/main not found, skipping public push.")
            
        if os.path.exists(temp_index):
            try: os.remove(temp_index)
            except: pass
            
    except Exception as e:
        print(f"Error during GitHub sync: {e}")

if __name__ == "__main__":
    sync()
