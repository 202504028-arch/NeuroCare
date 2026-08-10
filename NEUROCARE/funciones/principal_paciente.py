import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from conexion import conectarBd

                                #python NEUROCARE/funciones/principal_paciente.py
class principal:

    def __init__(self, root,idPaciente):

        self.root = root
        self.idPaciente=idPaciente
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- MENU PRINCIPAL")
        self.ventana.geometry("650x700+500+10")
        self.ventana.configure(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
      

        self.crear_interfaz()

    def crear_interfaz(self):

#CANVAS 

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
        
#ENCABEZADO

        marco_encabezado = tk.Frame(self.marco_principal)
        marco_encabezado.configure(width=600, height=70, bg="lavender")
        marco_encabezado.pack(pady=(15,15))
        marco_encabezado.pack_propagate(False)

        self.imagen_logo = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_logo = self.imagen_logo.subsample(5,5)

        etiqueta_logo = tk.Label(marco_encabezado, image=self.imagen_logo)
        etiqueta_logo.configure(bg="lavender")
        etiqueta_logo.pack(side="left", padx=(15,8))

        etiqueta_titulo = tk.Label(marco_encabezado, text="NEUROCARE")
        etiqueta_titulo.configure(fg="medium purple", bg="lavender", font=("Quicksand",20,"bold"))
        etiqueta_titulo.pack(side="left")
        
# BIENVENIDA 

        marco_bienvenida = tk.Frame(self.marco_principal)
        marco_bienvenida.configure(width=600, height=170, bg="lavender")
        marco_bienvenida.pack(pady=(5,20))
        marco_bienvenida.pack_propagate(False)

        marco_texto = tk.Frame(marco_bienvenida)
        marco_texto.configure(width=360, height=170, bg="lavender")
        marco_texto.pack(side="left", fill="y")
        marco_texto.pack_propagate(False)

        etiqueta_bienvenida = tk.Label(marco_texto, text="Bienvenido,")
        etiqueta_bienvenida.configure(bg="lavender", fg="black", font=("Quicksand",18,"bold"))
        etiqueta_bienvenida.pack(anchor="w", pady=(10,0), padx=10)

        conexion = conectarBd()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombreCompleto FROM paciente WHERE idPaciente = %s", (self.idPaciente,))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()


        etiqueta_nombre = tk.Label(marco_texto, text=resultado[0] if resultado else "usuario")  #👋
        etiqueta_nombre.configure(bg="lavender", fg="medium purple", font=("Quicksand",24,"bold"))
        etiqueta_nombre.pack(anchor="w", pady=(5,5), padx=10)

        etiqueta_descripcion = tk.Label(marco_texto, text=  "Estamos contigo en cada paso.\n  Aquí está tu resumen de hoy.")
        etiqueta_descripcion.configure(bg="lavender", fg="dim gray", font=("Quicksand",13))
        etiqueta_descripcion.pack(anchor="w", padx=11)

        marco_mascota = tk.Frame(marco_bienvenida)
        marco_mascota.configure(width=180, height=170, bg="lavender")
        marco_mascota.pack(side="right")
        marco_mascota.pack_propagate(False)

        self.imagen_mascota = tk.PhotoImage(file="NEUROCARE/funciones/recursos/mascota.png")
        self.imagen_mascota = self.imagen_mascota.subsample(7,7)

        etiqueta_mascota = tk.Label(marco_mascota, image=self.imagen_mascota)
        etiqueta_mascota.configure(bg="lavender")
        etiqueta_mascota.pack(expand=True)
        
# RESUMEN

        marco_resumen = tk.Frame(self.marco_principal)
        marco_resumen.configure(width=600, height=170, bg="lavender")
        marco_resumen.pack(pady=(5,20))
        marco_resumen.pack_propagate(False)

#ACTIVIDADES 

        marco_actividades = ctk.CTkFrame(marco_resumen,width=275, height=190, fg_color="#E9D5FF",corner_radius=30,
                                         border_width=1, border_color="#E9D5FF")
        marco_actividades.pack(side="left", padx=(10,15))
        marco_actividades.pack_propagate(False)

        marco_icono1 = tk.Frame(marco_actividades)
        marco_icono1.configure(width=65, height=65, bg="#E9D5FF")
        marco_icono1.pack(pady=(15,10))
        marco_icono1.pack_propagate(False)

        self.imagen_actividad = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_actividad = self.imagen_actividad.subsample(2,2)

        etiqueta_imagen1 = tk.Label(marco_icono1, image=self.imagen_actividad)
        etiqueta_imagen1.configure(bg="#E9D5FF")
        etiqueta_imagen1.pack(expand=True)

        etiqueta_numero1 = tk.Label(marco_actividades, text="aqui")
        etiqueta_numero1.configure(bg="yellow", fg="medium purple", font=("Quicksand",22,"bold"))
        etiqueta_numero1.pack()

        etiqueta_texto1 = tk.Label(marco_actividades, text="Actividades pendientes")
        etiqueta_texto1.configure(bg="#E9D5FF", fg="dim gray", font=("Quicksand",11))
        etiqueta_texto1.pack()

#RECORDATORIOS 
        marco_recordatorios = ctk.CTkFrame(marco_resumen,width=275,height=175,fg_color="#D1FAE5",
                                           corner_radius=30,border_width=1, border_color="#D1FAE5")
        marco_recordatorios.pack(side="right", padx=(15,10))
        marco_recordatorios.pack_propagate(False)

        marco_icono2 = tk.Frame(marco_recordatorios)
        marco_icono2.configure(width=65, height=65, bg="#D1FAE5")
        marco_icono2.pack(pady=(15,10))
        marco_icono2.pack_propagate(False)

        self.imagen_recordatorio = tk.PhotoImage(file="NEUROCARE/funciones/recursos/campana.png")
        self.imagen_recordatorio = self.imagen_recordatorio.subsample(2,2)

        etiqueta_imagen2 = tk.Label(marco_icono2, image=self.imagen_recordatorio)
        etiqueta_imagen2.configure(bg="#D1FAE5")
        etiqueta_imagen2.pack(expand=True)

        etiqueta_numero2 = tk.Label(marco_recordatorios, text="aqui")
        etiqueta_numero2.configure(bg="yellow", fg="medium purple", font=("Quicksand",22,"bold"))
        etiqueta_numero2.pack()

        etiqueta_texto2 = tk.Label(marco_recordatorios, text="Recordatorios pendientes")
        etiqueta_texto2.configure(bg="#D1FAE5", fg="dim gray", font=("Quicksand",11))
        etiqueta_texto2.pack()


        
#PROGRESO 

        marco_progreso = tk.Frame(self.marco_principal)
        marco_progreso.configure(width=600, height=100, bg="red")
        marco_progreso.pack(pady=(5,20))
        marco_progreso.pack_propagate(False)

        etiqueta_progreso = tk.Label(marco_progreso, text="Progreso del día")
        etiqueta_progreso.configure(bg="red", fg="black", font=("Quicksand",15,"bold"))
        etiqueta_progreso.pack(anchor="w")

        etiqueta_estado = tk.Label(marco_progreso, text="2 de 5 actividades completadas")
        etiqueta_estado.configure(bg="lavender", fg="dim gray", font=("Quicksand",11))
        etiqueta_estado.pack(anchor="w", pady=(2,8))

        barra_progreso = ttk.Progressbar(marco_progreso)
        barra_progreso.configure(length=560, maximum=5)

        barra_progreso["value"] = 2

        barra_progreso.pack(anchor="w")
        
        #BOTON SOS
        
        marco_sos = ctk.CTkFrame(self.marco_principal, fg_color="lavender")
        marco_sos.configure(width=550, height=70)
        marco_sos.pack(pady=(0, 10))
        marco_sos.pack_propagate(True)
        
        boton_sos = ctk.CTkButton(marco_sos,text="📞SOS📞\n    TOCA AQUI SI NECESITAS AYUDA    ",fg_color="red",corner_radius=25,border_width=3,
                                    border_color="red4", hover_color="red2",font=("Arial", 26, "bold"), command=self.mensaje_boton)
        boton_sos.pack(pady=5,padx=5)
        
#-------------------- TARJETA DE ACTIVIDADES --------------------#

        marco_tarjeta_actividades = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_actividades.configure(width=600,height=170,fg_color="white",
        corner_radius=25,border_width=3,border_color="medium purple")
        marco_tarjeta_actividades.pack(pady=(10,20))
        marco_tarjeta_actividades.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_actividad = tk.Frame(marco_tarjeta_actividades)
        contenedor_actividad.configure(bg="white")
        contenedor_actividad.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_actividad)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono_actividad = tk.Frame(marco_izquierdo)
        marco_icono_actividad.configure(width=100,height=100,bg="#E9D5FF",relief="solid",bd=1)
        marco_icono_actividad.pack(expand=True)
        marco_icono_actividad.pack_propagate(False)

        self.imagen_actividad2 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_actividad2 = self.imagen_actividad2.subsample(2,2)

        etiqueta_imagen_actividad = tk.Label(marco_icono_actividad,image=self.imagen_actividad2)
        etiqueta_imagen_actividad.configure(bg="#E9D5FF")
        etiqueta_imagen_actividad.pack(expand=True)

#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_actividad)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_actividad = tk.Label(marco_centro,text="Actividades")
        etiqueta_titulo_actividad.configure(bg="white",fg="medium purple",
        font=("Quicksand",22,"bold"))
        etiqueta_titulo_actividad.pack(anchor="w",pady=(15,5))

        etiqueta_descripcion_actividad = tk.Label(marco_centro,
        text="Ejercicios para mantener activa\nla memoria y la concentración.")
        etiqueta_descripcion_actividad.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_actividad.pack(anchor="w",)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_actividad)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_actividad = ctk.CTkButton(marco_derecho,text="-->",width=65,height=65,
        corner_radius=35,fg_color="#9370DB",hover_color="#7B3FE4",
        text_color="white",font=("Arial",28,"bold"),
        command=self.abrir_actividades)

        boton_actividad.pack(expand=True)

#-------------------- TARJETA DE RECORDATORIOS --------------------#

        marco_tarjeta_recordatorios = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_recordatorios.configure(width=600,height=170,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_recordatorios.pack(pady=(0,20))
        marco_tarjeta_recordatorios.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_recordatorio = tk.Frame(marco_tarjeta_recordatorios)
        contenedor_recordatorio.configure(bg="white")
        contenedor_recordatorio.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_recordatorio)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono_recordatorio = tk.Frame(marco_izquierdo)
        marco_icono_recordatorio.configure(width=100,height=100,bg="#D1FAE5",relief="solid",bd=1)
        marco_icono_recordatorio.pack(expand=True)
        marco_icono_recordatorio.pack_propagate(False)

        self.imagen_recordatorio2 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/campana.png")
        self.imagen_recordatorio2 = self.imagen_recordatorio2.subsample(3,3)

        etiqueta_imagen_recordatorio = tk.Label(marco_icono_recordatorio,image=self.imagen_recordatorio2)
        etiqueta_imagen_recordatorio.configure(bg="#D1FAE5")
        etiqueta_imagen_recordatorio.pack(expand=True)

#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_recordatorio)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_recordatorio = tk.Label(marco_centro,text="Recordatorios")
        etiqueta_titulo_recordatorio.configure(bg="white",fg="#22C55E",
        font=("Quicksand",22,"bold"))
        etiqueta_titulo_recordatorio.pack(anchor="w",pady=(25,5))

        etiqueta_descripcion_recordatorio = tk.Label(marco_centro,
        text="Organiza tus avisos y\nrecordatorios importantes.")
        etiqueta_descripcion_recordatorio.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_recordatorio.pack(anchor="w")

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_recordatorio)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_recordatorios = ctk.CTkButton(marco_derecho,text="-->",width=65,height=65,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"),
        command=self.abrir_recuerdos)

        boton_recordatorios.pack(expand=True)


#MENÚ INFERIOR 

        marco_menu = tk.Frame(self.marco_principal)
        marco_menu.configure(width=600, height=80, bg="white", relief="solid", bd=1)
        marco_menu.pack(pady=(10,20), padx=10)
        marco_menu.pack_propagate(False)

#BOTÓN INICIO 

        boton_inicio = tk.Button(marco_menu, text="🏠\nInicio")
        boton_inicio.configure(bg="white", fg="medium purple", font=("Quicksand",12,"bold"), relief="flat", bd=0)
        boton_inicio.pack(side="left", expand=True)

# BOTÓN ACTIVIDADES 

        boton_actividades = tk.Button(marco_menu, text="🧠\nActividades")
        boton_actividades.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_actividades)
        boton_actividades.pack(side="left", expand=True)

#BOTÓN AVISOS 

        boton_avisos = tk.Button(marco_menu, text="🔔\nAvisos")
        boton_avisos.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_recuerdos)
        boton_avisos.pack(side="left", expand=True)

#BOTÓN PERFIL

        boton_perfil = tk.Button(marco_menu, text="👤\nPerfil")
        boton_perfil.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_perfil)
        boton_perfil.pack(side="left", expand=True)

   
    
    def mensaje_boton(self):
        messagebox.showinfo(
            "‼️SOS - Emergencia‼️",
            "🛑📞Realizando llamada al \ncontacto de emergencia...📞🛑"
        )
        
    def abrir_actividades(self):
        from actividades import juegos

        self.ventana.withdraw()

        juegos(
                self.ventana,
                self.idPaciente
        )

    def abrir_recuerdos(self):
        from recordatorios import recordatorios1

        self.ventana.withdraw()

        recordatorios1(
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

if __name__ =="__main__":
    ventana = tk.Tk()

    idPaciente = 1

    app = principal(
        ventana,
        idPaciente
    )

    ventana.mainloop()
    