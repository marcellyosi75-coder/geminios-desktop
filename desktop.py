import tkinter as tk
from startmenu import StartMenu
from taskbar import Taskbar

class Desktop(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Konfigurasi Jendela Utama Menyesuaikan Layar Penuh (Native)
        self.title("GeminiOS")
        
        # Mengambil resolusi layar perangkat secara otomatis
        screen_w = self.winfo_screenwidth()
        screen_h = self.winfo_screenheight()
        self.geometry(f"{screen_w}x{screen_h}+0+0")
        
        # Opsional: Jika ingin benar-benar fullscreen tanpa border window bawaan OS
        # self.attributes("-fullscreen", True)

        self.configure(bg="#1e1e2e")

        # Inisialisasi variabel status Start Menu
        self.start_menu_window = None

        # Panggil Taskbar dan sambungkan tombol start ke fungsi toggle
        self.taskbar = Taskbar(self, on_start_click=self.toggle_start_menu)

    def toggle_start_menu(self):
        # Jika Start Menu sudah ada, tutup (toggle off)
        if self.start_menu_window and self.start_menu_window.winfo_exists():
            self.start_menu_window.destroy()
            self.start_menu_window = None
        else:
            # Jika belum ada, buat dan tampilkan Start Menu di atas taskbar
            self.start_menu_window = StartMenu(self)
            
            # Hitung posisi Y agar berada tepat di atas taskbar (tinggi taskbar 40px)
            menu_height = 280
            menu_width = 240
            pos_y = self.winfo_height() - menu_height - 45
            
            self.start_menu_window.place(x=5, y=pos_y, width=menu_width, height=menu_height)
            self.start_menu_window.lift() # Bawa ke lapisan paling depan

