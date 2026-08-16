import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
import random
import time

from conexion import conectarBd


class Rompecabezas:

    def __init__(self, root, idPaciente):

        self.root = root
        self.idPaciente = idPaciente

        # =====================================================
        # VENTANA
        # =====================================================

        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE - ROMPECABEZAS")
        self.ventana.geometry("760x850+350+1")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="lavender")

        self.ventana.protocol(
            "WM_DELETE_WINDOW",
            self.regresar
        )

        # =====================================================
        # IMAGEN DEL ROMPECABEZAS
        # =====================================================

        self.ruta_imagen = (
            "NEUROCARE/funciones/recursos/"
            "montaña.jpg"
        )

        self.imagen_original = None

        # =====================================================
        # CONFIGURACIÓN
        # =====================================================

        self.filas = 3
        self.columnas = 3

        # Tamaño de cada pieza
        self.tamano = 140

        self.piezas = []
        self.posiciones = []

        self.movimientos = 0

        self.tiempo_inicio = None
        self.tiempo_final = 0

        self.jugando = False

        self.seleccion = None

        # =====================================================
        # BASE DE DATOS
        # =====================================================

        self.idActividad = self.obtener_actividad()

        # =====================================================
        # INTERFAZ
        # =====================================================

        self.crear_interfaz()

        # Cargar automáticamente la imagen
        self.cargar_imagen()

    # =========================================================
    # BASE DE DATOS
    # =========================================================

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
                "Actividad para armar una imagen por piezas.",
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

    # =========================================================
    # INTERFAZ
    # =========================================================

    def crear_interfaz(self):

        # =====================================================
        # BOTÓN REGRESAR
        # =====================================================

        boton_regresar = ctk.CTkButton(
            self.ventana,
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
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # =====================================================
        # TÍTULO
        # =====================================================

        titulo = ctk.CTkLabel(
            self.ventana,
            text="🧩 ROMPECABEZAS",
            font=("Quicksand", 30, "bold"),
            text_color="#6C4AB6"
        )

        titulo.pack(
            pady=(5, 0)
        )

        subtitulo = ctk.CTkLabel(
            self.ventana,
            text="Acomoda las piezas para completar la imagen",
            font=("Quicksand", 15),
            text_color="#555555"
        )

        subtitulo.pack(
            pady=(0, 10)
        )

        # =====================================================
        # INFORMACIÓN
        # =====================================================

        marco_info = tk.Frame(
            self.ventana,
            bg="lavender"
        )

        marco_info.pack(
            fill="x",
            padx=80
        )

        self.etiqueta_movimientos = ctk.CTkLabel(
            marco_info,
            text="Movimientos: 0",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_movimientos.pack(
            side="left"
        )

        self.etiqueta_tiempo = ctk.CTkLabel(
            marco_info,
            text="Tiempo: 00:00",
            font=("Quicksand", 15, "bold"),
            text_color="#6C4AB6"
        )

        self.etiqueta_tiempo.pack(
            side="right"
        )

        # =====================================================
        # ETIQUETA / ESPACIO PARA LA IMAGEN
        # =====================================================

        self.etiqueta_imagen = tk.Label(
            self.ventana,
            text="Aquí aparecerá la imagen",
            bg="white",
            fg="#6C4AB6",
            font=("Quicksand", 14, "bold")
        )

        self.etiqueta_imagen.pack(
            pady=(5, 8)
        )

        # =====================================================
        # TABLERO
        # =====================================================

        self.tablero = tk.Frame(
            self.ventana,
            width=420,
            height=420,
            bg="lavender"
        )

        self.tablero.pack(
            pady=2
        )

        self.tablero.pack_propagate(False)

        # =====================================================
        # BOTÓN MEZCLAR
        # =====================================================

        boton_mezclar = ctk.CTkButton(
            self.ventana,
            text="🔀 MEZCLAR",
            width=180,
            height=45,
            corner_radius=12,
            fg_color="#22C55E",
            hover_color="#16A34A",
            font=("Quicksand", 14, "bold"),
            command=self.mezclar
        )

        boton_mezclar.pack(
            pady=5
        )

    # =========================================================
    # CARGAR IMAGEN
    # =========================================================

    def cargar_imagen(self):

        try:

            self.imagen_original = Image.open(
                self.ruta_imagen
            )

            # Mostrar una pequeña vista de la imagen original
            vista = self.imagen_original.copy()

            vista.thumbnail(
                (160, 90)
            )

            self.imagen_vista = ImageTk.PhotoImage(
                vista
            )

            self.etiqueta_imagen.configure(
                image=self.imagen_vista,
                text=""
            )

            self.crear_piezas()

            self.mezclar()

        except Exception as e:

            self.etiqueta_imagen.configure(
                text="No se pudo cargar la imagen"
            )

            messagebox.showerror(
                "Imagen",
                f"No se pudo cargar la imagen:\n\n{e}"
            )

    # =========================================================
    # CREAR PIEZAS
    # =========================================================

    def crear_piezas(self):

        for widget in self.tablero.winfo_children():
            widget.destroy()

        ancho = self.columnas * self.tamano
        alto = self.filas * self.tamano

        imagen = self.imagen_original.copy()

        imagen = imagen.resize(
            (ancho, alto)
        )

        self.piezas = []

        for fila in range(self.filas):

            for columna in range(self.columnas):

                izquierda = columna * self.tamano
                arriba = fila * self.tamano

                derecha = izquierda + self.tamano
                abajo = arriba + self.tamano

                pieza = imagen.crop(
                    (
                        izquierda,
                        arriba,
                        derecha,
                        abajo
                    )
                )

                self.piezas.append(
                    pieza
                )

        self.posiciones = list(
            range(
                len(self.piezas)
            )
        )

    # =========================================================
    # MOSTRAR PIEZAS
    # =========================================================

    def mostrar_piezas(self):

        for widget in self.tablero.winfo_children():
            widget.destroy()

        for posicion, indice_pieza in enumerate(
            self.posiciones
        ):

            fila = posicion // self.columnas
            columna = posicion % self.columnas

            imagen = self.piezas[
                indice_pieza
            ]

            imagen_tk = ImageTk.PhotoImage(
                imagen
            )

            boton = tk.Button(
                self.tablero,
                image=imagen_tk,
                width=self.tamano,
                height=self.tamano,
                bd=2,
                relief="solid",
                command=lambda p=posicion:
                self.seleccionar(p)
            )

            boton.image = imagen_tk

            boton.grid(
                row=fila,
                column=columna
            )

    # =========================================================
    # MEZCLAR
    # =========================================================

    def mezclar(self):

        if not self.piezas:
            return

        random.shuffle(
            self.posiciones
        )

        # Evitar que por casualidad salga armado
        if self.posiciones == list(
            range(len(self.piezas))
        ):

            random.shuffle(
                self.posiciones
            )

        self.movimientos = 0
        self.seleccion = None

        self.etiqueta_movimientos.configure(
            text="Movimientos: 0"
        )

        self.tiempo_inicio = time.time()

        self.tiempo_final = 0

        self.jugando = True

        self.mostrar_piezas()

        self.actualizar_tiempo()

    # =========================================================
    # SELECCIONAR PIEZA
    # =========================================================

    def seleccionar(self, posicion):

        if not self.jugando:
            return

        # Primera pieza
        if self.seleccion is None:

            self.seleccion = posicion

            return

        # Segunda pieza
        segunda = posicion

        if self.seleccion == segunda:
            return

        # Intercambiar piezas
        self.posiciones[
            self.seleccion
        ], self.posiciones[
            segunda
        ] = self.posiciones[
            segunda
        ], self.posiciones[
            self.seleccion
        ]

        self.movimientos += 1

        self.etiqueta_movimientos.configure(
            text=f"Movimientos: {self.movimientos}"
        )

        self.seleccion = None

        self.mostrar_piezas()

        self.comprobar_victoria()

    # =========================================================
    # COMPROBAR VICTORIA
    # =========================================================

    def comprobar_victoria(self):

        if self.posiciones == list(
            range(
                len(self.piezas)
            )
        ):

            self.jugando = False

            self.tiempo_final = int(
                time.time() -
                self.tiempo_inicio
            )

            self.guardar_resultado()

            minutos = self.tiempo_final // 60
            segundos = self.tiempo_final % 60

            puntuacion = max(
                0,
                100 - (
                    self.movimientos * 2
                )
            )

            messagebox.showinfo(
                "🎉 ¡Felicidades!",
                (
                    "¡Completaste el rompecabezas!\n\n"
                    f"Movimientos: {self.movimientos}\n"
                    f"Puntuación: {puntuacion}\n"
                    f"Tiempo: "
                    f"{minutos:02d}:{segundos:02d}"
                )
            )

    # =========================================================
    # TIEMPO
    # =========================================================

    def actualizar_tiempo(self):

        if not self.jugando:
            return

        if not self.ventana.winfo_exists():
            return

        segundos = int(
            time.time() -
            self.tiempo_inicio
        )

        minutos = segundos // 60
        segundos = segundos % 60

        self.etiqueta_tiempo.configure(
            text=f"Tiempo: {minutos:02d}:{segundos:02d}"
        )

        self.ventana.after(
            1000,
            self.actualizar_tiempo
        )

    # =========================================================
    # GUARDAR RESULTADO EN BD
    # =========================================================

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
                    self.movimientos * 2
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
                __import__("datetime").date.today(),
                puntuacion,
                self.tiempo_final,
                True
            )

            cursor.execute(
                sql,
                valores
            )

            conexion.commit()

        except Exception as e:

            messagebox.showerror(
                "Base de datos",
                f"No se pudo guardar el resultado:\n\n{e}"
            )

        finally:

            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    # =========================================================
    # REGRESAR
    # =========================================================

    def regresar(self):

        self.jugando = False

        if self.ventana.winfo_exists():

            self.ventana.destroy()

        if self.root.winfo_exists():

            self.root.deiconify()

            # Restauramos Actividades
            self.root.geometry(
                "520x700+520+60"
            )

            self.root.update_idletasks()


# =============================================================
# PRUEBA DIRECTA
# =============================================================

if __name__ == "__main__":

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = tk.Tk()

    root.withdraw()

    idPaciente = 22

    app = Rompecabezas(
        root,
        idPaciente
    )

    root.mainloop()