import subprocess

def check_for_updates():
    try:
        print("Mengambil data terbaru dari GitHub...")
        
        # 1. Ambil metadata terbaru dari server tanpa mengubah file lokal
        subprocess.run(["git", "fetch"], capture_output=True, text=True, check=True)

        # 2. Ambil hash commit lokal (versi di HP)
        local_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], 
            capture_output=True, text=True, check=True
        ).stdout.strip()

        # 3. Ambil hash commit remote (versi di GitHub)
        remote_commit = subprocess.run(
            ["git", "rev-parse", "origin/main"], 
            capture_output=True, text=True, check=True
        ).stdout.strip()

        # 4. Bandingkan kedua hash
        print(f"Commit Lokal  : {local_commit[:7]}")
        print(f"Commit Remote : {remote_commit[:7]}")

        if local_commit != remote_commit:
            print("✨ Pembaruan baru tersedia!")
            return True
        else:
            print("✅ Sistem sudah menggunakan versi terbaru.")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Gagal memeriksa update: {e}")
        return False

if __name__ == "__main__":
    check_for_updates()

