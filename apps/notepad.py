from window import AppWindow
import tkinter as tk

class Notepad(AppWindow):
    def __init__(self, master):
        super().__init__(master, "Notepad", 700, 500)
        
        self.text_area = tk.Text(
            self.body, bg="#1e1e1e", fg="white", insertbackground="white", 
            bd=0, font=("Consolas", 10), padx=5, pady=5
        )
        self.text_area.pack(fill="both", expand=True)

        # Context Menu Khusus Teks Editor
        self.edit_menu = tk.Menu(
            self, tearoff=0, bg="#303030", fg="white", 
            activebackground="#007acc", activeforeground="white", bd=1
        )
        self.edit_menu.add_command(label=" Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label=" Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label=" Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label=" Select All", command=self.select_all)

        # Bind Klik Kanan di dalam Text Area
        self.text_area.bind("<Button-3>", lambda e: self.edit_menu.tk_popup(e.x_root, e.y_root))

    def select_all(self):
        self.text_area.tag_add("sel", "1.0", "end")

