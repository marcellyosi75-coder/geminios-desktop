import tkinter as tk
from apps.notepad import Notepad
from apps.explorer import Explorer
from apps.settings import Settings

class StartMenu:
    def __init__(self, master):
        self.master = master
        self.visible = False
        self.frame = tk.Frame(master, width=220, height=300, bg="#303030")
        self.frame.pack_propagate(False)

        # Tombol Aplikasi
        tk.Button(self.frame, text="Notepad", bg="#404040", fg="white", anchor="w",
                  command=lambda: [Notepad(master), self.toggle()]).pack(fill="x", padx=5, pady=2)
        tk.Button(self.frame, text="Explorer", bg="#404040", fg="white", anchor="w",
                  command=lambda: [Explorer(master), self.toggle()]).pack(fill="x", padx=5, pady=2)
        tk.Button(self.frame, text="Settings", bg="#404040", fg="white", anchor="w",
                  command=lambda: [Settings(master), self.toggle()]).pack(fill="x", padx=5, pady=2)

    def toggle(self):
        if self.visible:
            self.frame.place_forget()
            self.visible = False
        else:
            # Gunakan winfo_screenheight() agar akurat mengambil tinggi layar total
            screen_h = self.master.winfo_screenheight()
            taskbar_h = 42
            menu_h = 300

            y_pos = screen_h - taskbar_h - menu_h
            self.frame.place(x=0, y=y_pos, width=220, height=menu_h)
            self.frame.lift()  # Paksa berada di lapisan paling atas
            self.visible = True
