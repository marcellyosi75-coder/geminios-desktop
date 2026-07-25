import tkinter as tk

class DesktopIcon(tk.Frame):
    def __init__(self, parent, name, icon_symbol, command):
        super().__init__(parent, bg="#1e1e2e", cursor="hand2", padx=5, pady=5)
        self.command = command

        # Simbol Ikon
        self.lbl_icon = tk.Label(self, text=icon_symbol, font=("Segoe UI Emoji", 22), bg="#1e1e2e", fg="#cdd6f4")
        self.lbl_icon.pack()

        # Nama Aplikasi
        self.lbl_name = tk.Label(
            self, text=name, font=("Helvetica", 8), 
            bg="#1e1e2e", fg="#cdd6f4", wraplength=70, justify="center"
        )
        self.lbl_name.pack()

        # Event Binding (Double Click untuk Membuka)
        for widget in (self, self.lbl_icon, self.lbl_name):
            widget.bind("<Double-Button-1>", lambda e: self.command())
            widget.bind("<Enter>", lambda e: self.config(bg="#313244"))
            widget.bind("<Leave>", lambda e: self.config(bg="#1e1e2e"))

class DesktopGrid(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#1e1e2e")
        self.pack(fill="both", expand=True, padx=15, pady=15)
        
        self.col_count = 0
        self.row_count = 0

    def add_icon(self, name, icon_symbol, command):
        icon = DesktopIcon(self, name, icon_symbol, command)
        icon.grid(row=self.row_count, column=self.col_count, padx=15, pady=15, sticky="nw")
        
        # Susun otomatis ke bawah (grid vertikal)
        self.row_count += 1
        if self.row_count > 4:  # Jika sudah 5 baris, pindah ke kolom baru
            self.row_count = 0
            self.col_count += 1

