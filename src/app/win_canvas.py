import math
import time
import tkinter as tk
from tkinter import ttk


def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Reloj")
    win.geometry("500x620")
    win.configure(bg="black")

    canvas = tk.Canvas(
        win,
        width=340,
        height=340,
        background="black",
        highlightthickness=0,
    )
    canvas.pack(pady=(15, 5))

    center_x = center_y = 170
    radius = 145
    canvas.create_oval(
        center_x - radius,
        center_y - radius,
        center_x + radius,
        center_y + radius,
        outline="white",
        width=3,
    )

    for number in range(1, 13):
        angle = math.radians(number * 30 - 90)
        x = center_x + math.cos(angle) * (radius - 25)
        y = center_y + math.sin(angle) * (radius - 25)
        canvas.create_text(x, y, text=str(number), fill="white", font=("Segoe UI", 14, "bold"))

    for tick in range(60):
        angle = math.radians(tick * 6 - 90)
        outer_radius = radius - 5
        inner_radius = radius - (18 if tick % 5 == 0 else 10)
        canvas.create_line(
            center_x + math.cos(angle) * inner_radius,
            center_y + math.sin(angle) * inner_radius,
            center_x + math.cos(angle) * outer_radius,
            center_y + math.sin(angle) * outer_radius,
            fill="white",
            width=2 if tick % 5 == 0 else 1,
        )

    hour_hand = canvas.create_line(0, 0, 0, 0, fill="white", width=6, capstyle=tk.ROUND)
    minute_hand = canvas.create_line(0, 0, 0, 0, fill="white", width=4, capstyle=tk.ROUND)
    second_hand = canvas.create_line(0, 0, 0, 0, fill="red", width=2, capstyle=tk.ROUND)
    canvas.create_oval(
        center_x - 5,
        center_y - 5,
        center_x + 5,
        center_y + 5,
        fill="red",
        outline="red",
    )

    etiqueta = tk.Label(
        win,
        font=("Helvetica", 32, "bold"),
        background="black",
        foreground="white",
    )
    etiqueta.pack(pady=5)

    def actualizar_reloj():
        ahora = time.localtime()
        etiqueta.config(text=time.strftime("%H:%M:%S", ahora))

        segundos = ahora.tm_sec
        minutos = ahora.tm_min + segundos / 60
        horas = (ahora.tm_hour % 12) + minutos / 60

        for hand, angle, hand_length in (
            (hour_hand, horas * 30 - 90, 75),
            (minute_hand, minutos * 6 - 90, 105),
            (second_hand, segundos * 6 - 90, 120),
        ):
            radians = math.radians(angle)
            canvas.coords(
                hand,
                center_x,
                center_y,
                center_x + math.cos(radians) * hand_length,
                center_y + math.sin(radians) * hand_length,
            )

        win.after(1000, actualizar_reloj)

    actualizar_reloj()

    estilo = ttk.Style(win)
    estilo.configure(
        "Grande.TButton",
        font=("Segoe UI", 30, "bold"),
        padding=(40, 40),  # espacio interno: horizontal, vertical
    )

    ttk.Button(
        win,
        text="X",
        command=win.destroy,
        style="Grande.TButton",
    ).pack(pady=8)

    return win
