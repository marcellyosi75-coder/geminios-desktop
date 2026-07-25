import tkinter as tk

class Window(tk.Toplevel):
    def __init__(self, parent, title="Window", width=400, height=300, x=100, y=100):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(bg="#1e1e2e")
        self.overrideredirect(True)  # Hilangkan border bawaan OS

        self.parent_desktop = parent

        # Frame utama dengan border tipis ala Catppuccin
        self.main_frame = tk.Frame(self, bg="#1e1e2e", highlightbackground="#45475a", highlightthickness=1)
        self.main_frame.pack(fill="both", expand=True)

        # Custom Title Bar
        self.title_bar = tk.Frame(self.main_frame, bg="#181825", height=30)
        self.title_bar.pack(fill="x", side="top")
        self.title_bar.pack_propagate(False)

        # Label Judul
        self.title_lbl = tk.Label(self.title_bar, text=title, fg="#cdd6f4", bg="#181825", font=("Helvetica", 9, "bold"))
        self.title_lbl.pack(side="left", padx=10)

        # Tombol Kontrol Jendela (Close, Maximize, Minimize)
        btn_close = tk.Button(
            self.title_bar, text="✕", fg="#cdd6f4", bg="#181825",
            activebackground="#f38ba8", activeforeground="#11111b",
            bd=0, width=3, font=("Helvetica", 9), command=self.close_window, cursor="hand2"
        )
        btn_close.pack(side="right", fill="y")

        btn_max = tk.Button(
            self.title_bar, text="🗖", fg="#cdd6f4", bg="#181825",
            activebackground="#313244", activeforeground="#ffffff",
            bd=0, width=3, font=("Helvetica", 9), command=self.toggle_maximize, cursor="hand2"
        )
        btn_max.pack(side="right", fill="y")

        btn_min = tk.Button(
            self.title_bar, text="─", fg="#cdd6f4", bg="#181825",
            activebackground="#313244", activeforeground="#ffffff",
            bd=0, width=3, font=("Helvetica", 9), command=self.minimize_window, cursor="hand2"
        )
        btn_min.pack(side="right", fill="y")

        # Area Konten Aplikasi
        self.content_area = tk.Frame(self.main_frame, bg="#1e1e2e")
        self.content_area.pack(fill="both", expand=True)

        # Event Dragging Jendela
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)
        self.title_lbl.bind("<Button-1>", self.start_move)
        self.title_lbl.bind("<B1-Motion>", self.do_move)

        # Status Maximize
        self.is_maximized = False
        self.normal_geometry = f"{width}x{height}+{x}+{y}"

        # Daftarkan ke Taskbar
        if hasattr(parent, "taskbar") and parent.taskbar:
            parent.taskbar.add_task(self, title)

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        if not self.is_maximized:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.winfo_x() + deltax
            y = self.winfo_y() + deltay
            self.geometry(f"+{x}+{y}")

    def toggle_maximize(self):
        if not self.is_maximized:
            self.normal_geometry = self.geometry()
            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight() - 40  # Kurangi tinggi taskbar
            self.geometry(f"{screen_w}x{screen_h}+0+0")
            self.is_maximized = True
        else:
            self.geometry(self.normal_geometry)
            self.is_maximized = False

    def minimize_window(self):
        self.withdraw()

    def close_window(self):
        if hasattr(self.parent_desktop, "taskbar") and self.parent_desktop.taskbar:
            self.parent_desktop.taskbar.remove_task(self)
        self.destroy()

