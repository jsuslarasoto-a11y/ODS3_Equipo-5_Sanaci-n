import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

# archivo donde se guardan los datos del paciente
# parents[2] es la raiz del repo, asi que queda en <repo>/data/mis_datos.txt
RUTA_DATOS = Path(__file__).resolve().parents[2] / "data" / "mis_datos.txt"


def open_win_form(parent: tk.Tk):
    # creamos la ventana secundaria encima del menu principal
    win = tk.Toplevel(parent)
    win.title("Mis datos")
    win.geometry("700x520")

    # estilos con letra grande para que el paciente pueda leer facil
    estilo = ttk.Style(win)
    estilo.configure("Datos.TLabel", font=("Segoe UI", 18, "bold"))
    estilo.configure("Datos.TButton", font=("Segoe UI", 20, "bold"), padding=(20, 15))

    # marco principal donde van todos los elementos
    frm = ttk.Frame(win, padding=20)
    frm.pack(fill="both", expand=True)

    # titulo de la ventana
    ttk.Label(frm, text="Mis datos", font=("Segoe UI", 32, "bold")).grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # campos del formulario
    campos = ["Nombre", "Edad", "Domicilio", "Contacto de emergencia", "Teléfono del contacto"]
    entradas = {}  # aqui guardamos cada caja de texto con el nombre de su campo

    # con un for creamos una etiqueta y una caja de texto por cada campo
    fila = 1
    for campo in campos:
        ttk.Label(frm, text=campo + ":", style="Datos.TLabel").grid(row=fila, column=0, sticky="w", pady=8)
        ent = ttk.Entry(frm, width=25, font=("Segoe UI", 16))
        ent.grid(row=fila, column=1, sticky="w", pady=8, padx=10)
        entradas[campo] = ent
        fila += 1  # pasamos a la siguiente fila

    # si ya hay datos guardados los cargamos para que el paciente los vea
    if RUTA_DATOS.exists():
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            for linea in f:
                # cada linea tiene el formato "Campo: valor"
                if ":" in linea:
                    campo, valor = linea.split(":", 1)
                    if campo in entradas:
                        entradas[campo].insert(0, valor.strip())

    # funcion del boton Guardar: revisa los datos y los escribe en el archivo
    def guardar():
        # leemos lo que escribio el usuario (strip quita espacios de sobra)
        nombre = entradas["Nombre"].get().strip()
        edad = entradas["Edad"].get().strip()
        telefono = entradas["Teléfono del contacto"].get().strip()

        # validaciones: si algo esta mal mostramos un error y no guardamos
        if not nombre:
            messagebox.showerror("Error", "El nombre es requerido.")
            return
        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return
        if telefono and not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono solo debe tener números.")
            return

        # escribimos cada campo en una linea del archivo
        with open(RUTA_DATOS, "w", encoding="utf-8") as f:
            for campo in campos:
                f.write(f"{campo}: {entradas[campo].get().strip()}\n")
        messagebox.showinfo("OK", "Datos guardados.")

    # botones de abajo: Guardar y X para cerrar la ventana
    ttk.Button(frm, text="Guardar", style="Datos.TButton", command=guardar)\
        .grid(row=fila, column=0, pady=30)
    ttk.Button(frm, text="X", style="Datos.TButton", command=win.destroy)\
        .grid(row=fila, column=1, pady=30)

    return win
