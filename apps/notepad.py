import tkinter as tk
from window import Window

class Notepad(Window):
    def __init__(self, parent):
        super().__init__(parent, title="Notepad", width=520, height=360, x=140, y=120)
        
        # Area Text Editor
        self.text_area = tk.Text(
            self.content_area, bg="#1e1e2e", fg="#cdd6f4", 
            insertbackground="#cdd6f4", font=("Consolas", 10), bd=0, highlightthickness=0
        )
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

# Alias
NotepadApp = Notepad
