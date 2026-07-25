import tkinter as tk
from apps.notepad import Notepad
from apps.file_explorer import FileExplorer
from apps.settings import Settings
from apps.task_manager import TaskManager

class StartMenu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#11111b", highlightbackground="#45475a", highlightthickness=1)
        self.desktop_parent = parent
        
        header_lbl = tk.Label(
            self, text="GeminiOS Apps", fg="#cdd6f4", bg="#11111b", 
            font=("Helvetica", 10, "bold")
        )
        header_lbl.pack(anchor="w", padx=15, pady=(15, 10))

        sep = tk.Frame(self, bg="#313244", height=1)
        sep.pack(fill="x", padx=10, pady=5)

        # Daftar Aplikasi di Menu Start
        apps_list = [
            ("📝 Notepad", self.open_notepad),
            ("📁 File Explorer", self.open_file_explorer),
            ("⚙️ Settings", self.open_settings),
            ("📊 Task Manager", self.open_task_manager),
        ]

        for name, cmd in apps_list:
            btn = tk.Button(
                self, text=name, fg="#cdd6f4", bg="#11111b", 
                activebackground="#313244", activeforeground="#ffffff",
                bd=0, anchor="w", padx=15, pady=8, cursor="hand2",
                font=("Helvetica", 9), command=cmd
            )
            btn.pack(fill="x", padx=5, pady=2)

    def open_notepad(self):
        Notepad(self.desktop_parent)
        self.destroy()

    def open_file_explorer(self):
        FileExplorer(self.desktop_parent)
        self.destroy()

    def open_settings(self):
        Settings(self.desktop_parent)
        self.destroy()

    def open_task_manager(self):
        TaskManager(self.desktop_parent)
        self.destroy()
