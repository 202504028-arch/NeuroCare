import tkinter as tk
from tkinter import ttk

class MiPerfilPaciente:
    def __init__(self, root):
        self.root = root
        self.root.title("NeuroCare - Mi Perfil")
        self.root.geometry("400x700")
        self.root.configure(bg="white smoke")
        
        self.crear_interfaz()

    def crear_interfaz(self):
        # ----------------------------------------
        # FRAME PRINCIPAL (CONTENEDOR CON SCROLL)
        # ----------------------------------------
        self.main_canvas = tk.Canvas(self.root, bg="white smoke", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg="white smoke")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )

        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # ----------------------------------------
        # TITULO
        # ----------------------------------------
        self.frame_titulo = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_titulo.pack(fill="x", padx=20, pady=(20, 10))
        self.frame_titulo.pack_propagate(False)
        self.frame_titulo.configure(height=40)

        tk.Label(
            self.frame_titulo, 
            text="Mi perfil", 
            font=("Quicksand", 22, "bold"), 
            bg="white smoke", 
            fg="black"
        ).pack(anchor="w")

        # ----------------------------------------
        # TARJETA INFORMACION PERSONAL
        # ----------------------------------------
        self.frame_tarjeta_perfil = tk.Frame(
            self.scrollable_frame, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_tarjeta_perfil.pack(fill="x", padx=20, pady=10)
        self.frame_tarjeta_perfil.pack_propagate(False)
        self.frame_tarjeta_perfil.configure(height=260)

        # Franja superior de la tarjeta (Púrpura)
        self.frame_header_tarjeta = tk.Frame(self.frame_tarjeta_perfil, bg="MediumPurple3")
        self.frame_header_tarjeta.pack(fill="x", padx=10, pady=10)
        self.frame_header_tarjeta.pack_propagate(False)
        self.frame_header_tarjeta.configure(height=65)

        tk.Label(
            self.frame_header_tarjeta, 
            text="PACIENTE NEUROCARE", 
            font=("Quicksand", 9, "bold"), 
            bg="MediumPurple3", 
            fg="Lavender"
        ).pack(anchor="nw", padx=15, pady=(8, 0))

        tk.Label(
            self.frame_header_tarjeta, 
            text="Sisi", 
            font=("Quicksand", 16, "bold"), 
            bg="MediumPurple3", 
            fg="white"
        ).pack(anchor="nw", padx=15, pady=(0, 8))

        # Cuerpo de datos clínicos de la tarjeta
        self.frame_datos_grid = tk.Frame(self.frame_tarjeta_perfil, bg="white")
        self.frame_datos_grid.pack(fill="both", expand=True, padx=15, pady=10)

        # Columna Izquierda
        self.frame_col_izq = tk.Frame(self.frame_datos_grid, bg="white")
        self.frame_col_izq.pack(side="left", fill="both", expand=True)

        tk.Label(self.frame_col_izq, text="EDAD", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="72", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="CELULAR", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="1234537890", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="ETAPA DE ALZHEIMER", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="MÉDICO", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w")

        # Columna Derecha
        self.frame_col_der = tk.Frame(self.frame_datos_grid, bg="white")
        self.frame_col_der.pack(side="right", fill="both", expand=True)

        tk.Label(self.frame_col_der, text="TIPO DE SANGRE", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_der, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_der, text="EMERGENCIA", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_der, text="123456789", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_der, text="ALERGIAS", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w", pady=(18, 0))
        tk.Label(self.frame_col_der, text="Ninguna", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w")

        # ----------------------------------------
        # RESUMEN SEMANAL
        # ----------------------------------------
        self.frame_titulo_resumen = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_titulo_resumen.pack(fill="x", padx=20, pady=(15, 5))
        self.frame_titulo_resumen.pack_propagate(False)
        self.frame_titulo_resumen.configure(height=30)

        tk.Label(
            self.frame_titulo_resumen, 
            text="Resumen semanal", 
            font=("Quicksand", 16, "bold"), 
            bg="white smoke", 
            fg="black"
        ).pack(anchor="w")

        self.frame_resumen_contenedor = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_resumen_contenedor.pack(fill="x", padx=20, pady=5)
        self.frame_resumen_contenedor.pack_propagate(False)
        self.frame_resumen_contenedor.configure(height=110)

        # Tarjeta Actividades completadas
        self.frame_card_act = tk.Frame(
            self.frame_resumen_contenedor, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_card_act.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self.frame_card_act.pack_propagate(False)

        tk.Label(self.frame_card_act, text="0", font=("Quicksand", 16, "bold"), bg="white", fg="black").pack(pady=(25, 0))
        tk.Label(self.frame_card_act, text="Actividades completadas", font=("Quicksand", 8), bg="white", fg="dim gray").pack()

        # Tarjeta Ejercicios realizados
        self.frame_card_ej = tk.Frame(
            self.frame_resumen_contenedor, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_card_ej.pack(side="right", fill="both", expand=True, padx=(5, 0))
        self.frame_card_ej.pack_propagate(False)

        tk.Label(self.frame_card_ej, text="0", font=("Quicksand", 16, "bold"), bg="white", fg="black").pack(pady=(25, 0))
        tk.Label(self.frame_card_ej, text="Ejercicios realizados", font=("Quicksand", 8), bg="white", fg="dim gray").pack()

        # ----------------------------------------
        # BARRA DE NAVEGACION INFERIOR (NAVBAR)
        # ----------------------------------------
        self.frame_navbar = tk.Frame(self.root, bg="white", height=60, highlightbackground="gainsboro", highlightthickness=1)
        self.frame_navbar.pack(side="bottom", fill="x")
        self.frame_navbar.pack_propagate(False)

        # Se distribuyen los 5 botones del menú inferior de forma uniforme
        self.frame_navbar.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        tk.Button(self.frame_navbar, text="🏠\nInicio", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=0, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🧠\nRecuerdos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=1, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🖼️\nRecuerdos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=2, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🔔\nAvisos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=3, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="👤\nPerfil", font=("Quicksand", 8, "bold"), bg="white", fg="MediumPurple3", bd=0, relief="flat").grid(row=0, column=4, sticky="nsew", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiPerfilPaciente(root)
    root.mainloop()
    
    
    
        Marco_principal = tk.Frame(self.canvas, bg="blue")
        Marco_principal.configure(width=400, height=650)
        Marco_principal.pack(pady=10)
        Marco_principal.pack_propagate(False)
        #MARCO TITULO 
            
        marco_actividades = tk.Frame(self.marco_principal, bg="lavender")
        marco_actividades.configure(width=400, height=80)
        marco_actividades.pack(pady=(15,5))
        marco_actividades.pack_propagate(False)
        
        texto_actividad = tk.Label(marco_actividades, text="Actividades")
        texto_actividad.configure(bg="lavender", fg="black", font=("Quicksand",25,"bold"))
        texto_actividad.pack(side="top", anchor="w")
        
        texto_info1 = tk.Label(marco_actividades, text="Elige una actividad para seguir avanzando")
        texto_info1.configure(bg="lavender", fg="dim gray", font=("Arial",15))
        texto_info1.pack(side="top", anchor="w")

        #MARCO MEMORAMA

        Marco_principal = tk.Frame(self.canvas, bg="blue")
        Marco_principal.configure(width=400, height=650)
        Marco_principal.pack(pady=10)
        Marco_principal.pack_propagate(False)

        marco_tarjeta_memorama = ctk.CTkFrame(Marco_principal)
        marco_tarjeta_memorama.configure(width=600,height=170,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_memorama.pack(pady=(0,20))
        marco_tarjeta_memorama.pack_propagate(False)
        
        self.crear_interfaz()

    def crear_interfaz(self):
            
        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="lavender", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

#BARRA DE SCROLL

        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical", command=self.canvas.yview)
        barra_scroll.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=barra_scroll.set)

# MARCO PRINCIPAL 

        self.marco_principal = tk.Frame(self.canvas)
        self.marco_principal.configure(bg="lavender")

        self.canvas.create_window((0,0), window=self.marco_principal, anchor="nw")

        self.marco_principal.bind(
            "<Configure>",
            lambda evento:
            self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        


        
        #MENÚ INFERIOR 
        
        marco_menu = tk.Frame(self.marco_principal)
        marco_menu.configure(width=600, height=80, bg="white", relief="solid", bd=1)
        marco_menu.pack(pady=(10,20))
        marco_menu.pack_propagate(False)

        #BOTÓN INICIO 

        boton_inicio = tk.Button(marco_menu, text="🏠\nInicio")
        boton_inicio.configure(bg="white", fg="dim gray", font=("Quicksand",12,"bold"), relief="flat", bd=0, command=self.abrir_inicio)
        boton_inicio.pack(side="left", expand=True)
        
        # BOTÓN ACTIVIDADES 

        boton_actividades = tk.Button(marco_menu, text="🧠\nActividades")
        boton_actividades.configure(bg="white", fg="medium purple", font=("Quicksand",12), relief="flat", bd=0)
        boton_actividades.pack(side="left", expand=True)

        #BOTÓN AVISOS 

        boton_avisos = tk.Button(marco_menu, text="🔔\nAvisos")
        boton_avisos.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_avisos)
        boton_avisos.pack(side="left", expand=True)

        #BOTÓN PERFIL

        boton_perfil = tk.Button(marco_menu, text="👤\nPerfil")
        boton_perfil.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_perfil)
        boton_perfil.pack(side="left", expand=True)
        

    def abrir_perfil(self):
        from perfil import usuario_perfil
        self.ventana.withdraw()
        usuario_perfil(self.ventana)

    def abrir_inicio(self):
        from principal_paciente import principal
        self.ventana.withdraw()
        principal(self.ventana)
        
    def abrir_avisos(self):
        from recuerdos import avisos
        self.ventana.withdraw()
        avisos(self.ventana)
        
        
        
        
        
        import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import random

# python NEUROCARE/funciones/memorama.py

class memorama:

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
        memorama(self.root)

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
    app = memorama(ventana)
    ventana.mainloop()
    
    
    #recordatorios
           #------------------------------------------------#
    #            TARJETA MEMORAMA                    #
    #------------------------------------------------#
    
            tarjeta_memorama = ctk.CTkFrame(
                self.contenedor,
                fg_color="white",
                corner_radius=25,
                height=100
            )
    
            tarjeta_memorama.pack(
                fill="x",
                pady=(0,15)
            )
    
            marco_icono1 = ctk.CTkFrame(
                tarjeta_memorama,
                width=55,
                height=55,
                corner_radius=28,
                fg_color="#EEE7FF"
            )
    
            marco_icono1.pack(
                side="left",
                padx=18,
                pady=18
            )
    
            marco_icono1.pack_propagate(False)
    
            tk.Label(
                marco_icono1,
                text="🧠",
                bg="#EEE7FF",
                font=("Segoe UI Emoji",20)
            ).pack(expand=True)
    
            marco_texto1 = tk.Frame(
                tarjeta_memorama,
                bg="white"
            )
    
            marco_texto1.pack(
                side="left",
                expand=True,
                anchor="w"
            )
    
            tk.Label(
                marco_texto1,
                text="Ejercicio de Memorama",
                bg="white",
                fg="black",
                font=("Quicksand",17,"bold")
            ).pack(anchor="w")
    
            tk.Label(
                marco_texto1,
                text="10:00 • Actividad",
                bg="white",
                fg="gray",
                font=("Quicksand",12)
            ).pack(anchor="w")
    
            boton_memorama = ctk.CTkButton(
                tarjeta_memorama,
                text="✓",
                width=45,
                height=45,
                corner_radius=22,
                fg_color="white",
                hover_color="#F5F5F5",
                text_color="#22C55E",
                border_width=2,
                border_color="#E5E7EB",
                font=("Arial",20,"bold")
            )   
    
            boton_memorama.pack(
                side="right",
                padx=20
            )
    