import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from conexion import conectarBd
import tkinter as tk

                        #python NEUROCARE/funciones/actividades.py

class juegos:

    def __init__(self, root, idPaciente):

        self.root = root
        self.idPaciente = idPaciente
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- ACTIVIDADES")
        self.ventana.geometry("520x700+520+60")
        self.ventana.config(bg="lavender")
        self.ventana.attributes("-alpha")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)

        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")

        self.crear_interfaz()

    def crear_interfaz(self):

#-------------------- CANVAS --------------------#

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="lavender",highlightthickness=0)
        self.canvas.pack(side="left",fill="both",expand=True)

#-------------------- SCROLL --------------------#

        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical",command=self.canvas.yview)
        barra_scroll.pack(side="right",fill="y")

        self.canvas.configure(yscrollcommand=barra_scroll.set)

#-------------------- MARCO PRINCIPAL --------------------#

        self.marco_principal = tk.Frame(self.canvas)
        self.marco_principal.configure(bg="lavender")

        self.ventana.update_idletasks()

        self.canvas.create_window(
            (0,0),
            window=self.marco_principal,
            anchor="nw",
            width=500
        )

        self.marco_principal.bind(
            "<Configure>",
            lambda evento:
            self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))

#-------------------- CONTENEDOR --------------------#

        marco_contenedor = tk.Frame(self.marco_principal)
        marco_contenedor.configure(width=480,height=820,
        bg="lavender")

        marco_contenedor.pack(pady=10, padx=10)
        marco_contenedor.pack_propagate(False)

#-------------------- TITULO --------------------#

        marco_titulo = tk.Frame(marco_contenedor)
        marco_titulo.configure(width=480,height=80,bg="lavender")
        marco_titulo.pack(pady=(15,10))
        marco_titulo.pack_propagate(False)

        etiqueta_titulo = tk.Label(marco_titulo,text="Actividades")

        etiqueta_titulo.configure(bg="lavender",fg="black",font=("Quicksand",26,"bold"))
        etiqueta_titulo.pack(anchor="w")


        etiqueta_descripcion = tk.Label(marco_titulo,text="Elige una actividad para seguir avanzando.")
        etiqueta_descripcion.configure(bg="lavender",fg="dim gray",font=("Quicksand",13))
        etiqueta_descripcion.pack(anchor="w")
        
#-------------------- TARJETA MEMORAMA --------------------#

        marco_tarjeta_memorama = ctk.CTkFrame(marco_contenedor)
        marco_tarjeta_memorama.configure(width=480,height=180,
        fg_color="white",corner_radius=25,
        border_width=3,border_color="#801AEE")

        marco_tarjeta_memorama.pack(pady=(0,20))
        marco_tarjeta_memorama.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_memorama = tk.Frame(marco_tarjeta_memorama)
        contenedor_memorama.configure(bg="white")

        contenedor_memorama.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo_memorama = tk.Frame(contenedor_memorama)
        marco_izquierdo_memorama.configure(width=120,
        height=130,bg="white")

        marco_izquierdo_memorama.pack(side="left")
        marco_izquierdo_memorama.pack_propagate(False)

        marco_icono_memorama = ctk.CTkFrame(marco_izquierdo_memorama)
        marco_icono_memorama.configure(width=90,height=90,
        fg_color="#E9D5FF",corner_radius=45)

        marco_icono_memorama.pack(expand=True)
        marco_icono_memorama.pack_propagate(False)

        self.imagen_memorama = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_memorama = self.imagen_memorama.subsample(3,3)

        etiqueta_imagen_memorama = tk.Label(
        marco_icono_memorama,image=self.imagen_memorama)

        etiqueta_imagen_memorama.configure(bg="#E9D5FF")
        etiqueta_imagen_memorama.pack(expand=True)

#-------------------- MARCO CENTRO --------------------#

        marco_centro_memorama = tk.Frame(contenedor_memorama)
        marco_centro_memorama.configure(bg="white")

        marco_centro_memorama.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_categoria_memorama = tk.Label(marco_centro_memorama,text="COGNITIVA")
        etiqueta_categoria_memorama.configure(bg="#E9D5FF",fg="#7C3AED",font=("Quicksand",10,"bold"))
        etiqueta_categoria_memorama.pack(anchor="w")

        etiqueta_titulo_memorama = tk.Label(marco_centro_memorama,text="Memorama")
        etiqueta_titulo_memorama.configure(bg="white",fg="#E9D5FF",font=("Quicksand",22,"bold"))
        etiqueta_titulo_memorama.pack(anchor="w",pady=(8,5))

        etiqueta_descripcion_memorama = tk.Label(marco_centro_memorama,
        text="Encuentra las parejas iguales\ny ejercita tu memoria.")
        etiqueta_descripcion_memorama.configure(bg="white",fg="dim gray",font=("Quicksand",12),justify="left")
        etiqueta_descripcion_memorama.pack(anchor="w",pady=(0,10))

        etiqueta_progreso_memorama = tk.Label(marco_centro_memorama,text="Progreso: 0%")
        etiqueta_progreso_memorama.configure(bg="white",fg="dim gray",font=("Quicksand",11))
        etiqueta_progreso_memorama.pack(anchor="w")

        barra_memorama = ctk.CTkProgressBar(marco_centro_memorama,width=180)
        barra_memorama.pack(anchor="w",pady=(5,0))
        barra_memorama.set(0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho_memorama = tk.Frame(contenedor_memorama)
        marco_derecho_memorama.configure(width=110,height=130,bg="white")
        marco_derecho_memorama.pack(side="right")
        marco_derecho_memorama.pack_propagate(False)

        boton_memorama = ctk.CTkButton(marco_derecho_memorama,text="-->",width=65,height=65,
            corner_radius=20,fg_color="#E9D5FF",hover_color="#E9D5FF",text_color="white",
            font=("Arial",20,"bold"),command=self.abrir_memorama)
        boton_memorama.pack(expand=True)
        
#-------------------- TARJETA ROMPECABEZAS --------------------#

        marco_tarjeta_rompecabezas = ctk.CTkFrame(marco_contenedor)
        marco_tarjeta_rompecabezas.configure(width=480,height=180,fg_color="white",corner_radius=25,
        border_width=3,border_color="#3B82F6")

        marco_tarjeta_rompecabezas.pack(pady=(0,20))
        marco_tarjeta_rompecabezas.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_rompecabezas = tk.Frame(marco_tarjeta_rompecabezas)
        contenedor_rompecabezas.configure(bg="white")

        contenedor_rompecabezas.pack(fill="both",
        expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo_rompecabezas = tk.Frame(contenedor_rompecabezas)
        marco_izquierdo_rompecabezas.configure(width=120,
        height=130,bg="white")

        marco_izquierdo_rompecabezas.pack(side="left")
        marco_izquierdo_rompecabezas.pack_propagate(False)

        marco_icono_rompecabezas = ctk.CTkFrame(marco_izquierdo_rompecabezas)
        marco_icono_rompecabezas.configure(width=90,height=90,
        fg_color="#DBEAFE",corner_radius=45)

        marco_icono_rompecabezas.pack(expand=True)
        marco_icono_rompecabezas.pack_propagate(False)

        self.imagen_rompecabezas = tk.PhotoImage(file="NEUROCARE/funciones/recursos/rompecabezas.png")
        self.imagen_rompecabezas = self.imagen_rompecabezas.subsample(3,3)

        etiqueta_imagen_rompecabezas = tk.Label(
        marco_icono_rompecabezas,
        image=self.imagen_rompecabezas)

        etiqueta_imagen_rompecabezas.configure(bg="#DBEAFE")
        etiqueta_imagen_rompecabezas.pack(expand=True)

#-------------------- MARCO CENTRO --------------------#

        marco_centro_rompecabezas = tk.Frame(contenedor_rompecabezas)
        marco_centro_rompecabezas.configure(bg="white")

        marco_centro_rompecabezas.pack(side="left",
        fill="both",expand=True,padx=(20,10))

        etiqueta_categoria_rompecabezas = tk.Label(marco_centro_rompecabezas,text="COGNITIVA")
        etiqueta_categoria_rompecabezas.configure(bg="#DBEAFE",fg="#7C3AED",font=("Quicksand",10,"bold"))
        etiqueta_categoria_rompecabezas.pack(anchor="w")

        etiqueta_titulo_rompecabezas = tk.Label(marco_centro_rompecabezas,text="Rompecabezas")
        etiqueta_titulo_rompecabezas.configure(bg="white",fg="#3B82F6",font=("Quicksand",22,"bold"))
        etiqueta_titulo_rompecabezas.pack(anchor="w",pady=(8,5))

        etiqueta_descripcion_rompecabezas = tk.Label(
        marco_centro_rompecabezas,
        text="Arma una imagen por piezas\ny mejora tu concentración.")

        etiqueta_descripcion_rompecabezas.configure(bg="white",fg="dim gray",font=("Quicksand",12),justify="left")
        etiqueta_descripcion_rompecabezas.pack(anchor="w",pady=(0,10))

        etiqueta_progreso_rompecabezas = tk.Label(marco_centro_rompecabezas,text="Progreso: 0%")

        etiqueta_progreso_rompecabezas.configure(bg="white",fg="dim gray",font=("Quicksand",11))
        etiqueta_progreso_rompecabezas.pack(anchor="w")

        barra_rompecabezas = ctk.CTkProgressBar(
        marco_centro_rompecabezas,width=180)

        barra_rompecabezas.pack(anchor="w",pady=(5,0))
        barra_rompecabezas.set(0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho_rompecabezas = tk.Frame(
        contenedor_rompecabezas)

        marco_derecho_rompecabezas.configure(width=110,height=130,bg="white")
        marco_derecho_rompecabezas.pack(side="right")
        marco_derecho_rompecabezas.pack_propagate(False)

        boton_rompecabezas = ctk.CTkButton(
        marco_derecho_rompecabezas,text="-->",width=65,height=65,corner_radius=20,fg_color="#3B82F6",
        hover_color="#2563EB",text_color="white",font=("Arial",20,"bold"),command=self.abrir_rompecabezas)
        boton_rompecabezas.pack(expand=True)
        
#-------------------- TARJETA EJERCICIOS FÍSICOS --------------------#

        marco_tarjeta_ejercicios = ctk.CTkFrame(marco_contenedor)
        marco_tarjeta_ejercicios.configure(width=480,height=180,fg_color="white",corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_ejercicios.pack(pady=(0,20))
        marco_tarjeta_ejercicios.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_ejercicios = tk.Frame(marco_tarjeta_ejercicios)
        contenedor_ejercicios.configure(bg="white")

        contenedor_ejercicios.pack(fill="both",
        expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#     #python NEUROCARE/funciones/actividades.py

        marco_izquierdo_ejercicios = tk.Frame(contenedor_ejercicios)
        marco_izquierdo_ejercicios.configure(width=120,
        height=130,bg="white")

        marco_izquierdo_ejercicios.pack(side="left")
        marco_izquierdo_ejercicios.pack_propagate(False)

        marco_icono_ejercicios = ctk.CTkFrame(marco_izquierdo_ejercicios)
        marco_icono_ejercicios.configure(width=90,height=90,
        fg_color="#EAF8F0",corner_radius=45)

        marco_icono_ejercicios.pack(expand=True)
        marco_icono_ejercicios.pack_propagate(False)

        self.imagen_ejercicios = tk.PhotoImage(file="NEUROCARE/funciones/recursos/ejercicio.png")
        self.imagen_ejercicios = self.imagen_ejercicios.subsample(3,3)

        etiqueta_imagen_ejercicios = tk.Label(
        marco_icono_ejercicios,
        image=self.imagen_ejercicios)

        etiqueta_imagen_ejercicios.configure(bg="#EAF8F0")
        etiqueta_imagen_ejercicios.pack(expand=True)

#-------------------- MARCO CENTRO --------------------#

        marco_centro_ejercicios = tk.Frame(contenedor_ejercicios)
        marco_centro_ejercicios.configure(bg="white")

        marco_centro_ejercicios.pack(side="left",
        fill="both",expand=True,padx=(20,10))

        etiqueta_categoria_ejercicios = tk.Label(
        marco_centro_ejercicios,
        text="FÍSICA")

        etiqueta_categoria_ejercicios.configure(bg="#DDF4E7",fg="#4CAF7D",font=("Quicksand",10,"bold"))
        etiqueta_categoria_ejercicios.pack(anchor="w")

        etiqueta_titulo_ejercicios = tk.Label(
        marco_centro_ejercicios,
        text="Ejercicios físicos")

        etiqueta_titulo_ejercicios.configure(bg="white",fg="#4CAF7D",font=("Quicksand",20,"bold"))
        etiqueta_titulo_ejercicios.pack(anchor="w",pady=(8,5))
        
        etiqueta_descripcion_ejercicios = tk.Label(
        marco_centro_ejercicios,text="Realiza movimientos suaves\ny mejora tu movilidad.")

        etiqueta_descripcion_ejercicios.configure(bg="white",fg="dim gray",font=("Quicksand",12),justify="left")
        etiqueta_descripcion_ejercicios.pack(anchor="w",pady=(0,10))

        etiqueta_progreso_ejercicios = tk.Label(
        marco_centro_ejercicios,
        text="Progreso: 0%")

        etiqueta_progreso_ejercicios.configure(bg="white",fg="dim gray",font=("Quicksand",11))

        etiqueta_progreso_ejercicios.pack(anchor="w")

        barra_ejercicios = ctk.CTkProgressBar(
        marco_centro_ejercicios,
        width=180)

        barra_ejercicios.pack(anchor="w",pady=(5,0))
        barra_ejercicios.set(0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho_ejercicios = tk.Frame(
        contenedor_ejercicios)

        marco_derecho_ejercicios.configure(width=110,height=130,bg="white")

        marco_derecho_ejercicios.pack(side="right")
        marco_derecho_ejercicios.pack_propagate(False)

        boton_ejercicios = ctk.CTkButton(
        marco_derecho_ejercicios,text="-->",width=65,height=65,corner_radius=20,
        fg_color="#4CAF7D",hover_color="#4CAF7D",text_color="white",font=("Arial",20,"bold"),command=self.abrir_ejercicios)
        boton_ejercicios.pack(expand=True)
        
#-------------------- MENÚ INFERIOR --------------------#

        marco_menu = tk.Frame(marco_contenedor)
        marco_menu.configure(width=480,height=80,
        bg="white",relief="solid",bd=1)

        marco_menu.pack(pady=(10,20))
        marco_menu.pack_propagate(False)

#-------------------- BOTÓN INICIO --------------------#

        boton_inicio = tk.Button(marco_menu,text="🏠\nInicio")
        boton_inicio.configure(bg="white",fg="dim gray",font=("Quicksand",12,"bold"),relief="flat",bd=0,command=self.abrir_inicio)
        boton_inicio.pack(side="left",expand=True)

#-------------------- BOTÓN ACTIVIDADES --------------------#

        boton_actividades = tk.Button(marco_menu,text="🧠\nActividades")
        boton_actividades.configure(bg="white",fg="medium purple",font=("Quicksand",12,"bold"),relief="flat",bd=0)
        boton_actividades.pack(side="left",expand=True)

#-------------------- BOTÓN AVISOS --------------------#

        boton_avisos = tk.Button(marco_menu,text="🔔\nAvisos")
        boton_avisos.configure(bg="white",fg="dim gray",font=("Quicksand",12,"bold"),
        relief="flat",bd=0,command=self.abrir_avisos)
        boton_avisos.pack(side="left",expand=True)

#-------------------- BOTÓN PERFIL --------------------#

        boton_perfil = tk.Button(marco_menu,text="👤\nPerfil")
        boton_perfil.configure(bg="white",fg="dim gray",font=("Quicksand",12,"bold"),relief="flat",bd=0,
        command=self.abrir_perfil)
        boton_perfil.pack(side="left",expand=True)

#======================================================#
#                     FUNCIONES                        #
#======================================================#

    def abrir_memorama(self):
        from memorama import memoramaa

        self.ventana.withdraw()

        memoramaa(
            self.ventana,
            self.idPaciente
        )

    def abrir_rompecabezas(self):

        from rompecabezas import Rompecabezas

        self.ventana.withdraw()

        Rompecabezas(
            self.ventana,
            self.idPaciente
        )
        
    def abrir_ejercicios(self):

        from fisica import ejercicios_fisicos

        self.ventana.withdraw()

        ejercicios_fisicos(
            self.ventana,
            self.idPaciente
        )

    def abrir_perfil(self):

        from perfil import usuario_perfil

        self.ventana.withdraw()

        usuario_perfil(
            self.ventana,
            self.idPaciente
        )

    def abrir_inicio(self):

        from principal_paciente import principal

        self.ventana.withdraw()

        principal(
            self.ventana,
            self.idPaciente
        )   

    def abrir_avisos(self):

        from recordatorios import recordatorios1

        self.ventana.withdraw()

        recordatorios1(
            self.ventana,
            self.idPaciente
        )


if __name__ =="__main__":

    ventana = tk.Tk()
    ventana.withdraw()

    idPaciente = 1

    app = juegos(
        ventana,
        idPaciente
    )

    ventana.mainloop()