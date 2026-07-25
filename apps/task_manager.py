import tkinter as tk
from window import Window
import os

class TaskManager(Window):
    def __init__(self, parent):
        super().__init__(parent, title="Task Manager", width=500, height=340, x=200, y=120)

        lbl = tk.Label(self.content_area, text="Active Processes (Termux)", fg="#cdd6f4", bg="#1e1e2e", font=("Helvetica", 11, "bold"))
        lbl.pack(anchor="w", padx=15, pady=10)

        # Listbox untuk menampilkan proses aktif
        list_frame = tk.Frame(self.content_area, bg="#1e1e2e")
        list_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.listbox = tk.Listbox(
            list_frame, bg="#11111b", fg="#a6e3a1", selectbackground="#313244",
            bd=0, highlightthickness=0, font=("Consolas", 9)
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.load_processes()

    def load_processes(self):
        try:
            self.listbox.delete(0, tk.END)
            # Mengambil daftar proses dasar menggunakan perintah sistem ps
            stream = os.popen("ps")
            for line in stream.readlines():
                self.listbox.insert(tk.END, line.strip())
        except Exception as e:
            self.listbox.insert(tk.END, f"Gagal memuat proses: {str(e)}")

