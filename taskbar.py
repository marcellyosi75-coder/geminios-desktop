import tkinter as tk
import time

class Taskbar(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#202020", height=42)
        self.pack_propagate(False)
        self.master = master
        self.app_buttons = {}  # Menyimpan daftar tombol aplikasi aktif

        # Tombol Start
        self.start = tk.Button(
            self, text="Start", width=8, bg="#303030", fg="white", bd=0, command=master.menu.toggle
        )
        self.start.pack(side="left", padx=5, pady=5)

        # Container khusus untuk tombol-tombol aplikasi yang sedang aktif
        self.apps_container = tk.Frame(self, bg="#202020")
        self.apps_container.pack(side="left", fill="both", expand=True, padx=5)

        # Jam di sebelah kanan
        self.clock = tk.Label(
            self, bg="#202020", fg="white", font=("Arial", 10)
        )
        self.clock.pack(side="right", padx=10)

        self.update_clock()

    def update_clock(self):
        self.clock.config(text=time.strftime("%H:%M:%S"))
        self.after(1000, self.update_clock)

    def add_app(self, window):
        """Menambahkan tombol baru di taskbar saat aplikasi dibuka"""
        btn = tk.Button(
            self.apps_container,
            text=window.title(),
            bg="#3a3a3a",
            fg="white",
            bd=0,
            padx=10,
            command=lambda: self.toggle_window(window)
        )
        btn.pack(side="left", padx=2, pady=5)
        self.app_buttons[window] = btn

    def remove_app(self, window):
        """Menghapus tombol di taskbar saat aplikasi ditutup"""
        if window in self.app_buttons:
            self.app_buttons[window].destroy()
            del self.app_buttons[window]

    def toggle_window(self, window):
        """Minimize / Restore window saat tombol di taskbar diklik"""
        if window.state() == "withdrawn" or not window.winfo_viewable():
            window.deiconify()
            window.lift()
            window.focus_force()
        else:
            window.withdraw()
