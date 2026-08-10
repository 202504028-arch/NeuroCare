import customtkinter as ctk
from tkinter import messagebox
from datetime import date
import random

from conexion import conectarBd


class rompecabezas:

    def __init__(self, root, idPaciente):

        self.root = root
        self.idPaciente = idPaciente

        # ------------------------------------------------------
        # VENTANA
        # ------------------------------------------------------

        self.ventana = ctk.CTkToplevel(root)
        self.ventana.title("NEUROCARE - ROMPECABEZAS")
        self.ventana.geometry("850x720+250+40")
        self.ventana.resizable(False, False)
        self.ventana.configure(fg_color="lavender")

        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar
        )

        # ------------------------------------------------------
        # DATOS DEL JUEGO
        # ------------------------------------------------------

        self.tamano = 4
        self.total_piezas = 16

        self.tablero = []
        self.botones = []

        self.movimientos = 0
        self.tiempo = 0

        self.jugando = False
        self.juego_iniciado = False
        self.bloqueado = False

        self.idActividad = self.obtener_actividad()

        self.crear_interfaz()

    # ==========================================================
    # ACTIVIDAD EN BASE DE DATOS
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
                ("Rompecabezas",)
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
                "Rompecabezas",
                "Actividad de memoria y razonamiento para ordenar las piezas.",
                300
            )

            cursor.execute(
                sql,
                valores
            )

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

        # ------------------------------------------------------
        # BARRA SUPERIOR
        # ------------------------------------------------------

        marco_superior = ctk.CTkFrame(
            self.ventana,
            fg_color="lavender",
            corner_radius=0
        )

        marco_superior.pack(
            fill="x",
            padx=20,
            pady=(15, 0)
        )

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
            command=self.cerrar
        )

        boton_regresar.pack(
            side="left"
        )

        # ------------------------------------------------------
        # TITULO
        # ------------------------------------------------------

        titulo = ctk.CTkLabel(
            self.ventana,
            text="🧩  ROMPECABEZAS",
            font=("Quicksand", 30, "bold"),
            text_color="#6C4AB6"
        )

        titulo.pack(
            pady=(5, 0)
        )

        subtitulo = ctk.CTkLabel(
            self.ventana,
            text="Ordena todas las piezas para completar el rompecabezas",
            font=("Quicksand", 15),
            text_color="#555555"
        )

        subtitulo.pack(
            pady=(0, 5)
        )

        # ------------------------------------------------------
        # INFORMACION
        # ------------------------------------------------------

        marco_informacion = ctk.CTkFrame(
            self.ventana,
            fg_color="transparent"
        )

        marco_informacion.pack(
            fill="x",
            padx=50,
            pady=(5, 5)
        )

        self.etiqueta_movimientos = ctk.CTkLabel(
            marco_informacion,
            text="Movimientos: 0",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_movimientos.pack(
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

        # ------------------------------------------------------
        # TABLERO
        # ------------------------------------------------------

        self.marco_tablero = ctk.CTkFrame(
            self.ventana,
            width=500,
            height=440,
            fg_color="lavender",
            corner_radius=15
        )

        self.marco_tablero.pack(
            pady=5
        )

        self.marco_tablero.pack_propagate(False)

        # ------------------------------------------------------
        # MENSAJE INICIAL
        # ------------------------------------------------------

        self.mensaje_inicio = ctk.CTkLabel(
            self.marco_tablero,
            text="Presiona \"EMPEZAR JUEGO\" para comenzar",
            font=("Quicksand", 19, "bold"),
            text_color="#6C4AB6"
        )

        self.mensaje_inicio.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # ------------------------------------------------------
        # BOTON EMPEZAR
        # ------------------------------------------------------

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

        self.movimientos = 0
        self.tiempo = 0

        self.jugando = True
        self.juego_iniciado = True
        self.bloqueado = False

        self.boton_empezar.configure(
            state="disabled",
            text="JUEGO EN CURSO"
        )

        self.mensaje_inicio.place_forget()

        # ------------------------------------------------------
        # CREAR TABLERO
        # ------------------------------------------------------

        self.tablero = list(
            range(1, self.total_piezas)
        )

        self.tablero.append(0)

        # Mezclar hasta que sea resoluble
        while True:

            random.shuffle(
                self.tablero
            )

            if self.es_resoluble(
                self.tablero
            ) and not self.esta_resuelto():

                break

        # ------------------------------------------------------
        # LIMPIAR TABLERO
        # ------------------------------------------------------

        for widget in self.marco_tablero.winfo_children():

            widget.destroy()

        self.botones = []

        # ------------------------------------------------------
        # CREAR PIEZAS
        # ------------------------------------------------------

        for fila in range(self.tamano):

            self.marco_tablero.grid_rowconfigure(
                fila,
                weight=1
            )

            for columna in range(self.tamano):

                self.marco_tablero.grid_columnconfigure(
                    columna,
                    weight=1
                )

                indice = (
                    fila * self.tamano
                ) + columna

                valor = self.tablero[indice]

                if valor == 0:

                    boton = ctk.CTkButton(
                        self.marco_tablero,
                        text="",
                        width=105,
                        height=90,
                        corner_radius=12,
                        fg_color="#DCD5ED",
                        hover_color="#DCD5ED",
                        state="disabled"
                    )

                else:

                    boton = ctk.CTkButton(
                        self.marco_tablero,
                        text=str(valor),
                        width=105,
                        height=90,
                        corner_radius=12,
                        fg_color="white",
                        hover_color="#E9DFFF",
                        text_color="#6C4AB6",
                        border_width=3,
                        border_color="#B99AEF",
                        font=("Quicksand", 25, "bold"),
                        command=lambda i=indice:
                        self.mover_pieza(i)
                    )

                boton.grid(
                    row=fila,
                    column=columna,
                    padx=7,
                    pady=7
                )

                self.botones.append(
                    boton
                )

        self.actualizar_informacion()

        self.actualizar_tiempo()

    # ==========================================================
    # MOVER PIEZA
    # ==========================================================

    def mover_pieza(self, indice):

        if not self.jugando:
            return

        if self.bloqueado:
            return

        indice_vacio = self.tablero.index(0)

        fila_pieza = indice // self.tamano
        columna_pieza = indice % self.tamano

        fila_vacia = (
            indice_vacio // self.tamano
        )

        columna_vacia = (
            indice_vacio % self.tamano
        )

        distancia = (
            abs(fila_pieza - fila_vacia)
            +
            abs(columna_pieza - columna_vacia)
        )

        # Solo puede moverse una pieza
        # que esté junto al espacio vacío

        if distancia != 1:
            return

        # ------------------------------------------------------
        # INTERCAMBIAR PIEZAS
        # ------------------------------------------------------

        self.tablero[indice], self.tablero[indice_vacio] = (
            self.tablero[indice_vacio],
            self.tablero[indice]
        )

        self.movimientos += 1

        self.actualizar_tablero()

        self.actualizar_informacion()

        # ------------------------------------------------------
        # COMPROBAR VICTORIA
        # ------------------------------------------------------

        if self.esta_resuelto():

            self.jugando = False

            self.guardar_resultado()

            self.mostrar_victoria()

    # ==========================================================
    # ACTUALIZAR TABLERO
    # ==========================================================

    def actualizar_tablero(self):

        for indice in range(
            self.total_piezas
        ):

            valor = self.tablero[indice]

            if valor == 0:

                self.botones[indice].configure(
                    text="",
                    fg_color="#DCD5ED",
                    hover_color="#DCD5ED",
                    state="disabled"
                )

            else:

                self.botones[indice].configure(
                    text=str(valor),
                    fg_color="white",
                    hover_color="#E9DFFF",
                    text_color="#6C4AB6",
                    state="normal"
                )

    # ==========================================================
    # COMPROBAR SI ESTÁ RESUELTO
    # ==========================================================

    def esta_resuelto(self):

        return self.tablero == list(
            range(
                1,
                self.total_piezas
            )
        ) + [0]

    # ==========================================================
    # COMPROBAR SI EL TABLERO ES RESOLUBLE
    # ==========================================================

    def es_resoluble(self, tablero):

        inversiones = 0

        lista = [
            numero
            for numero in tablero
            if numero != 0
        ]

        for i in range(
            len(lista)
        ):

            for j in range(
                i + 1,
                len(lista)
            ):

                if lista[i] > lista[j]:

                    inversiones += 1

        fila_vacia = (
            tablero.index(0)
            // self.tamano
        )

        fila_desde_abajo = (
            self.tamano - fila_vacia
        )

        if self.tamano % 2 == 1:

            return inversiones % 2 == 0

        else:

            if fila_desde_abajo % 2 == 0:

                return inversiones % 2 == 1

            else:

                return inversiones % 2 == 0

    # ==========================================================
    # INFORMACION
    # ==========================================================

    def actualizar_informacion(self):

        self.etiqueta_movimientos.configure(
            text=f"Movimientos: {self.movimientos}"
        )

    # ==========================================================
    # CRONOMETRO
    # ==========================================================

    def actualizar_tiempo(self):

        if not self.ventana.winfo_exists():
            return

        if self.jugando:

            minutos = (
                self.tiempo // 60
            )

            segundos = (
                self.tiempo % 60
            )

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
                100 - (
                    self.movimientos // 5
                )
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

        ventana = ctk.CTkToplevel(
            self.ventana
        )

        ventana.title(
            "Rompecabezas completado"
        )

        ventana.geometry(
            "430x430"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            fg_color="lavender"
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
            text="¡Completaste el rompecabezas!",
            font=("Quicksand", 18, "bold"),
            text_color="#333333"
        )

        mensaje.pack(
            pady=8
        )

        minutos = (
            self.tiempo // 60
        )

        segundos = (
            self.tiempo % 60
        )

        puntuacion = max(
            0,
            100 - (
                self.movimientos // 5
            )
        )

        resultado = ctk.CTkLabel(
            ventana,
            text=(
                f"Movimientos: {self.movimientos}\n\n"
                f"Puntuación: {puntuacion}\n\n"
                f"Tiempo: {minutos:02d}:{segundos:02d}"
            ),
            font=("Quicksand", 16),
            text_color="#555555",
            justify="center"
        )

        resultado.pack(
            pady=10
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

    def cerrar(self):

        self.jugando = False

        if self.ventana.winfo_exists():

            self.ventana.destroy()

            from actividades import juegos

            juegos(
                self.root,
                self.idPaciente
            )


# ==============================================================
# PRUEBA DIRECTA
# ==============================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("light")

    ctk.set_default_color_theme("blue")

    root = ctk.CTk()

    root.withdraw()

    idPaciente = 1

    juego = rompecabezas(
        root,
        idPaciente
    )

    root.mainloop()