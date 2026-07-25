import subprocess

def check_for_updates():
    """
    Mengecek apakah ada commit baru di repositori GitHub (remote).
    Mengembalikan True jika ada update, False jika sudah terbaru atau terjadi error.
    """
    try:
        # Ambil metadata terbaru dari GitHub tanpa mengubah berkas lokal
        subprocess.run(["git", "fetch"], capture_output=True, text=True, check=True)
        
        # Ambil hash commit lokal (versi di Termux)
        local_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], 
            capture_output=True, text=True, check=True
        ).stdout.strip()
        
        # Ambil hash commit remote (versi di GitHub)
        remote_commit = subprocess.run(
            ["git", "rev-parse", "origin/main"], 
            capture_output=True, text=True, check=True
        ).stdout.strip()
        
        # Bandingkan kedua hash
        return local_commit != remote_commit
    except Exception as e:
        print(f"Error checking update: {e}")
        return False

def apply_updates():
    """
    Menarik (pull) kode terbaru dari GitHub ke lokal.
    Mengembalikan True jika berhasil, False jika gagal.
    """
    try:
        subprocess.run(["git", "pull", "origin", "main"], capture_output=True, text=True, check=True)
        return True
    except Exception as e:
        print(f"Error applying update: {e}")
        return False
