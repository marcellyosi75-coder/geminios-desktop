import tkinter as tk
from taskbar import Taskbar
from startmenu import StartMenu
from apps.notepad import Notepad
from apps.explorer import Explorer
from apps.settings import Settings

class Desktop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Desktop")
        
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+0+0")
        self.overrideredirect(True)
        self.configure(bg="#1d3557")
        self.update_idletasks()

        # 1. Start Menu & Taskbar
        self.menu = StartMenu(self)
        self.taskbar = Taskbar(self)
        self.taskbar.pack(side="bottom", fill="x")

        # 2. Area Desktop
        self.desktop = tk.Frame(self, bg="#1d3557", highlightthickness=0, bd=0)
        self.desktop.pack(side="top", fill="both", expand=True)

        # 3. Context Menu Desktop (Klik Kanan)
        self.context_menu = tk.Menu(
            self, tearoff=0, bg="#303030", fg="white", 
            activebackground="#007acc", activeforeground="white", bd=1
        )
        self.context_menu.add_command(label=" Refresh", command=self.refresh_desktop)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=" Buka Notepad", command=lambda: Notepad(self))
        self.context_menu.add_command(label=" Buka Explorer", command=lambda: Explorer(self))
        self.context_menu.add_command(label=" Pengaturan", command=lambda: Settings(self))
        self.context_menu.add_separator()
        self.context_menu.add_command(label=" Keluar / Shutdown", command=self.destroy)

        # Event Binding
        self.desktop.bind("<Button-1>", self.close_menu)
        self.desktop.bind("<Button-3>", self.show_context_menu)  # Trigger Klik Kanan
        self.bind("<Escape>", lambda e: self.destroy())

    def show_context_menu(self, event):
        if self.menu.visible:
            self.menu.toggle()
        # Pop-up menu sesuai koordinat kursor mouse
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def refresh_desktop(self):
        self.desktop.config(bg="#1d3557")
        self.update()

    def close_menu(self, event=None):
        if self.menu.visible:
            self.menu.toggle()
