import tkinter as tk
import threading

# Import updater secara aman
try:
    from updater import check_for_updates, apply_updates
except ImportError:
    def check_for_updates(): return False
    def apply_updates(): return False

class Settings:
    def __init__(self, parent=None):
        self.parent = parent
        self._is_maximized = False
        self._prev_geometry = "580x380+50+50"

        # ------------------- MODE WADAH WINDOW (DESKTOP / STANDALONE) -------------------
        if isinstance(parent, (tk.Tk, tk.Toplevel)) or parent is None:
            if parent is None or isinstance(parent, tk.Tk):
                self.win = tk.Toplevel(parent) if parent else tk.Tk()
            else:
                self.win = parent
            
            self.win.title("Pengaturan")
            self.win.geometry("580x380")
            self.win.configure(bg="#1e1e2e")
            self.win.overrideredirect(True) # Hilangkan border bawaan HP

            # ------------------- TITLEBAR DRAGGABLE -------------------
            self.title_bar = tk.Frame(self.win, bg="#11111b", height=32)
            self.title_bar.pack(fill="x", side="top")
            self.title_bar.pack_propagate(False)

            # Judul Window
            lbl_title = tk.Label(self.title_bar, text="⚙️ Pengaturan", fg="#cdd6f4", bg="#11111b", font=("Helvetica", 9, "bold"))
            lbl_title.pack(side="left", padx=10)

            # 1. Tombol Close (✕)
            btn_close = tk.Button(
                self.title_bar, text="✕", fg="#ffffff", bg="#f38ba8", activebackground="#e85d75",
                bd=0, padx=12, cursor="hand2", command=self.close_window, font=("Helvetica", 9, "bold")
            )
            btn_close.pack(side="right", fill="y")

            # 2. Tombol Maximize / Restore (□ / ❐)
            self.btn_max = tk.Button(
                self.title_bar, text="□", fg="#cdd6f4", bg="#11111b", activebackground="#313244", activeforeground="#ffffff",
                bd=0, padx=10, cursor="hand2", command=self.toggle_maximize, font=("Helvetica", 9, "bold")
            )
            self.btn_max.pack(side="right", fill="y")

            # 3. Tombol Minimize (─)
            btn_min = tk.Button(
                self.title_bar, text="─", fg="#cdd6f4", bg="#11111b", activebackground="#313244", activeforeground="#ffffff",
                bd=0, padx=10, cursor="hand2", command=self.minimize_window, font=("Helvetica", 9, "bold")
            )
            btn_min.pack(side="right", fill="y")

            # Event Binding Drag & Double Click Titlebar
            self.title_bar.bind("<ButtonPress-1>", self.start_drag)
            self.title_bar.bind("<B1-Motion>", self.do_drag)
            self.title_bar.bind("<Double-Button-1>", lambda e: self.toggle_maximize())
            lbl_title.bind("<ButtonPress-1>", self.start_drag)
            lbl_title.bind("<B1-Motion>", self.do_drag)
            lbl_title.bind("<Double-Button-1>", lambda e: self.toggle_maximize())

            self.container = tk.Frame(self.win, bg="#1e1e2e")
            self.container.pack(fill="both", expand=True)
        else:
            # Mode Integrasi GeminiOS (Dikontrol oleh window.py)
            self.container = tk.Frame(self.parent, bg="#1e1e2e")
            self.container.pack(fill="both", expand=True)

        # ------------------- SIDEBAR (KIRI) -------------------
        self.sidebar = tk.Frame(self.container, bg="#181825", width=160)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        lbl_sidebar_title = tk.Label(
            self.sidebar, text="⚙️ Pengaturan", 
            font=("Helvetica", 11, "bold"), fg="#cdd6f4", bg="#181825"
        )
        lbl_sidebar_title.pack(pady=(15, 12), padx=12, anchor="w")

        self.btn_sys = self.create_sidebar_btn("🖥️ Sistem", self.show_sistem)
        self.btn_update = self.create_sidebar_btn("ℹ️ Update OS", self.show_update)

        # ------------------- CONTENT AREA (KANAN) -------------------
        self.content_area = tk.Frame(self.container, bg="#1e1e2e")
        self.content_area.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        # Tampilkan Tab Sistem secara default
        self.show_sistem()

    # ------------------- FUNGSI KONTROL JENDELA -------------------
    def start_drag(self, event):
        if not self._is_maximized:
            self._drag_x = event.x
            self._drag_y = event.y

    def do_drag(self, event):
        if not self._is_maximized:
            x = self.win.winfo_x() + (event.x - self._drag_x)
            y = self.win.winfo_y() + (event.y - self._drag_y)
            self.win.geometry(f"+{x}+{y}")

    def minimize_window(self):
        if hasattr(self, 'win'):
            self.win.withdraw()  # Meminimalkan/menyembunyikan window

    def toggle_maximize(self):
        if not hasattr(self, 'win'):
            return
        if self._is_maximized:
            # Restore ke ukuran semula
            self.win.geometry(self._prev_geometry)
            self._is_maximized = False
            self.btn_max.config(text="□")
        else:
            # Maximize memenuhi layar
            self._prev_geometry = self.win.geometry()
            sw = self.win.winfo_screenwidth()
            sh = self.win.winfo_screenheight()
            self.win.geometry(f"{sw}x{sh}+0+0")
            self._is_maximized = True
            self.btn_max.config(text="❐")

    def close_window(self):
        if hasattr(self, 'win'):
            self.win.destroy()

    def create_sidebar_btn(self, text, command):
        btn = tk.Button(
            self.sidebar, text=text, font=("Helvetica", 10),
            fg="#a6adc8", bg="#181825", activeforeground="#cdd6f4", activebackground="#313244",
            bd=0, anchor="w", padx=12, pady=8, cursor="hand2", command=command
        )
        btn.pack(fill="x", pady=2)
        return btn

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    # ------------------- TAB 1: SISTEM (Info Ala Ubuntu) -------------------
    def show_sistem(self):
        self.clear_content()

        title = tk.Label(self.content_area, text="Tentang Sistem", font=("Helvetica", 13, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        title.pack(anchor="w", pady=(0, 10))

        card = tk.Frame(self.content_area, bg="#313244", padx=20, pady=15)
        card.pack(fill="both", expand=True)

        lbl_icon = tk.Label(card, text="💻", font=("Segoe UI Emoji", 30), bg="#313244")
        lbl_icon.pack(pady=(2, 2))

        lbl_os_name = tk.Label(card, text="GeminiOS Desktop", font=("Helvetica", 12, "bold"), fg="#89b4fa", bg="#313244")
        lbl_os_name.pack(pady=(0, 10))

        specs_frame = tk.Frame(card, bg="#1e1e2e", padx=12, pady=10)
        specs_frame.pack(fill="x", pady=2)

        def add_spec_row(parent, label, value):
            row = tk.Frame(parent, bg="#1e1e2e")
            row.pack(fill="x", pady=3)
            lbl_key = tk.Label(row, text=label, font=("Helvetica", 9, "bold"), fg="#a6adc8", bg="#1e1e2e", width=14, anchor="w")
            lbl_key.pack(side="left")
            lbl_val = tk.Label(row, text=value, font=("Helvetica", 9), fg="#cdd6f4", bg="#1e1e2e", anchor="w")
            lbl_val.pack(side="left", fill="x", expand=True)

        add_spec_row(specs_frame, "Versi OS", "v1.0.0 (Stable)")
        add_spec_row(specs_frame, "Lingkungan", "Termux X11 / Python Tkinter")
        add_spec_row(specs_frame, "Pembuat", "marcellyosi75-coder")
        add_spec_row(specs_frame, "Arsitektur", "ARM64 / Linux")

    # ------------------- TAB 2: UPDATE OS -------------------
    def show_update(self):
        self.clear_content()
        
        title = tk.Label(self.content_area, text="Pembaruan Sistem", font=("Helvetica", 13, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        title.pack(anchor="w", pady=(0, 10))

        card = tk.Frame(self.content_area, bg="#313244", padx=20, pady=20)
        card.pack(fill="both", expand=True)

        lbl_update_icon = tk.Label(card, text="🔄", font=("Segoe UI Emoji", 24), bg="#313244")
        lbl_update_icon.pack(pady=(0, 5))

        lbl_update_title = tk.Label(card, text="Pembaruan Perangkat Lunak", font=("Helvetica", 11, "bold"), fg="#cdd6f4", bg="#313244")
        lbl_update_title.pack(pady=(0, 8))

        self.lbl_status = tk.Label(
            card, 
            text="Tekan tombol di bawah untuk memeriksa versi terbaru dari server.", 
            font=("Helvetica", 10), fg="#a6adc8", bg="#313244", wraplength=320, justify="center"
        )
        self.lbl_status.pack(pady=12)

        self.btn_check = tk.Button(
            card, text="Cek Pembaruan", font=("Helvetica", 10, "bold"),
            bg="#89b4fa", fg="#11111b", activebackground="#74c7ec",
            bd=0, padx=18, pady=8, cursor="hand2", command=self.on_check_update
        )
        self.btn_check.pack(pady=5)

    def on_check_update(self):
        self.lbl_status.config(text="Memeriksa pembaruan dari server...", fg="#89b4fa")
        self.btn_check.config(state="disabled")

        def worker():
            try:
                has_update = check_for_updates()
                if has_update:
                    self.lbl_status.config(text="✨ Pembaruan baru tersedia di server!", fg="#fab387")
                    self.btn_check.config(
                        state="normal", text="Pasang Sekarang", bg="#a6e3a1", command=self.on_apply_update
                    )
                else:
                    self.lbl_status.config(text="✅ Sistem Anda sudah menggunakan versi terbaru.", fg="#a6e3a1")
                    self.btn_check.config(
                        state="normal", text="Cek Pembaruan", bg="#89b4fa", command=self.on_check_update
                    )
            except Exception as e:
                self.lbl_status.config(text="Terjadi kesalahan koneksi.", fg="#f38ba8")
                self.btn_check.config(state="normal", text="Cek Pembaruan")

        threading.Thread(target=worker, daemon=True).start()

    def on_apply_update(self):
        self.lbl_status.config(text="Sedang mengunduh pembaruan...", fg="#89b4fa")
        self.btn_check.config(state="disabled")

        def worker():
            try:
                success = apply_updates()
                if success:
                    self.lbl_status.config(text="✅ Berhasil diperbarui! Silakan restart aplikasi.", fg="#a6e3a1")
                    self.btn_check.config(state="disabled", text="Terpasang", bg="#45475a")
                else:
                    self.lbl_status.config(text="❌ Gagal mengunduh pembaruan.", fg="#f38ba8")
                    self.btn_check.config(
                        state="normal", text="Coba Lagi", bg="#f38ba8", command=self.on_apply_update
                    )
            except Exception as e:
                self.lbl_status.config(text="Terjadi kesalahan saat menginstal.", fg="#f38ba8")
                self.btn_check.config(state="normal", text="Coba Lagi")

        threading.Thread(target=worker, daemon=True).start()

# Alias
SettingsApp = Settings

if __name__ == "__main__":
    app = Settings()
    app.win.mainloop()
