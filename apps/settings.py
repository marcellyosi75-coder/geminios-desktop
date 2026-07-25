from window import AppWindow
import tkinter as tk
import time

class Settings(AppWindow):
    def __init__(self, master):
        super().__init__(master, "Pengaturan - GeminiOS", 750, 500)
        self.desktop_ref = master

        # Versi OS saat ini
        self.current_version = "v1.0.0"

        # Container Utama (Material Dark Surface)
        main_container = tk.Frame(self.body, bg="#121212")
        main_container.pack(fill="both", expand=True)

        # -----------------------------------------------------------------
        # SIDEBAR LEFT
        # -----------------------------------------------------------------
        self.sidebar = tk.Frame(main_container, bg="#1e1e24", width=210)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Title Header
        tk.Label(
            self.sidebar, text="GeminiOS", bg="#1e1e24", fg="#8ab4f8",
            font=("Arial", 12, "bold"), anchor="w", padx=16, pady=18
        ).pack(fill="x")

        # Area Konten Kanan
        self.content_area = tk.Frame(main_container, bg="#121212")
        self.content_area.pack(side="right", fill="both", expand=True, padx=20, pady=15)

        self.nav_buttons = {}

        # Daftar Menu Navigasi
        self.add_nav_item("🎨  Tampilan", self.show_appearance_page)
        self.add_nav_item("⚙️  Sistem", self.show_system_page)
        self.add_nav_item("ℹ️  Tentang OS & Update", self.show_about_page)

        # Halaman Default
        self.switch_page("🎨  Tampilan", self.show_appearance_page)

    def add_nav_item(self, text, command):
        btn = tk.Button(
            self.sidebar, text=text, bg="#1e1e24", fg="#bdc1c6",
            activebackground="#2a2b32", activeforeground="#8ab4f8",
            bd=0, relief="flat", anchor="w", font=("Arial", 10),
            padx=16, pady=10, command=lambda: self.switch_page(text, command)
        )
        btn.pack(fill="x", pady=2)
        self.nav_buttons[text] = btn

    def switch_page(self, title, page_func):
        for name, btn in self.nav_buttons.items():
            if name == title:
                btn.config(bg="#2d2f39", fg="#8ab4f8", font=("Arial", 10, "bold"))
            else:
                btn.config(bg="#1e1e24", fg="#bdc1c6", font=("Arial", 10))

        for child in self.content_area.winfo_children():
            child.destroy()

        page_func()

    def create_card(self, title, desc=""):
        card = tk.Frame(self.content_area, bg="#1e1e24", bd=0, relief="flat")
        card.pack(fill="x", pady=8, ipady=6)

        tk.Label(
            card, text=title, bg="#1e1e24", fg="#e8eaed",
            font=("Arial", 10, "bold"), anchor="w"
        ).pack(fill="x", padx=14, pady=(10, 2))

        if desc:
            tk.Label(
                card, text=desc, bg="#1e1e24", fg="#9aa0a6",
                font=("Arial", 9), anchor="w"
            ).pack(fill="x", padx=14, pady=(0, 8))

        return card

    # -----------------------------------------------------------------
    # HALAMAN 1: TAMPILAN
    # -----------------------------------------------------------------
    def show_appearance_page(self):
        tk.Label(
            self.content_area, text="Tampilan & Warna", bg="#121212", fg="#8ab4f8",
            font=("Arial", 14, "bold"), anchor="w"
        ).pack(fill="x", pady=(0, 10))

        card_bg = self.create_card("Warna Background Desktop", "Ubah warna wallpaper desktop secara langsung")
        palette_frame = tk.Frame(card_bg, bg="#1e1e24")
        palette_frame.pack(fill="x", padx=14, pady=8)

        colors = [
            ("#1d3557", "Default Blue"),
            ("#121212", "Dark Void"),
            ("#2d3748", "Slate Gray"),
            ("#3c1361", "Deep Purple"),
            ("#0f3460", "Midnight Navy")
        ]

        for hex_code, name in colors:
            btn = tk.Button(
                palette_frame, text=name, bg=hex_code, fg="white",
                bd=0, relief="flat", font=("Arial", 8, "bold"),
                padx=10, pady=6,
                command=lambda c=hex_code: self.change_desktop_bg(c)
            )
            btn.pack(side="left", padx=4, pady=4)

    def change_desktop_bg(self, color):
        if hasattr(self.desktop_ref, 'desktop'):
            self.desktop_ref.desktop.config(bg=color)

    # -----------------------------------------------------------------
    # HALAMAN 2: SISTEM
    # -----------------------------------------------------------------
    def show_system_page(self):
        tk.Label(
            self.content_area, text="Sistem Perangkat", bg="#121212", fg="#8ab4f8",
            font=("Arial", 14, "bold"), anchor="w"
        ).pack(fill="x", pady=(0, 10))

        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.create_card("Resolusi Layar", f"Display Server: {w} x {h} Pixels")
        self.create_card("Lingkungan Eksekusi", "Termux:X11 + Python Tkinter Subsystem Engine")

    # -----------------------------------------------------------------
    # HALAMAN 3: TENTANG OS & SYSTEM UPDATE (FITUR BARU)
    # -----------------------------------------------------------------
    def show_about_page(self):
        tk.Label(
            self.content_area, text="Tentang OS & Pembaruan", bg="#121212", fg="#8ab4f8",
            font=("Arial", 14, "bold"), anchor="w"
        ).pack(fill="x", pady=(0, 10))

        # Card Informasi OS
        card_about = self.create_card("GeminiOS Desktop Environment", f"Versi Terpasang: {self.current_version}")
        info_text = (
            "• Subsystem Engine: Python 3 & Tkinter\n"
            "• UI Framework: Custom Material Dark UI\n"
            "• Target Host: Termux X11 Server"
        )
        tk.Label(
            card_about, text=info_text, bg="#1e1e24", fg="#bdc1c6",
            font=("Arial", 9), justify="left", anchor="w"
        ).pack(fill="x", padx=14, pady=(2, 10))

        # Card Pembaruan Sistem (Update Manager)
        card_update = self.create_card("Pembaruan Sistem (Software Update)", "Periksa repositori untuk mendapatkan fitur terbaru")

        update_frame = tk.Frame(card_update, bg="#1e1e24")
        update_frame.pack(fill="x", padx=14, pady=5)

        self.update_btn = tk.Button(
            update_frame, text="🔄  Cek Pembaruan", bg="#007acc", fg="white",
            activebackground="#005999", activeforeground="white",
            bd=0, relief="flat", font=("Arial", 9, "bold"), padx=12, pady=6,
            command=self.check_for_updates
        )
        self.update_btn.pack(side="left", pady=5)

        self.update_status = tk.Label(
            update_frame, text="Sistem Anda siap diperbarui.", bg="#1e1e24", fg="#bdc1c6",
            font=("Arial", 9)
        )
        self.update_status.pack(side="left", padx=15)

    def check_for_updates(self):
        """Simulasi Proses Update Berbasis Repositori Linux"""
        self.update_btn.config(state="disabled", bg="#404040")
        
        # Langkah 1: Menghubungkan ke Repo
        self.update_status.config(text="[1/3] Menghubungkan ke repositori server...", fg="#8ab4f8")
        self.update_idletasks()
        self.after(1200, self._update_step2)

    def _update_step2(self):
        # Langkah 2: Memeriksa Manifest/Versi
        self.update_status.config(text="[2/3] Membandingkan manifest paket lokal vs server...", fg="#8ab4f8")
        self.update_idletasks()
        self.after(1500, self._update_step3)

    def _update_step3(self):
        # Langkah 3: Hasil Pemeriksaan
        self.update_status.config(text="✓ GeminiOS sudah menggunakan versi terbaru (v1.0.0).", fg="#81c784")
        self.update_btn.config(state="normal", bg="#007acc")
