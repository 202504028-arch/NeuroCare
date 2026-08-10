import tkinter as tk
import customtkinter as ctk
from conexion import conectarBd
from tkinter import ttk
#python NEUROCARE/funciones/recordatorios.py

class recordatorios_actividadees:

    def __init__(self, root, id_paciente):

        self.root = root
        self.id_paciente = id_paciente
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- RECORDATORIOS")
        self.ventana.geometry("640x700+500+10")
        self.ventana.config(bg="lavender")

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


#------------------------------------------------#
#                  CABECERA                      #
#------------------------------------------------#

        marco_superior = tk.Frame(self.marco_principal,bg="lavender")
        marco_superior.pack(fill="x",padx=20,pady=(20,10))


#------------------------------------------------#
#                  TITULO                        #
#------------------------------------------------#

        marco_titulo = tk.Frame(marco_superior,bg="lavender")
        marco_titulo.pack(side="left",expand=True,padx=10)

        tk.Label(marco_titulo,text="Avisos",bg="lavender",fg="black",font=("Quicksand",26,"bold")).pack(anchor="w")
        tk.Label(marco_titulo,text="Recordatorios de hoy",bg="lavender",fg="dim gray",font=("Quicksand",13)).pack(anchor="w")

#------------------------------------------------#
#              BOTON AGREGAR                     #
#------------------------------------------------#

        boton_agregar = ctk.CTkButton(marco_superior,text="+",width=50,height=50,corner_radius=25,
            fg_color="#7C3AED",hover_color="#6D28D9",font=("Arial",28,"bold"))
        boton_agregar.pack(side="right")

#------------------------------------------------#
#                 FILTROS                        #
#------------------------------------------------#

        marco_filtros = tk.Frame(self.marco_principal,bg="lavender")

        marco_filtros.pack(fill="x",padx=20,pady=(5,20))

        self.btn_todos = ctk.CTkButton(marco_filtros,text="Todos",width=120,height=42,corner_radius=20,
                                       fg_color="white",hover_color="#6D28D9",text_color="black",
                                       font=("Quicksand",15),command=self.recordatorios_todos)
        self.btn_todos.pack(side="left", padx=(40,30))

        self.btn_actividad = ctk.CTkButton(marco_filtros,text="Actividades",width=140,height=42,corner_radius=20,
                                           fg_color="#7C3AED",hover_color="#6D28D9",text_color="black",border_width=2,border_color="#DDDDDD",font=("Quicksand",15,"bold"))
        self.btn_actividad.pack(side="left", padx=(30,30))
        
        self.btn_medicos = ctk.CTkButton(marco_filtros,text="Medicos",width=140,height=42,corner_radius=20,
                                           fg_color="white",hover_color="#6D28D9",text_color="black",border_width=2,border_color="#DDDDDD",
                                           font=("Quicksand",15), command=self.recordatorios_medicos)
        self.btn_medicos.pack(side="left", padx=(20,40))

#------------------------------------------------#
#        CONTENEDOR RECORDATORIOS                #
#------------------------------------------------#

        self.contenedor = tk.Frame(self.marco_principal,bg="red")
        self.contenedor.configure(height=350)
        self.contenedor.pack(fill="both",expand=True,padx=20,pady=10)
        
#MENÚ INFERIOR 

        marco_menu = tk.Frame(self.marco_principal)
        marco_menu.configure(width=600, height=80, bg="white", relief="solid", bd=1)
        marco_menu.pack(pady=(10,20), padx=10)
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
        boton_avisos.configure(bg="white", fg="medium purple", font=("Quicksand",12), relief="flat", bd=0 )
        boton_avisos.pack(side="left", expand=True)

#BOTÓN PERFIL

        boton_perfil = tk.Button(marco_menu, text="👤\nPerfil")
        boton_perfil.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_perfil)
        boton_perfil.pack(side="left", expand=True)
        
 
#FUNCIONES

    def abrir_actividades(self):
        from actividades import juegos
        self.ventana.withdraw()
        juegos(self.ventana , self.id_paciente)

    def abrir_inicio(self):
        from principal_paciente import principal
        self.ventana.withdraw()
        principal(self.ventana, self.id_paciente)
        
    def abrir_perfil(self):
        from perfil import usuario_perfil
        self.ventana.withdraw()
        usuario_perfil(self.ventana, self.id_paciente)
    
    def recordatorios_medicos(self):
            from recordatorios_medicos import recordatorios_medicoos
            self.ventana.withdraw()
            recordatorios_medicoos(self.ventana, self.id_paciente)
    
    def recordatorios_todos(self):
        from recordatorios import recordatorios1
        self.ventana.withdraw()
        recordatorios1(self.ventana , self.id_paciente)
 
#FUNCIONES


if __name__ == "__main__":

    ventana = tk.Tk()
    ventana.withdraw()

    app = recordatorios_actividadees(ventana)

    ventana.mainloop()