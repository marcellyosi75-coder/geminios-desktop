from window import AppWindow
import tkinter as tk
import os

class Explorer(AppWindow):

    def __init__(self, master):
        super().__init__(master, "Explorer")

        self.list = tk.Listbox(self.body)
        self.list.pack(fill="both", expand=True)

        for i in os.listdir("."):
            self.list.insert("end", i)
