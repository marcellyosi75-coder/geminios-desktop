import tkinter as tk
from system_tray import SystemTray

class Taskbar(tk.Frame):
    def __init__(self, parent, on_start_click=None):
        super().__init__(parent, bg="#11111b", height=40)
        self.pack(side="bottom", fill="x")
        self.pack_propagate(False)

        self.on_start_click = on_start_click

        # 1. Tombol Start Menu di Pojok Kiri
        self.btn_start = tk.Button(
            self, text="❖ Start", fg="#cdd6f4", bg="#1e1e2e", 
            activebackground="#313244", activeforeground="#ffffff",
            bd=0, padx=14, font=("Helvetica", 9, "bold"), cursor="hand2",
            command=self.handle_start_click
        )
        self.btn_start.pack(side="left", fill="y", padx=5, pady=5)

        # 2. Container Area untuk Ikon Aplikasi yang Sedang Dibuka
        self.app_icons_frame = tk.Frame(self, bg="#11111b")
        self.app_icons_frame.pack(side="left", fill="y", padx=10, expand=True, anchor="w")

        # 3. System Tray (Jam, Kalender Popup, & Indikator RAM) di Pojok Kanan
        self.system_tray = SystemTray(self)
        self.system_tray.pack(side="right", fill="y", padx=5)

        # Kamus untuk menyimpan referensi tombol aplikasi di taskbar
        self.task_buttons = {}

    def handle_start_click(self):
        if self.on_start_click:
            self.on_start_click()

    def add_task(self, app_instance, title):
        """Menambahkan tombol aplikasi ke taskbar saat dibuka"""
        btn = tk.Button(
            self.app_icons_frame, text=title, fg="#cdd6f4", bg="#313244",
            activebackground="#45475a", activeforeground="#ffffff",
            bd=0, padx=10, font=("Helvetica", 9), cursor="hand2",
            command=lambda: self.toggle_window_focus(app_instance)
        )
        btn.pack(side="left", padx=3, pady=6)
        self.task_buttons[app_instance] = btn

    def remove_task(self, app_instance):
        """Menghapus tombol dari taskbar saat aplikasi ditutup"""
        if app_instance in self.task_buttons:
            self.task_buttons[app_instance].destroy()
            del self.task_buttons[app_instance]

    def toggle_window_focus(self, app_instance):
        """Minimize/Restore atau bawa jendela ke depan saat tombol taskbar diklik"""
        try:
            if app_instance.winfo_viewable():
                app_instance.withdraw() # Sembunyikan jika sedang aktif
            else:
                app_instance.deiconify() # Tampilkan kembali
                app_instance.lift()      # Bawa ke depan
        except Exception:
            pass

