import tkinter as tk
from tkinter import messagebox
from datetime import date
import random
import customtkinter as ctk

from conexion import conectarBd


class memoramaa:

    def __init__(self, root, idPaciente):

        self.root = root
        self.idPaciente = idPaciente

        # ======================================================
        # VENTANA PRINCIPAL DEL JUEGO
        # ======================================================

        # IMPORTANTE:
        # Usamos Tkinter normal para la ventana principal.
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE - MEMORAMA")
        self.ventana.geometry("760x700+250+40")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="lavender")

        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar
        )

        # ======================================================
        # DATOS DEL JUEGO
        # ======================================================

        self.pares = [
            "🧠", "🧠",
            "⭐", "⭐",
            "🌸", "🌸",
            "🐟", "🐟",
            "🍎", "🍎",
            "🌈", "🌈",
            "🦋", "🦋",
            "🐣", "🐣"
        ]

        self.cartas = []

        self.primera_carta = None
        self.segunda_carta = None

        self.bloqueado = False

        self.pares_encontrados = 0
        self.intentos = 0
        self.errores = 0

        self.tiempo = 0

        self.jugando = False
        self.juego_iniciado = False

        # ======================================================
        # ACTIVIDAD EN BASE DE DATOS
        # ======================================================

        self.idActividad = self.obtener_actividad()

        # ======================================================
        # CREAR INTERFAZ
        # ======================================================

        self.crear_interfaz()

    # ==========================================================
    # OBTENER ACTIVIDAD
    # ==========================================================

    def obtener_actividad(self):

        conexion = None
        cursor = None

        try:

            conexion = conectarBd()
            cursor = conexion.cursor()

            sql = """
            SELECT idActividad
            FROM actividad
            WHERE nombreActividad = %s
            LIMIT 1
            """

            cursor.execute(
                sql,
                ("Memorama",)
            )

            resultado = cursor.fetchone()

            if resultado:
                return resultado[0]

            sql = """
            INSERT INTO actividad
            (
                nombreActividad,
                descripcion,
                tiempoEstimado
            )
            VALUES (%s, %s, %s)
            """

            valores = (
                "Memorama",
                "Actividad de memoria para encontrar parejas.",
                300
            )

            cursor.execute(sql, valores)

            conexion.commit()

            return cursor.lastrowid

        except Exception as e:

            messagebox.showerror(
                "Base de datos",
                f"No se pudo obtener la actividad:\n\n{e}"
            )

            return None

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def crear_interfaz(self):

        # ======================================================
        # BARRA SUPERIOR
        # ======================================================

        marco_superior = tk.Frame(
            self.ventana,
            bg="lavender"
        )

        marco_superior.pack(
            fill="x",
            padx=20,
            pady=(15, 0)
        )

        # Botón usando CustomTkinter
        boton_regresar = ctk.CTkButton(
            marco_superior,
            text="← REGRESAR",
            width=130,
            height=40,
            corner_radius=10,
            fg_color="white",
            hover_color="#E6E0F5",
            text_color="#6C4AB6",
            border_width=2,
            border_color="#6C4AB6",
            font=("Quicksand", 14, "bold"),
            command=self.regresar
        )

        boton_regresar.pack(
            side="left"
        )

        # ======================================================
        # TITULO
        # ======================================================

        titulo = ctk.CTkLabel(
            self.ventana,
            text="🧠  MEMORAMA",
            font=("Quicksand", 30, "bold"),
            text_color="#6C4AB6"
        )

        titulo.pack(
            pady=(5, 0)
        )

        subtitulo = ctk.CTkLabel(
            self.ventana,
            text="Encuentra todas las parejas",
            font=("Quicksand", 16),
            text_color="#555555"
        )

        subtitulo.pack(
            pady=(0, 5)
        )

        # ======================================================
        # INFORMACION
        # ======================================================

        marco_informacion = tk.Frame(
            self.ventana,
            bg="lavender"
        )

        marco_informacion.pack(
            fill="x",
            padx=50,
            pady=(5, 5)
        )

        self.etiqueta_pares = ctk.CTkLabel(
            marco_informacion,
            text="Parejas: 0 / 8",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_pares.pack(
            side="left",
            padx=20
        )

        self.etiqueta_intentos = ctk.CTkLabel(
            marco_informacion,
            text="Intentos: 0",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_intentos.pack(
            side="left",
            padx=20
        )

        self.etiqueta_tiempo = ctk.CTkLabel(
            marco_informacion,
            text="Tiempo: 00:00",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_tiempo.pack(
            side="right",
            padx=20
        )

        # ======================================================
        # TABLERO
        # ======================================================

        self.marco_tablero = tk.Frame(
            self.ventana,
            width=680,
            height=440,
            bg="lavender"
        )

        self.marco_tablero.pack(
            pady=5
        )

        self.marco_tablero.pack_propagate(False)

        # ======================================================
        # MENSAJE INICIAL
        # ======================================================

        self.mensaje_inicio = ctk.CTkLabel(
            self.marco_tablero,
            text='Presiona "EMPEZAR JUEGO" para comenzar',
            font=("Quicksand", 20, "bold"),
            text_color="#6C4AB6"
        )

        self.mensaje_inicio.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ======================================================
        # BOTON EMPEZAR
        # ======================================================

        self.boton_empezar = ctk.CTkButton(
            self.ventana,
            text="▶  EMPEZAR JUEGO",
            width=260,
            height=55,
            corner_radius=12,
            fg_color="#6C4AB6",
            hover_color="#573A99",
            font=("Quicksand", 17, "bold"),
            command=self.iniciar_juego
        )

        self.boton_empezar.pack(
            pady=(10, 20)
        )

    # ==========================================================
    # INICIAR JUEGO
    # ==========================================================

    def iniciar_juego(self):

        self.pares_encontrados = 0
        self.intentos = 0
        self.errores = 0
        self.tiempo = 0

        self.primera_carta = None
        self.segunda_carta = None

        self.bloqueado = False

        self.jugando = True
        self.juego_iniciado = True

        self.boton_empezar.configure(
            state="disabled",
            text="JUEGO EN CURSO"
        )

        self.mensaje_inicio.place_forget()

        random.shuffle(self.pares)

        # Limpiar tablero

        for widget in self.marco_tablero.winfo_children():
            widget.destroy()

        self.cartas = []

        # ======================================================
        # CREAR CARTAS
        # ======================================================

        for fila in range(4):

            self.marco_tablero.grid_rowconfigure(
                fila,
                weight=1
            )

            for columna in range(4):

                self.marco_tablero.grid_columnconfigure(
                    columna,
                    weight=1
                )

                indice = fila * 4 + columna

                carta = ctk.CTkButton(
                    self.marco_tablero,
                    text="?",
                    width=130,
                    height=90,
                    corner_radius=15,
                    fg_color="white",
                    hover_color="#E9DFFF",
                    text_color="#6C4AB6",
                    border_width=3,
                    border_color="#B99AEF",
                    font=("Arial", 30, "bold"),
                    command=lambda i=indice:
                    self.voltear_carta(i)
                )

                carta.grid(
                    row=fila,
                    column=columna,
                    padx=7,
                    pady=7
                )

                self.cartas.append({
                    "boton": carta,
                    "valor": self.pares[indice],
                    "descubierta": False,
                    "encontrada": False
                })

        self.actualizar_informacion()

        self.actualizar_tiempo()

    # ==========================================================
    # VOLTEAR CARTA
    # ==========================================================

    def voltear_carta(self, indice):

        if not self.jugando:
            return

        if self.bloqueado:
            return

        carta = self.cartas[indice]

        if carta["descubierta"]:
            return

        if carta["encontrada"]:
            return

        carta["descubierta"] = True

        carta["boton"].configure(
            text=carta["valor"],
            fg_color="#E9DFFF",
            hover_color="#E9DFFF",
            text_color="#573A99"
        )

        if self.primera_carta is None:

            self.primera_carta = indice

        else:

            self.segunda_carta = indice

            self.intentos += 1

            self.actualizar_informacion()

            self.bloqueado = True

            self.ventana.after(
                700,
                self.comprobar_pareja
            )

    # ==========================================================
    # COMPROBAR PAREJA
    # ==========================================================

    def comprobar_pareja(self):

        if self.primera_carta is None:
            return

        if self.segunda_carta is None:
            return

        primera = self.cartas[
            self.primera_carta
        ]

        segunda = self.cartas[
            self.segunda_carta
        ]

        if primera["valor"] == segunda["valor"]:

            primera["encontrada"] = True
            segunda["encontrada"] = True

            primera["boton"].configure(
                fg_color="#C8F7DD",
                hover_color="#C8F7DD",
                border_color="#68C69B"
            )

            segunda["boton"].configure(
                fg_color="#C8F7DD",
                hover_color="#C8F7DD",
                border_color="#68C69B"
            )

            self.pares_encontrados += 1

            self.primera_carta = None
            self.segunda_carta = None
            self.bloqueado = False

            self.actualizar_informacion()

            if self.pares_encontrados == 8:

                self.jugando = False

                self.guardar_resultado()

                self.mostrar_victoria()

        else:

            self.errores += 1

            self.ventana.after(
                500,
                self.ocultar_cartas
            )

    # ==========================================================
    # OCULTAR CARTAS
    # ==========================================================

    def ocultar_cartas(self):

        if self.primera_carta is None:
            return

        if self.segunda_carta is None:
            return

        primera = self.cartas[
            self.primera_carta
        ]

        segunda = self.cartas[
            self.segunda_carta
        ]

        primera["descubierta"] = False
        segunda["descubierta"] = False

        primera["boton"].configure(
            text="?",
            fg_color="white",
            hover_color="#E9DFFF",
            text_color="#6C4AB6"
        )

        segunda["boton"].configure(
            text="?",
            fg_color="white",
            hover_color="#E9DFFF",
            text_color="#6C4AB6"
        )

        self.primera_carta = None
        self.segunda_carta = None

        self.bloqueado = False

    # ==========================================================
    # ACTUALIZAR INFORMACION
    # ==========================================================

    def actualizar_informacion(self):

        self.etiqueta_pares.configure(
            text=f"Parejas: {self.pares_encontrados} / 8"
        )

        self.etiqueta_intentos.configure(
            text=f"Intentos: {self.intentos}"
        )

    # ==========================================================
    # TIEMPO
    # ==========================================================

    def actualizar_tiempo(self):

        if not self.ventana.winfo_exists():
            return

        if self.jugando:

            minutos = self.tiempo // 60
            segundos = self.tiempo % 60

            self.etiqueta_tiempo.configure(
                text=f"Tiempo: {minutos:02d}:{segundos:02d}"
            )

            self.tiempo += 1

            self.ventana.after(
                1000,
                self.actualizar_tiempo
            )

    # ==========================================================
    # GUARDAR RESULTADO
    # ==========================================================

    def guardar_resultado(self):

        if self.idActividad is None:
            return

        conexion = None
        cursor = None

        try:

            conexion = conectarBd()
            cursor = conexion.cursor()

            puntuacion = max(
                0,
                100 - (self.errores * 5)
            )

            sql = """
            INSERT INTO historialActividad
            (
                idPaciente,
                idActividad,
                fecha,
                puntuacion,
                tiempoRealizado,
                completada
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                self.idPaciente,
                self.idActividad,
                date.today(),
                puntuacion,
                self.tiempo,
                True
            )

            cursor.execute(
                sql,
                valores
            )

            conexion.commit()

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"No se pudo guardar el resultado:\n\n{e}"
            )

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    # ==========================================================
    # VICTORIA
    # ==========================================================

    def mostrar_victoria(self):

        ventana = tk.Toplevel(
            self.ventana
        )

        ventana.title(
            "Memorama completado"
        )

        ventana.geometry(
            "430x430+300+100"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="lavender"
        )

        ventana.transient(
            self.ventana
        )

        ventana.grab_set()

        titulo = ctk.CTkLabel(
            ventana,
            text="🎉 ¡Felicidades!",
            font=("Quicksand", 28, "bold"),
            text_color="#6C4AB6"
        )

        titulo.pack(
            pady=(30, 10)
        )

        mensaje = ctk.CTkLabel(
            ventana,
            text="¡Encontraste todas las parejas!",
            font=("Quicksand", 18, "bold"),
            text_color="#333333"
        )

        mensaje.pack(
            pady=8
        )

        minutos = self.tiempo // 60
        segundos = self.tiempo % 60

        puntuacion = max(
            0,
            100 - (self.errores * 5)
        )

        resultado = ctk.CTkLabel(
            ventana,
            text=(
                f"Parejas: 8 / 8\n\n"
                f"Intentos: {self.intentos}\n\n"
                f"Errores: {self.errores}\n\n"
                f"Puntuación: {puntuacion}\n\n"
                f"Tiempo: {minutos:02d}:{segundos:02d}"
            ),
            font=("Quicksand", 15),
            text_color="#555555",
            justify="center"
        )

        resultado.pack(
            pady=8
        )

        boton = ctk.CTkButton(
            ventana,
            text="JUGAR DE NUEVO",
            width=220,
            height=45,
            corner_radius=12,
            fg_color="#6C4AB6",
            hover_color="#573A99",
            font=("Quicksand", 15, "bold"),
            command=lambda:
            self.nuevo_juego(ventana)
        )

        boton.pack(
            pady=15
        )

    # ==========================================================
    # NUEVO JUEGO
    # ==========================================================

    def nuevo_juego(self, ventana):

        ventana.destroy()

        self.iniciar_juego()

    # ==========================================================
    # REGRESAR
    # ==========================================================

    def regresar(self):

        self.jugando = False

        # Cancelar cualquier ventana secundaria de victoria
        # que todavía pudiera existir.
        for ventana in self.ventana.winfo_children():

            if isinstance(ventana, tk.Toplevel):
                try:
                    ventana.destroy()
                except:
                    pass

        # Destruir el juego
        if self.ventana.winfo_exists():
            self.ventana.destroy()

        # ======================================================
        # RESTAURAR ACTIVIDADES
        # ======================================================

        if self.root.winfo_exists():

            self.root.deiconify()

            # Restaurar tamaño y posición centrado
            self.root.geometry("650x700+0+0")
            self.root.update_idletasks()
            ancho = self.root.winfo_width()
            alto = self.root.winfo_height()
            x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
            y = (self.root.winfo_screenheight() // 2) - (alto // 2)
            self.root.geometry(f"{ancho}x{alto}+{x}+{y}")


    # ==========================================================
    # CERRAR
    # ==========================================================

    def cerrar(self):

        self.jugando = False

        if self.ventana.winfo_exists():
            self.ventana.destroy()

        if self.root.winfo_exists():

            self.root.deiconify()

            self.root.geometry("650x700+0+0")
            self.root.update_idletasks()
            ancho = self.root.winfo_width()
            alto = self.root.winfo_height()
            x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
            y = (self.root.winfo_screenheight() // 2) - (alto // 2)
            self.root.geometry(f"{ancho}x{alto}+{x}+{y}")


# ==============================================================
# PRUEBA DIRECTA
# ==============================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("light")

    ctk.set_default_color_theme("blue")

    # Ventana raíz normal
    root = tk.Tk()

    root.withdraw()

    idPaciente = 1

    juego = memoramaa(
        root,
        idPaciente
    )

    root.mainloop()