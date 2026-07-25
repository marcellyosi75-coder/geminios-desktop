import tkinter as tk

class AppWindow(tk.Toplevel):
    def __init__(self, master, title="Application", width=600, height=400):
        super().__init__(master)
        self.geometry(f"{width}x{height}+150+120")
        self.title(title)
        self.overrideredirect(True)
        
        self.dragx = 0
        self.dragy = 0
        self.is_maximized = False
        self.normal_geometry = f"{width}x{height}+150+120"

        # Context Menu Window (Titlebar)
        self.win_context_menu = tk.Menu(
            self, tearoff=0, bg="#303030", fg="white", 
            activebackground="#007acc", activeforeground="white", bd=1
        )
        self.win_context_menu.add_command(label=" Minimize", command=self.minimize)
        self.win_context_menu.add_command(label=" Maximize / Restore", command=self.toggle_maximize)
        self.win_context_menu.add_separator()
        self.win_context_menu.add_command(label=" Tutup", command=self.destroy)

        # Titlebar Custom
        self.titlebar = tk.Frame(self, bg="#2b2b2b", height=30)
        self.titlebar.pack(fill="x")
        self.titlebar.pack_propagate(False)

        self.label = tk.Label(self.titlebar, text=title, bg="#2b2b2b", fg="white", font=("Arial", 9, "bold"))
        self.label.pack(side="left", padx=10)

        # Control Buttons
        close_btn = tk.Button(self.titlebar, text="✕", bg="#e63946", fg="white", bd=0, relief="flat", command=self.destroy)
        close_btn.pack(side="right", fill="y", ipadx=12)

        self.max_btn = tk.Button(self.titlebar, text="□", bg="#2b2b2b", fg="white", bd=0, relief="flat", command=self.toggle_maximize)
        self.max_btn.pack(side="right", fill="y", ipadx=12)

        min_btn = tk.Button(self.titlebar, text="—", bg="#2b2b2b", fg="white", bd=0, relief="flat", command=self.minimize)
        min_btn.pack(side="right", fill="y", ipadx=12)

        # Body Window
        self.body = tk.Frame(self, bg="#202020")
        self.body.pack(fill="both", expand=True)

        # Bind Klik Kanan (<Button-3>) di Titlebar
        self.titlebar.bind("<Button-3>", self.show_win_context_menu)
        self.label.bind("<Button-3>", self.show_win_context_menu)

        # Drag Event
        self.titlebar.bind("<Button-1>", self.start_move)
        self.titlebar.bind("<B1-Motion>", self.move)
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.move)

        if hasattr(self.master, 'taskbar'):
            self.master.taskbar.add_app(self)

    def show_win_context_menu(self, event):
        self.win_context_menu.tk_popup(event.x_root, event.y_root)

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
        self.withdraw()

    def toggle_maximize(self):
        if not self.is_maximized:
            self.normal_geometry = self.geometry()
            screen_w = self.winfo_screenwidth()
            screen_h = self.winfo_screenheight()
            taskbar_h = 42
            
            self.geometry(f"{screen_w}x{screen_h - taskbar_h}+0+0")
            self.is_maximized = True
            self.max_btn.config(text="❐")
        else:
            self.geometry(self.normal_geometry)
            self.is_maximized = False
            self.max_btn.config(text="□")

    def destroy(self):
        if hasattr(self.master, 'taskbar'):
            self.master.taskbar.remove_app(self)
        super().destroy()
