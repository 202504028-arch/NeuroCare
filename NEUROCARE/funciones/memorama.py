import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random

# python NEUROCARE/funciones/memorama.pyp

class memoramaj:

    def __init__(self, root):

        self.root = root
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- MEMORAMA")
        self.ventana.geometry("500x700+520+60")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(500,700)
        self.ventana.maxsize(700,800)

        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        self.ventana.protocol("WM_DELETE_WINDOW", self.regresar)

        self.intentos = 0
        self.parejas = 0
        self.segundos = 0

        self.crear_interfaz()
        self.actualizar_tiempo()

    def crear_interfaz(self):

        #-------------------- MARCO PRINCIPAL --------------------#

        self.marco_principal = tk.Frame(self.ventana)
        self.marco_principal.configure(bg="lavender")
        self.marco_principal.pack(fill="both", expand=True)

        #-------------------- CABECERA --------------------#

        marco_superior = tk.Frame(self.marco_principal)
        marco_superior.configure(bg="lavender")
        marco_superior.pack(fill="x", padx=20, pady=(20,10))

        #-------------------- BOTON REGRESAR --------------------#

        boton_regresar = ctk.CTkButton(
            marco_superior,
            text="←",
            width=50,
            height=50,
            corner_radius=25,
            fg_color="white",
            hover_color="#E5E7EB",
            text_color="black",
            font=("Arial",24,"bold"),
            command=self.regresar
        )
        boton_regresar.pack(side="left")

        #-------------------- TITULO --------------------#

        marco_titulo = tk.Frame(marco_superior)
        marco_titulo.configure(bg="lavender")
        marco_titulo.pack(side="left", expand=True)

        etiqueta_categoria = tk.Label(
            marco_titulo,
            text="COGNITIVA"
        )
        etiqueta_categoria.configure(
            bg="lavender",
            fg="dim gray",
            font=("Quicksand",12,"bold")
        )
        etiqueta_categoria.pack()

        etiqueta_titulo = tk.Label(
            marco_titulo,
            text="Memorama"
        )
        etiqueta_titulo.configure(
            bg="lavender",
            fg="black",
            font=("Quicksand",22,"bold")
        )
        etiqueta_titulo.pack()

        #-------------------- BOTON REINICIAR --------------------#

        boton_reiniciar = ctk.CTkButton(
            marco_superior,
            text="↻",
            width=50,
            height=50,
            corner_radius=25,
            fg_color="white",
            hover_color="#E5E7EB",
            text_color="black",
            font=("Arial",24,"bold"),
            command=self.reiniciar
        )
        boton_reiniciar.pack(side="right")

        #-------------------- INFORMACION --------------------#

        marco_info = tk.Frame(self.marco_principal)
        marco_info.configure(bg="lavender")
        marco_info.pack(fill="x", padx=20, pady=(10,20))

        tarjeta_tiempo = ctk.CTkFrame(
            marco_info,
            width=130,
            height=80,
            corner_radius=20,
            fg_color="white"
        )
        tarjeta_tiempo.pack(side="left", padx=5)
        tarjeta_tiempo.pack_propagate(False)

        tk.Label(
            tarjeta_tiempo,
            text="TIEMPO",
            bg="white",
            fg="dim gray",
            font=("Quicksand",12)
        ).pack(pady=(12,0))

        self.etiqueta_tiempo = tk.Label(
            tarjeta_tiempo,
            text="00:00",
            bg="white",
            fg="black",
            font=("Quicksand",20,"bold")
        )
        self.etiqueta_tiempo.pack()

        tarjeta_intentos = ctk.CTkFrame(
            marco_info,
            width=130,
            height=80,
            corner_radius=20,
            fg_color="white"
        )
        tarjeta_intentos.pack(side="left", padx=5)
        tarjeta_intentos.pack_propagate(False)

        tk.Label(
            tarjeta_intentos,
            text="INTENTOS",
            bg="white",
            fg="dim gray",
            font=("Quicksand",12)
        ).pack(pady=(12,0))

        self.etiqueta_intentos = tk.Label(
            tarjeta_intentos,
            text="0",
            bg="white",
            fg="black",
            font=("Quicksand",20,"bold")
        )
        self.etiqueta_intentos.pack()

        tarjeta_parejas = ctk.CTkFrame(
            marco_info,
            width=130,
            height=80,
            corner_radius=20,
            fg_color="white"
        )
        tarjeta_parejas.pack(side="left", padx=5)
        tarjeta_parejas.pack_propagate(False)

        tk.Label(
            tarjeta_parejas,
            text="PAREJAS",
            bg="white",
            fg="dim gray",
            font=("Quicksand",12)
        ).pack(pady=(12,0))

        self.etiqueta_parejas = tk.Label(
            tarjeta_parejas,
            text="0/8",
            bg="white",
            fg="black",
            font=("Quicksand",20,"bold")
        )
        self.etiqueta_parejas.pack()

        #-------------------- TABLERO --------------------#

        self.marco_tablero = tk.Frame(self.marco_principal)
        self.marco_tablero.configure(width=450, height=450, bg="lavender")
        self.marco_tablero.pack(pady=(10,20))
        self.marco_tablero.pack_propagate(False)

        #-------------------- IMAGENES --------------------#

        self.imagen_fish = tk.PhotoImage(file="NEUROCARE/funciones/recursos/fish_4x4-cm.png")
        self.imagen_island = tk.PhotoImage(file="NEUROCARE/funciones/recursos/island_4x4-cm.png")
        self.imagen_jellyfish = tk.PhotoImage(file="NEUROCARE/funciones/recursos/jellyfish_4x4-cm.png")
        self.imagen_lighthouse = tk.PhotoImage(file="NEUROCARE/funciones/recursos/lighthouse_4x4-cm.png")
        self.imagen_mar = tk.PhotoImage(file="NEUROCARE/funciones/recursos/mar_4x4-cm.png")
        self.imagen_marines = tk.PhotoImage(file="NEUROCARE/funciones/recursos/marines_4x4-cm.png")
        self.imagen_sharks = tk.PhotoImage(file="NEUROCARE/funciones/recursos/sharks_4x4-cm.png")
        self.imagen_starfish = tk.PhotoImage(file="NEUROCARE/funciones/recursos/starfish_4x4-cm.png")

        self.cartas = [
            self.imagen_fish,
            self.imagen_island,
            self.imagen_jellyfish,
            self.imagen_lighthouse,
            self.imagen_mar,
            self.imagen_marines,
            self.imagen_sharks,
            self.imagen_starfish
        ]

        self.identificadores = [0,1,2,3,4,5,6,7]

        self.cartas = self.cartas * 2
        self.identificadores = self.identificadores * 2

        combinadas = list(zip(self.cartas, self.identificadores))
        random.shuffle(combinadas)
        self.cartas, self.identificadores = zip(*combinadas)
        self.cartas = list(self.cartas)
        self.identificadores = list(self.identificadores)

        #-------------------- VARIABLES --------------------#

        self.primera_carta = None
        self.segunda_carta = None
        self.cartas_descubiertas = []
        self.bloqueado = False

        #-------------------- BOTONES --------------------#

        self.botones = []

        for fila in range(4):

            for columna in range(4):

                indice = len(self.botones)

                boton = tk.Button(
                    self.marco_tablero,
                    text="",
                    width=6,
                    height=3,
                    bg="#7C3AED",
                    activebackground="#6D28D9",
                    relief="flat",
                    bd=0,
                    highlightthickness=0,
                    command=lambda i=indice: self.voltear_carta(i)
                )

                boton.grid(
                    row=fila,
                    column=columna,
                    padx=8,
                    pady=8,
                    ipadx=12,
                    ipady=12
                )

                self.botones.append(boton)

    def regresar(self):

        self.ventana.destroy()

        try:
            from actividades import juegos
            juegos(self.root)
        except Exception:
            pass

    def reiniciar(self):

        self.ventana.destroy()
        memoramaj(self.root)

    def actualizar_tiempo(self):

        self.segundos += 1

        minutos = self.segundos // 60
        segundos = self.segundos % 60

        self.etiqueta_tiempo.configure(
            text=f"{minutos:02}:{segundos:02}"
        )

        if self.parejas < 8:
            self.ventana.after(1000, self.actualizar_tiempo)

    def voltear_carta(self, indice):

        if self.bloqueado:
            return

        if indice in self.cartas_descubiertas:
            return

        if self.primera_carta == indice:
            return

        boton = self.botones[indice]

        boton.configure(
            image=self.cartas[indice],
            text="",
            bg="white",
            activebackground="white"
        )

        if self.primera_carta is None:

            self.primera_carta = indice

        else:

            self.segunda_carta = indice
            self.bloqueado = True
            self.ventana.after(800, self.comparar_cartas)

    def comparar_cartas(self):

        primera = self.primera_carta
        segunda = self.segunda_carta

        self.intentos += 1
        self.etiqueta_intentos.configure(text=str(self.intentos))

        if self.identificadores[primera] == self.identificadores[segunda]:

            self.cartas_descubiertas.append(primera)
            self.cartas_descubiertas.append(segunda)

            self.botones[primera].configure(state="disabled")
            self.botones[segunda].configure(state="disabled")

            self.parejas += 1
            self.etiqueta_parejas.configure(text=f"{self.parejas}/8")

        else:

            self.botones[primera].configure(
                image="",
                text="",
                bg="#7C3AED",
                activebackground="#6D28D9"
            )

            self.botones[segunda].configure(
                image="",
                text="",
                bg="#7C3AED",
                activebackground="#6D28D9"
            )

        self.primera_carta = None
        self.segunda_carta = None
        self.bloqueado = False

        if self.parejas == 8:

            self.bloqueado = True

            messagebox.showinfo(
                "¡Felicidades!",
                f"Completaste el memorama.\n\nIntentos: {self.intentos}\nTiempo: {self.etiqueta_tiempo.cget('text')}"
            )

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.withdraw()
    app = memoramaj(ventana)
    ventana.mainloop()