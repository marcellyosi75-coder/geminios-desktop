import tkinter as tk

class AppWindow(tk.Toplevel):
    def __init__(self, master, title="Application", width=600, height=400):
        super().__init__(master)
        self.geometry(f"{width}x{height}+150+120")
        self.title(title)
        
        # Sembunyikan border bawaan window manager X11
        self.overrideredirect(True)
        
        self.dragx = 0
        self.dragy = 0
        self.is_maximized = False
        self.normal_geometry = f"{width}x{height}+150+120"

        # Titlebar Custom
        self.titlebar = tk.Frame(self, bg="#2b2b2b", height=30)
        self.titlebar.pack(fill="x")
        self.titlebar.pack_propagate(False)

        self.label = tk.Label(self.titlebar, text=title, bg="#2b2b2b", fg="white", font=("Arial", 9, "bold"))
        self.label.pack(side="left", padx=10)

        # Tombol Kontrol (Close, Maximize, Minimize) diatur dari kanan ke kiri
        close_btn = tk.Button(self.titlebar, text="✕", bg="#e63946", fg="white", bd=0, relief="flat", command=self.destroy)
        close_btn.pack(side="right", fill="y", ipadx=8)
        close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#ff4d4d"))
        close_btn.bind("<Leave>", lambda e: close_btn.config(bg="#e63946"))

        self.max_btn = tk.Button(self.titlebar, text="🗖", bg="#2b2b2b", fg="white", bd=0, relief="flat", command=self.toggle_maximize)
        self.max_btn.pack(side="right", fill="y", ipadx=8)
        self.max_btn.bind("<Enter>", lambda e: self.max_btn.config(bg="#3a3a3a"))
        self.max_btn.bind("<Leave>", lambda e: self.max_btn.config(bg="#2b2b2b"))

        min_btn = tk.Button(self.titlebar, text="—", bg="#2b2b2b", fg="white", bd=0, relief="flat", command=self.minimize)
        min_btn.pack(side="right", fill="y", ipadx=8)
        min_btn.bind("<Enter>", lambda e: min_btn.config(bg="#3a3a3a"))
        min_btn.bind("<Leave>", lambda e: min_btn.config(bg="#2b2b2b"))

        # Body Window
        self.body = tk.Frame(self, bg="#202020")
        self.body.pack(fill="both", expand=True)

        # Drag Window Event (Hanya bisa digeser jika tidak sedang maximize)
        self.titlebar.bind("<Button-1>", self.start_move)
        self.titlebar.bind("<B1-Motion>", self.move)
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.move)

    def start_move(self, event):
        if not self.is_maximized:
            self.dragx = event.x
            self.dragy = event.y

    def move(self, event):
        if not self.is_maximized:
            x = self.winfo_x() + event.x - self.dragx
            y = self.winfo_y() + event.y - self.dragy
            self.geometry(f"+{x}+{y}")

    def minimize(self):
        # Menyembunyikan jendela (bisa dikembangkan nanti agar masuk ke taskbar)
        self.withdraw()

    def toggle_maximize(self):
        if not self.is_maximized:
            # Simpan ukuran normal sebelum maximize
            self.normal_geometry = self.geometry()
            
            # Ambil ukuran layar penuh dikurangi taskbar (42px)
            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight()
            taskbar_h = 42
            
            self.geometry(f"{screen_w}x{screen_h - taskbar_h}+0+0")
            self.is_maximized = True
            self.max_btn.config(text="🗗") # Ubah ikon menjadi restore
        else:
            # Kembalikan ke ukuran semula
            self.geometry(self.normal_geometry)
            self.is_maximized = False
            self.max_btn.config(text="🗖") # Kembalikan ikon maximize

