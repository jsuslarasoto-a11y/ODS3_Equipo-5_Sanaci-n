import tkinter as tk
from tkinter import ttk
from datetime import datetime

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Hoy")
    win.geometry("800x500")
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    ahora = datetime.now()
    saludo = "Buenos días" if ahora.hour < 12 else "Buenas tardes" if ahora.hour < 20 else "Buenas noches"

    ttk.Label(frm, text=f"{saludo}, Ana María López", font=("Segoe UI", 28, "bold")).pack(pady=(0, 16))
    ttk.Label(frm, text=f"Hoy es {DIAS[ahora.weekday()]} {ahora.day} de {MESES[ahora.month - 1]} de {ahora.year}",
              font=("Segoe UI", 18, "bold")).pack(pady=(0, 8))
    ttk.Label(frm, text=f"Son las {ahora:%H:%M}", font=("Segoe UI", 18, "bold")).pack(pady=(0, 16))
    ttk.Button(frm, text="Cerrar", style="Menu.TButton", command=win.destroy).pack(fill="x", pady=8)