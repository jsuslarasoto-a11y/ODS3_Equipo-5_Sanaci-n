import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# archivo donde se guardan los recordatorios
# parents[2] es la raiz del repo, asi que queda en <repo>/data/recordatorios.txt
RUTA_RECORDATORIOS = Path(__file__).resolve().parents[2] / "data" / "recordatorios.txt"


def open_win_list(parent: tk.Tk):
    # creamos la ventana secundaria encima del menu principal
    win = tk.Toplevel(parent)
    win.title("Recordatorios")
    win.geometry("800x750")

    # estilos con letra grande para que el paciente pueda leer facil
    estilo = ttk.Style(win)
    estilo.configure("Lista.TLabel", font=("Segoe UI", 18, "bold"))
    estilo.configure("Lista.TButton", font=("Segoe UI", 18, "bold"), padding=(10, 12))

    # marco principal donde van todos los elementos
    frm = ttk.Frame(win, padding=20)
    frm.pack(fill="both", expand=True)

    # titulo de la ventana
    ttk.Label(frm, text="Recordatorios", font=("Segoe UI", 32, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # lista de recordatorios (lado izquierdo)
    lb = tk.Listbox(frm, height=10, font=("Segoe UI", 18))
    lb.grid(row=1, column=0, rowspan=6, sticky="nsew", padx=(0, 15))
    # esto hace que la lista crezca si se agranda la ventana
    frm.columnconfigure(0, weight=1)
    frm.rowconfigure(6, weight=1)

    # entradas para la hora y el texto (lado derecho)
    ttk.Label(frm, text="Hora (HH:MM):", style="Lista.TLabel").grid(row=1, column=1, sticky="w")
    ent_hora = ttk.Entry(frm, width=10, font=("Segoe UI", 16))
    ent_hora.grid(row=2, column=1, sticky="w", pady=(0, 10))

    ttk.Label(frm, text="Recordatorio:", style="Lista.TLabel").grid(row=3, column=1, sticky="w")
    ent_texto = ttk.Entry(frm, width=20, font=("Segoe UI", 16))
    ent_texto.grid(row=4, column=1, sticky="ew", pady=(0, 10))

    # escribe todo lo que hay en la lista al archivo, un recordatorio por linea
    # se llama cada vez que la lista cambia para no perder nada
    def guardar_archivo():
        with open(RUTA_RECORDATORIOS, "w", encoding="utf-8") as f:
            for item in lb.get(0, "end"):
                f.write(item + "\n")

    # cargamos los recordatorios que ya estaban guardados
    if RUTA_RECORDATORIOS.exists():
        with open(RUTA_RECORDATORIOS, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():  # nos saltamos las lineas vacias
                    lb.insert("end", linea.strip())

    # funcion del boton Agregar: valida la hora y agrega el recordatorio a la lista
    def agregar():
        hora = ent_hora.get().strip()
        texto = ent_texto.get().strip()

        # el texto es obligatorio
        if not texto:
            messagebox.showwarning("Aviso", "Escribe un recordatorio para agregar.")
            return
        # la hora es opcional, pero si la escriben revisamos que sea valida
        if hora:
            partes = hora.split(":")  # "08:30" -> ["08", "30"]
            if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit() \
                    or int(partes[0]) > 23 or int(partes[1]) > 59:
                messagebox.showerror("Error", "La hora debe tener el formato HH:MM, por ejemplo 08:30.")
                return
            lb.insert("end", f"{hora} - {texto}")
        else:
            lb.insert("end", texto)

        # limpiamos las cajas de texto y guardamos el cambio
        ent_hora.delete(0, "end")
        ent_texto.delete(0, "end")
        guardar_archivo()

    # funcion del boton Eliminar: borra el recordatorio seleccionado
    def eliminar():
        sel = lb.curselection()  # regresa la posicion seleccionada en la lista
        if sel:
            lb.delete(sel[0])
            guardar_archivo()
        else:
            messagebox.showwarning("Aviso", "Selecciona un recordatorio de la lista.")

    # funcion del boton Borrar todo: pregunta antes de vaciar la lista
    def limpiar():
        if messagebox.askyesno("Confirmar", "¿Borrar todos los recordatorios?"):
            lb.delete(0, "end")
            guardar_archivo()

    # botones de acciones, uno debajo del otro
    botones = ttk.Frame(frm)
    botones.grid(row=5, column=1, sticky="ew")
    ttk.Button(botones, text="Agregar", style="Lista.TButton", command=agregar).pack(fill="x", pady=5)
    ttk.Button(botones, text="Eliminar", style="Lista.TButton", command=eliminar).pack(fill="x", pady=5)
    ttk.Button(botones, text="Borrar todo", style="Lista.TButton", command=limpiar).pack(fill="x", pady=5)

    # boton X para cerrar la ventana
    ttk.Button(frm, text="X", style="Lista.TButton", command=win.destroy)\
        .grid(row=7, column=0, columnspan=2, pady=20)

    return win
