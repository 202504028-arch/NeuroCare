
from tkinter import messagebox
from conexion import conectarBd
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

                                    #python NEUROCARE/funciones/perfil.py
class usuario_perfil:
    
    def __init__ (self,root):
            self.root = root
            self.ventana = tk.Toplevel(root)
        

            self.ventana.title(" NEUROCARE -- PERFIL")
            self.ventana.geometry("650x700+500+10")
            self.ventana.config(bg="lavender")

            self.ventana.minsize(False,False)
            self.ventana.maxsize(False,False)
            self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
            
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
        
        #MI PROGRESO
        
        marco_encabezado = tk.Frame(self.marco_principal)
        marco_encabezado.configure(width=600, height=70, bg="lavender")
        marco_encabezado.pack(pady=(15,5), padx=20)
        marco_encabezado.pack_propagate(False)

        etiqueta_titulo = tk.Label(marco_encabezado, text="Mi progreso")
        etiqueta_titulo.configure(fg="black", bg="lavender", font=("Quicksand",20,"bold"))
        etiqueta_titulo.pack(side="left")
        
        #CUADRADO INFORMATIVO
        marco_paciente = tk.Frame(self.marco_principal)
        marco_paciente.configure(width=600, height=120, bg="purple")
        marco_paciente.pack(pady=(15,0))
        marco_paciente.pack_propagate(False)
        
        #IMAGEN
        marco_izquierdo = tk.Frame(marco_paciente)
        marco_izquierdo.configure(width=120,
        height=130,bg="purple")
        
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)
        
        marco_icono_perfil = ctk.CTkFrame(marco_izquierdo)
        marco_icono_perfil.configure(width=90,height=90,
        fg_color="#E9D5FF",corner_radius=45)

        marco_icono_perfil.pack(expand=True)
        marco_icono_perfil.pack_propagate(False)

        self.imagen_perfil = tk.PhotoImage(file="NEUROCARE/funciones/recursos/tarjeta de identificacion.png")
        self.imagen_perfil = self.imagen_perfil.subsample(3,3)

        etiqueta_imagen_perfil = tk.Label(
        marco_icono_perfil,
        image=self.imagen_perfil)

        etiqueta_imagen_perfil.configure(bg="#E9D5FF")
        etiqueta_imagen_perfil.pack(expand=True)
        
        #TEXTO
        marco_centro = tk.Frame(marco_paciente)
        marco_centro.configure(bg="purple")

        marco_centro.pack(side="left",
        fill="both",expand=True,padx=(20,10))
        
        etiqueta_titulo = tk.Label(marco_centro,
        text="PACIENTE NUEROCARE")
        etiqueta_titulo.configure(bg="purple",fg="white",font=("Quicksand",18,))
        etiqueta_titulo.pack(anchor="w",pady=(10,0))

        etiqueta_descripcion = tk.Label(marco_centro,text="nombre del paciente")
        etiqueta_descripcion.configure(bg="red",fg="white",font=("Quicksand",25, "bold"),justify="left")
        etiqueta_descripcion.pack(anchor="w",pady=(0,4))
        
        

        marco_paciente1 = tk.Frame(self.marco_principal)
        marco_paciente1.configure(width=600, height=300, bg="white")
        marco_paciente1.pack(pady=(0,10))
        marco_paciente1.pack_propagate(False)
                                                 #los que tienen fondo amariillo es donde vas a jalar lo que ponga el usuario en el registro, donde dice aqui
# ==========================
# FILA MÉDICA 1
# ==========================

        marco_fila1 = tk.Frame(marco_paciente1, bg="red")
        marco_fila1.configure(width=560, height=120)
        marco_fila1.pack(pady=(0, 10))
        marco_fila1.pack_propagate(False)


# --------------------------
# Sangre
# --------------------------

        marco_tipo_sangre = tk.Frame(marco_fila1, bg="blue")
        marco_tipo_sangre.configure(width=250, height=100)
        marco_tipo_sangre.pack(side="left", padx=10, pady=(10,10))
        marco_tipo_sangre.pack_propagate(False)
        
        etiqueta_sangre = tk.Label(marco_tipo_sangre, text="Tipo de sangre")
        etiqueta_sangre.configure(fg="black", bg="lavender", font=("Arial", 24,))
        etiqueta_sangre.pack(side="top", anchor="w")
        
        etiqueta_sangre1 =tk.Label(marco_tipo_sangre, text="aqui")
        etiqueta_sangre1.configure(fg="dim gray", bg="yellow", font=("Arial",18))
        etiqueta_sangre1.pack(side="top", anchor="w", pady=10, padx=5)
        etiqueta_sangre1.pack_propagate(True)
        
# --------------------------
# Alergias
# --------------------------

        marco_alergias = tk.Frame(marco_fila1, bg="blue")
        marco_alergias.configure(width=250, height=100)
        marco_alergias.pack(side="right", padx=10, pady=(10,10))
        marco_alergias.pack_propagate(False)

        etiqueta_alergias = tk.Label(marco_alergias, text="Alergias")
        etiqueta_alergias.configure(fg="black", bg="lavender", font=("Arial", 24,))
        etiqueta_alergias.pack(side="top", anchor="w",)
        
        etiqueta_alergia1 =tk.Label(marco_alergias, text="aqui")
        etiqueta_alergia1.configure(fg="dim gray", bg="yellow", font=("Arial",18))
        etiqueta_alergia1.pack(side="top", anchor="w", pady=10, padx=5)
        etiqueta_alergia1.pack_propagate(True)


# ==========================
# FILA MÉDICA 2
# ==========================

        marco_fila2 = tk.Frame(marco_paciente1, bg="red")
        marco_fila2.configure(width=560, height=100)
        marco_fila2.pack(pady=(0, 10))
        marco_fila2.pack_propagate(False)


# --------------------------
# emergencia
# --------------------------

        marco_contacto_emergencia = tk.Frame(marco_fila2, bg="blue")
        marco_contacto_emergencia.configure(width=250, height=100)
        marco_contacto_emergencia.pack(side="left", padx=10, pady=(10,10))
        marco_contacto_emergencia.pack_propagate(False)
        
        etiqueta_contacto_emergencia = tk.Label(marco_contacto_emergencia, text="Contacto de emergencia")
        etiqueta_contacto_emergencia.configure(fg="black", bg="lavender", font=("Arial", 17,))
        etiqueta_contacto_emergencia.pack(side="top", anchor="w")
        
        etiqueta_contacto1 =tk.Label(marco_contacto_emergencia, text="aqui")
        etiqueta_contacto1.configure(fg="dim gray", bg="yellow", font=("Arial",16))
        etiqueta_contacto1.pack(side="top", anchor="w", pady=10, padx=5)
        etiqueta_contacto1.pack_propagate(True)
        

# --------------------------
# enfermedad cronica
# --------------------------

        marco_enfermedad = tk.Frame(marco_fila2, bg="blue")
        marco_enfermedad.configure(width=250, height=100)
        marco_enfermedad.pack(side="right", padx=10, pady=(10,10))
        marco_enfermedad.pack_propagate(False)

        etiqueta_enfermedad = tk.Label(marco_enfermedad, text="Enfermedad cronica")
        etiqueta_enfermedad.configure(fg="black", bg="lavender", font=("Arial", 20,))
        etiqueta_enfermedad.pack(side="top", anchor="w",)
        
        etiqueta_enfermedad1 =tk.Label(marco_enfermedad, text="aqui")
        etiqueta_enfermedad1.configure(fg="dim gray", bg="yellow", font=("Arial",16))
        etiqueta_enfermedad1.pack(side="top", anchor="w", pady=10, padx=5)
        etiqueta_enfermedad1.pack_propagate(True)


        marco_boton = tk.Frame(marco_paciente1, bg="white")
        marco_boton.configure(width=2000, height=60)
        marco_boton.pack(pady=(0, 10), side="bottom", anchor="e")
        marco_boton.pack_propagate(False)
        #aqui vas a agregar la funcion de actualizar, eliminar y agregar informacion
        #las funciones van hasta abajo y solo las jalas con   command=
                
        boton_informacion = ctk.CTkButton(marco_boton,text="editar informacion",fg_color="blue",corner_radius=25,border_width=3,
                                    border_color="blue2", font=("Arial", 20, "bold")) 
        boton_informacion.pack(pady=5, padx=5)

        #resumen
        
        marco_resumen_semanal = tk.Frame(self.marco_principal)
        marco_resumen_semanal.configure(width=600, height=50, bg="lavender")
        marco_resumen_semanal.pack(pady=(5,2))
        marco_resumen_semanal.pack_propagate(False)
        
        etiqueta_resumen = tk.Label(marco_resumen_semanal, text="Resumen semanal")
        etiqueta_resumen.configure(fg="black", bg="lavender", font=("Quicksand",20,"bold"))
        etiqueta_resumen.pack(anchor="center")
        
        marco_resumen = tk.Frame(self.marco_principal)
        marco_resumen.configure(width=600, height=170, bg="lavender")
        marco_resumen.pack(pady=(5,20))
        marco_resumen.pack_propagate(False)
        
        #ACTIVIDADES                            #igual vas a jalar depenediendo las actividades y cosas pendiente donde esta el aqui

        marco_actividades = ctk.CTkFrame(marco_resumen,width=275, height=190, fg_color="#D1FAE5",corner_radius=30,
                                         border_width=1, border_color="#D1FAE5")
        marco_actividades.pack(side="left", padx=(10,15))
        marco_actividades.pack_propagate(False)

        marco_icono1 = tk.Frame(marco_actividades)
        marco_icono1.configure(width=65, height=65, bg="#D1FAE5")   
        marco_icono1.pack(pady=(15,10))
        marco_icono1.pack_propagate(False)

        self.imagen_actividad = tk.PhotoImage(file="NEUROCARE/funciones/recursos/palomita.png")
        self.imagen_actividad = self.imagen_actividad.subsample(2,2)

        etiqueta_imagen1 = tk.Label(marco_icono1, image=self.imagen_actividad)
        etiqueta_imagen1.configure(bg="#D1FAE5")    
        etiqueta_imagen1.pack(expand=True)

        etiqueta_numero1 = tk.Label(marco_actividades, text="aqui")
        etiqueta_numero1.configure(bg="yellow", fg="medium purple", font=("Quicksand",22,"bold"))
        etiqueta_numero1.pack()

        etiqueta_texto1 = tk.Label(marco_actividades, text="Actividades completadas")
        etiqueta_texto1.configure(bg="#D1FAE5", fg="dim gray", font=("Quicksand",11))
        etiqueta_texto1.pack()

#RECORDATORIOS 
        marco_recordatorios = ctk.CTkFrame(marco_resumen,width=275,height=175,fg_color="#E9D5FF",
                                           corner_radius=30,border_width=1, border_color="#E9D5FF")
        marco_recordatorios.pack(side="right", padx=(15,10))
        marco_recordatorios.pack_propagate(False)

        marco_icono2 = tk.Frame(marco_recordatorios)
        marco_icono2.configure(width=65, height=65, bg="#E9D5FF")
        marco_icono2.pack(pady=(15,10))
        marco_icono2.pack_propagate(False)

        self.imagen_recordatorio = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_recordatorio = self.imagen_recordatorio.subsample(2,2)

        etiqueta_imagen2 = tk.Label(marco_icono2, image=self.imagen_recordatorio)
        etiqueta_imagen2.configure(bg="#E9D5FF")
        etiqueta_imagen2.pack(expand=True)

        etiqueta_numero2 = tk.Label(marco_recordatorios, text="aqui")
        etiqueta_numero2.configure(bg="yellow", fg="medium purple", font=("Quicksand",22,"bold"))
        etiqueta_numero2.pack()

        etiqueta_texto2 = tk.Label(marco_recordatorios, text="Ejercicios pendientes")
        etiqueta_texto2.configure(bg="#E9D5FF", fg="dim gray", font=("Quicksand",11))
        etiqueta_texto2.pack()

        
        
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
        boton_actividades.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_actividades)
        boton_actividades.pack(side="left", expand=True)

#BOTÓN AVISOS 

        boton_avisos = tk.Button(marco_menu, text="🔔\nAvisos")
        boton_avisos.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_avisos)
        boton_avisos.pack(side="left", expand=True)

#BOTÓN PERFIL

        boton_perfil = tk.Button(marco_menu, text="👤\nPerfil")
        boton_perfil.configure(bg="white", fg="medium purple", font=("Quicksand",12), relief="flat", bd=0)
        boton_perfil.pack(side="left", expand=True)
        
        boton_salir = ctk.CTkButton(self.marco_principal, text="👤 Cerrar sesion",fg_color="red",corner_radius=25,border_width=3,
                                    border_color="red2", command=self.volver_menu)
        boton_salir.pack()

    def abrir_actividades(self):
        from actividades import juegos
        self.ventana.withdraw()
        juegos(self.ventana)

    def abrir_inicio(self):
        from principal_paciente import principal
        self.ventana.withdraw()
        principal(self.ventana)
        
    def abrir_avisos(self):
        from recordatorios import recordatorios1
        self.ventana.withdraw()
        recordatorios1(self.ventana)
        
    def volver_menu(self):
        respuesta= messagebox.askyesno(
            "Cerrar sesion",
            "¿Quieres salir de tu cuenta?"
        )
        
        if respuesta:
            messagebox.showinfo(
                "Hasta pronto",
                "Vuelva pronto👋"
            )
        
        from inicio_sesion import iniciar_sesion
        self.ventana.destroy()
        iniciar_sesion(self.root)                                                  
 

if __name__ =="__main__":
    ventana = tk.Tk()
    app = usuario_perfil(ventana)
    ventana.mainloop()
    