import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from pathlib import Path


def _create_database(db_path: Path):
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            """
           Haz una tabla si no existe medicinas (
                medicina en texto no vacio ,
                dosis en texto no vacio ,
                horario en texto no vacio)
            """
        )


def _load_medicines(db_path: Path):
    with sqlite3.connect(db_path) as connection:
        return connection.execute(
            "Seccione medicina, dosis, horario de medicinas ordenadas por id"
        ).fetchall()


def _save_medicine(db_path: Path, medicina: str, dosis: str, horario: str):
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            "Inserte en medicinas (medicina, dosis, horario) los nuevos valores (?, ?, ?)",
            (medicina, dosis, horario),
        )


def open_win_table(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Tabla (Treeview)")
    win.geometry("600x600")
    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    form = ttk.Frame(frm)
    form.pack(fill="x", pady=(0, 12))

    fields = (
        ("Medicina", "medicina"),
        ("Dosis", "dosis"),
        ("Horario", "horario"),
    )
    entries = {}
    for column, (label, key) in enumerate(fields):
        ttk.Label(form, text=label).grid(row=0, column=column, sticky="w", padx=4)
        entry = ttk.Entry(form)
        entry.grid(row=1, column=column, sticky="ew", padx=4)
        entries[key] = entry
        form.columnconfigure(column, weight=1)

    cols = ("Medicina", "Dosis", "Horario")
    tv = ttk.Treeview(frm, columns=cols, show="headings", height=20)
    for c in cols:
        tv.heading(c, text=c.capitalize())
        tv.column(c, width=120, anchor="center")
    tv.pack(fill="both", expand=True)

    db_path = Path(__file__).resolve().parents[2] / "data" / "medicinas.db"
    try:
        _create_database(db_path)
        for row in _load_medicines(db_path):
            tv.insert("", "end", values=row)
    except (OSError, sqlite3.Error) as error:
        messagebox.showerror(
            "Error",
            f"No se pudo abrir la base de datos:\n{error}",
            parent=win,
        )
        return

    def add_medicine():
        values = {key: entries[key].get().strip() for _, key in fields}
        if not all(values.values()):
            messagebox.showwarning(
                "Aviso",
                "Completa los campos de medicina, dosis y horario.",
                parent=win,
            )
            return

        try:
            _save_medicine(
                db_path,
                values["medicina"],
                values["dosis"],
                values["horario"],
            )
        except sqlite3.Error as error:
            messagebox.showerror(
                "Error",
                f"No se pudo guardar la medicina:\n{error}",
                parent=win,
            )
            return

        tv.insert(
            "",
            "end",
            values=(values["medicina"], values["dosis"], values["horario"]),
        )
        for entry in entries.values():
            entry.delete(0, "end")

    ttk.Button(form, text="Agregar", command=add_medicine).grid(
        row=1, column=len(fields), padx=4, sticky="ew"
    )
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor="e")
