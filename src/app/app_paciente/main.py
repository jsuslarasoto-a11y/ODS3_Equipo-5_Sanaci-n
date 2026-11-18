# Importa la librería Flet y le pone el apodo "ft" para escribir menos
import flet as ft
# Herramienta de Python para saber la fecha y hora actuales
from datetime import datetime
# Herramienta de Python para hacer tareas en segundo plano (como un reloj)
import asyncio

# Nombres de los días (0 = lunes ... 6 = domingo)
DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Nombres de los meses (posición 0 = enero ... 11 = diciembre)
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# Función principal: Flet la llama al abrir la app y le pasa "page" (la pantalla)
def main(page: ft.Page):
    # Título que aparece en la barra de la ventana
    page.title = "APP PACIENTE"
    # Ancho de la ventana en píxeles (parecido a un celular)
    page.window.width = 390
    # Alto de la ventana en píxeles
    page.window.height = 844
    # Centra horizontalmente todo lo que se ponga en la pantalla
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- Fábrica de botones ---
    # Función que crea un botón rectangular; recibe el texto, el color y qué hacer al presionarlo
    def crear_boton(texto, color, al_presionar):
        # Regresa (entrega) el botón ya armado a quien llamó la función
        return ft.Button(
            # Lo que se ve dentro del botón: el texto en tamaño 24
            content=ft.Text(texto, size=24),
            # Tamaño del botón: 300 de ancho y 80 de alto
            width=300, height=80,
            # Color de fondo (el que le pasemos) y color del texto (blanco)
            bgcolor=color, color=ft.Colors.WHITE,
            # Función que se ejecuta cuando lo presionan
            on_click=al_presionar,
        )

    # --- Fábrica de cuadros con ícono ---
    # Crea un cuadro con ícono y texto; si no le das ancho y alto, mide 160 x 160
    def crear_cuadro(texto, icono, color, al_presionar, ancho=160, alto=160):
        # Regresa una caja (Container) que funciona como botón
        return ft.Container(
            # Lo que va dentro de la caja: una columna (cosas una debajo de otra)
            content=ft.Column(
                # Lista de lo que va en la columna
                [
                    # El dibujo (ícono) en tamaño 60 y color blanco
                    ft.Icon(icono, size=60, color=ft.Colors.WHITE),
                    # El texto debajo del ícono: tamaño 20, en negritas, blanco y centrado
                    ft.Text(texto, size=20, weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                ],
                # Centra el ícono y el texto a lo ancho del cuadro
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                # Centra el ícono y el texto a lo alto del cuadro
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            # Ancho del cuadro (160 si no se indica otro)
            width=ancho,
            # Alto del cuadro (160 si no se indica otro)
            height=alto,
            # Color de fondo del cuadro
            bgcolor=color,
            # Redondea las esquinas
            border_radius=20,
            # Efecto de "onda" al tocarlo, para que se note que sí se presionó
            ink=True,
            # Función que se ejecuta al tocar el cuadro
            on_click=al_presionar,
        )

    # --- Cambiar de pantalla ---
    # Recibe una lista de controles y los pone en la pantalla en lugar de los que había
    def mostrar(controles):
        # Borra todo lo que hay en la pantalla
        page.controls.clear()
        # Pone los controles nuevos
        page.controls.extend(controles)
        # Refresca la pantalla para que se vean los cambios
        page.update()

    # --- Pantalla del menú ---
    # Arma la pantalla principal con el saludo y los cuadros
    def pantalla_inicio():
        # Muestra esta lista de cosas en la pantalla
        mostrar([
            # Saludo grande en negritas
            ft.Text("Hola, María", size=36, weight=ft.FontWeight.BOLD),
            # Pregunta más pequeña en gris
            ft.Text("¿Qué quieres hacer?", size=22, color=ft.Colors.GREY_700),

            # Primera fila: dos cuadros lado a lado
            ft.Row(
                [
                    # Cuadro verde con ícono de persona; abre la pantalla "¿Quién soy?"
                    crear_cuadro("¿Quién soy?", ft.Icons.PERSON, ft.Colors.GREEN, quien_soy),
                    # Cuadro naranja con ícono de calendario; abre la pantalla "Mi día"
                    crear_cuadro("Mi día", ft.Icons.CALENDAR_TODAY, ft.Colors.ORANGE, mi_dia),
                ],
                # Centra la fila en la pantalla
                alignment=ft.MainAxisAlignment.CENTER,
                # Espacio de 15 píxeles entre los dos cuadros
                spacing=15,
            ),
            # Segunda fila: otros dos cuadros
            ft.Row(
                [
                    # Cuadro azul con ícono de familia; abre "Mi familia"
                    crear_cuadro("Mi familia", ft.Icons.FAMILY_RESTROOM, ft.Colors.BLUE, mi_familia),
                    # Cuadro morado con ícono de medicina; abre "Mis pastillas"
                    crear_cuadro("Mis pastillas", ft.Icons.MEDICATION, ft.Colors.PURPLE, mis_pastillas),
                ],
                # Centra la fila
                alignment=ft.MainAxisAlignment.CENTER,
                # Espacio entre los cuadros
                spacing=15,
            ),

            # Cuadro rojo de ayuda: más ancho (335 = 160 + 15 + 160) para alinearse con las filas
            crear_cuadro("Necesito ayuda", ft.Icons.SOS, ft.Colors.RED, necesito_ayuda,
                         ancho=335, alto=110),
        ])

    # Función para el botón "Volver": regresa a la pantalla principal
    def volver(e):
        # Vuelve a armar el menú
        pantalla_inicio()

    # --- Pantallas de cada botón ---
    # Pantalla con los datos del paciente
    def quien_soy(e):
        mostrar([
            # Título verde (mismo color que su cuadro)
            ft.Text("¿Quién soy?", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
            # Nombre del paciente
            ft.Text("Me llamo: María López", size=24),
            # Edad
            ft.Text("Tengo: 78 años", size=24),
            # Dónde vive
            ft.Text("Vivo en: León, Guanajuato", size=24),
            # Botón gris para regresar al menú
            crear_boton("⬅ Volver", ft.Colors.GREY, volver),
        ])

    # Pantalla con el contacto de emergencia
    def necesito_ayuda(e):
        mostrar([
            # Título rojo
            ft.Text("Necesito ayuda", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
            # Instrucción
            ft.Text("Llama a tu cuidador:", size=24),
            # Nombre del cuidador, grande y en negritas
            ft.Text("Ana López", size=30, weight=ft.FontWeight.BOLD),
            # Teléfono del cuidador
            ft.Text("📞 477 123 4567", size=30),
            # Botón para regresar al menú
            crear_boton("⬅ Volver", ft.Colors.GREY, volver),
        ])

    # Pantalla de la familia (después tendrá fotos)
    def mi_familia(e):
        mostrar([
            # Título azul
            ft.Text("Mi familia", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            # Texto de relleno mientras agregamos las fotos
            ft.Text("Aquí verás las fotos de tu familia.", size=22),
            # Botón para regresar al menú
            crear_boton("⬅ Volver", ft.Colors.GREY, volver),
        ])

    # Pantalla de medicinas (después tendrá la lista de pastillas)
    def mis_pastillas(e):
        mostrar([
            # Título morado
            ft.Text("Mis pastillas", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE),
            # Texto de relleno mientras agregamos la lista
            ft.Text("Aquí verás qué medicina te toca y a qué hora.", size=22),
            # Botón para regresar al menú
            crear_boton("⬅ Volver", ft.Colors.GREY, volver),
        ])

        # Pantalla con el día, la fecha y la hora (que se actualiza sola)
    # Pantalla con el día, la fecha y la hora (que se actualiza sola)
    def mi_dia(e):
        # Creamos los textos vacíos; los llenamos en actualizar()
        texto_dia = ft.Text(size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)
        texto_fecha = ft.Text(size=24, color=ft.Colors.BLACK)
        texto_hora = ft.Text(size=64, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK)

        # Lee la fecha y hora actuales y las pone en los textos
        def actualizar():
            ahora = datetime.now()
            texto_dia.value = f"Hoy es {DIAS[ahora.weekday()]}"
            texto_fecha.value = f"{ahora.day} de {MESES[ahora.month - 1]} de {ahora.year}"

            # Convierte la hora de 0-23 a formato de 12 horas
            hora12 = ahora.hour % 12
            # A las 12 (mediodía y medianoche) el residuo es 0, así que lo cambiamos a 12
            if hora12 == 0:
                hora12 = 12

            # Antes de las 12 es a.m.; desde las 12 es p.m.
            if ahora.hour < 12:
                texto_hora.value = f"{hora12}:{ahora.minute:02d} a.m."
            else:
                texto_hora.value = f"{hora12}:{ahora.minute:02d} p.m."

        # Tarjeta naranja clarita con los tres textos
        tarjeta = ft.Container(
            content=ft.Column(
                [texto_dia, texto_fecha, ft.Divider(), texto_hora],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.ORANGE_50,
            padding=25,
            border_radius=20,
            width=335,
        )

        # Llena los textos por primera vez y muestra la pantalla
        actualizar()
        mostrar([
            ft.Text("Mi día", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE),
            tarjeta,
            crear_boton("⬅ Volver", ft.Colors.GREY, volver),
        ])

        # Reloj en segundo plano: se repite mientras la tarjeta esté en pantalla
        async def reloj():
            while tarjeta in page.controls:
                await asyncio.sleep(1)
                actualizar()
                page.update()

        # Pone a correr el reloj sin congelar la app
        page.run_task(reloj)

    # --- Arrancar en el menú ---
    # Al abrir la app, muestra primero la pantalla principal
    pantalla_inicio()


# Arranca la app usando la función main (va fuera de main, sin sangría)
ft.run(main)