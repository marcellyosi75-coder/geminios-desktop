import tkinter as tk
import time
import calendar
from datetime import datetime

try:
    import psutil
except ImportError:
    psutil = None

class CalendarPopup(tk.Toplevel):
    def __init__(self, parent, x, y):
        super().__init__(parent)
        self.overrideredirect(True)
        self.configure(bg="#1e1e2e")
        
        # Posisi popup melayang di atas jam taskbar
        width, height = 240, 220
        self.geometry(f"{width}x{height}+{x - width}+{y - height - 10}")

        # Container Utama
        frame = tk.Frame(self, bg="#1e1e2e", highlightbackground="#45475a", highlightthickness=1, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        now = datetime.now()
        lbl_month = tk.Label(
            frame, text=now.strftime("%B %Y"), 
            font=("Helvetica", 11, "bold"), fg="#89b4fa", bg="#1e1e2e"
        )
        lbl_month.pack(pady=(0, 8))

        # Tabel Kalender
        cal_frame = tk.Frame(frame, bg="#1e1e2e")
        cal_frame.pack(fill="both", expand=True)

        days = ["Min", "Sen", "Sel", "Rab", "Kam", "Jum", "Sab"]
        for idx, day in enumerate(days):
            lbl = tk.Label(cal_frame, text=day, font=("Helvetica", 8, "bold"), fg="#a6adc8", bg="#1e1e2e")
            lbl.grid(row=0, column=idx, padx=2, pady=2)

        month_cal = calendar.monthcalendar(now.year, now.month)
        for r_idx, week in enumerate(month_cal):
            for c_idx, day in enumerate(week):
                if day != 0:
                    is_today = (day == now.day)
                    btn_bg = "#89b4fa" if is_today else "#1e1e2e"
                    btn_fg = "#11111b" if is_today else "#cdd6f4"
                    lbl_day = tk.Label(
                        cal_frame, text=str(day), font=("Helvetica", 8, "bold" if is_today else "normal"),
                        fg=btn_fg, bg=btn_bg, width=3
                    )
                    lbl_day.grid(row=r_idx + 1, column=c_idx, padx=1, pady=1)

        # Otomatis tutup jika klik di luar
        self.bind("<FocusOut>", lambda e: self.destroy())
        self.focus_set()


class SystemTray(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#11111b")
        
        # Indikator Memori RAM
        self.lbl_ram = tk.Label(self, text="RAM: --%", font=("Helvetica", 8), fg="#a6adc8", bg="#11111b")
        self.lbl_ram.pack(side="left", padx=6)

        # Separator
        tk.Label(self, text="|", fg="#45475a", bg="#11111b").pack(side="left")

        # Jam System
        self.lbl_clock = tk.Label(
            self, text="00:00:00", font=("Helvetica", 9, "bold"), 
            fg="#cdd6f4", bg="#11111b", cursor="hand2"
        )
        self.lbl_clock.pack(side="left", padx=8)
        self.lbl_clock.bind("<Button-1>", self.toggle_calendar)

        self.cal_popup = None
        self.update_stats()

    def update_stats(self):
        # Update Jam
        now_str = time.strftime("%H:%M:%S")
        self.lbl_clock.config(text=now_str)

        # Update RAM (jika library psutil terpasang)
        if psutil:
            ram_permil = psutil.virtual_memory().percent
            self.lbl_ram.config(text=f"RAM: {ram_permil:.0f}%")

        # Refresh setiap 1 detik
        self.after(1000, self.update_stats)

    def toggle_calendar(self, event):
        if self.cal_popup and self.cal_popup.winfo_exists():
            self.cal_popup.destroy()
            self.cal_popup = None
        else:
            x = self.winfo_rootx() + self.winfo_width()
            y = self.winfo_rooty()
            self.cal_popup = CalendarPopup(self, x, y)

