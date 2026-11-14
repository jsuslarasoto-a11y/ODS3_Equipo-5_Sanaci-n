import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    root = tk.Tk()
    root.title("Proyecto Integrador - MEDAR -MVP")
    root.geometry("1080x1080")

    frame = ttk.Frame(root, padding=(40, 20, 20, 20))
    frame.pack(fill="both", expand=True)

    style = ttk.Style(root)
    style.configure("Menu.TButton", font=("Segoe UI", 20, "bold"))

    ttk.Label(frame, text="Memoria", font=("Segoe UI", 40, "bold")).pack(pady=(0, 15))
    ttk.Button(frame, text="1) Hoy", style="Menu.TButton", command=lambda: open_win_home(root)).pack(pady=15, fill="x")
    ttk.Button(frame, text="2) Mis datos", style="Menu.TButton", command=lambda: open_win_form(root)).pack(pady=15, fill="x")
    ttk.Button(frame, text="3) Recordatorios", style="Menu.TButton", command=lambda: open_win_list(root)).pack(pady=15, fill="x")
    ttk.Button(frame, text="4) Medicinas", style="Menu.TButton", command=lambda: open_win_table(root)).pack(pady=15, fill="x")
    ttk.Button(frame, text="5) Reloj", style="Menu.TButton", command=lambda: open_win_canvas(root)).pack(pady=15, fill="x")
    ttk.Separator(frame).pack(pady=22, fill="x")
    ttk.Button(frame, text="X",style="Menu.TButton", command=root.destroy).pack(pady=22)

    root.mainloop()

if __name__ == "__main__":
    main()
