# App Paciente (Flet)

Versión sencilla de la app para el **paciente** del Proyecto Sanación (ODS 3), hecha con [Flet](https://flet.dev) 1.1.2.

## Pantallas

| Pantalla | Qué muestra |
|---|---|
| Inicio | Saludo y menú de cuadros grandes con ícono |
| ¿Quién soy? | Nombre, edad y dónde vive el paciente |
| Mi día | Día, fecha y hora (se actualiza sola, formato a.m./p.m.) |
| Mi familia | *(pendiente: fotos de la familia)* |
| Mis pastillas | *(pendiente: lista de medicinas)* |
| Necesito ayuda | Nombre y teléfono del cuidador |

## Cómo correrla (Windows / PowerShell)

Requisitos: **Python 3.13** y **VS Code** con la extensión Python.

```powershell
# Solo la primera vez: permitir activar entornos virtuales
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

# Entrar a la carpeta de la app
cd src\app_paciente

# Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar Flet 1.1.2
pip install -r requirements.txt

# Correr la app (se recarga sola al guardar)
flet run -d main.py
```

En VS Code, elige el intérprete `.venv` (`Ctrl + Shift + P` → **Python: Select Interpreter**) para que el botón ▶ funcione.

En Mac, el comando para activar es `source .venv/bin/activate`.

## Notas

- Los datos del paciente y del cuidador (María López, Ana López) son de ejemplo.
- Usa la sintaxis de **Flet 1.0+** (`ft.run`, `ft.Button`). Código de tutoriales viejos con `ft.app` o `ElevatedButton` no funciona.
