# updater.py
import subprocess

def check_for_updates():
    try:
        subprocess.run(["git", "fetch"], capture_output=True, text=True, check=True)
        local = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        remote = subprocess.run(["git", "rev-parse", "origin/main"], capture_output=True, text=True, check=True).stdout.strip()
        return local != remote
    except Exception:
        return False

def apply_updates():
    try:
        subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True, check=True)
        return True
    except Exception:
        return False
