import subprocess
import tkinter as tk

def apply_x11_desktop_cursor():
    """Mengubah kursor root Termux X11 dari 'X' menjadi panah desktop"""
    try:
        subprocess.run(["xsetroot", "-cursor_name", "left_ptr"], check=True)
    except Exception:
        pass

if __name__ == "__main__":
    # 1. Ubah kursor sistem X11
    apply_x11_desktop_cursor()

    # 2. Import dan jalankan Desktop
    from desktop import Desktop
    app = Desktop()

    # 3. Ambil window Tkinter utama secara otomatis & terapkan kursor panah
    root = tk._default_root
    if root:
        root.config(cursor="left_ptr")
        root.option_add("*cursor", "left_ptr")
        root.mainloop()
