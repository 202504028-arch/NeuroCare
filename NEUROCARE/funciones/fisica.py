import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk


                                #python NEUROCARE/funciones/fisica.py
class ejercicios_fisicos:

    def __init__(self, root):

        self.root = root
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- Ejerciios fisicos")
        self.ventana.geometry("640x700+500+10")
        self.ventana.configure(bg="#DDF4E7")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
      

        self.crear_interfaz()

    def crear_interfaz(self):
        
#CANVAS 

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="#DDF4E7", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

#BARRA DE SCROLL

        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical", command=self.canvas.yview)
        barra_scroll.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=barra_scroll.set)

# MARCO PRINCIPAL 

        self.marco_principal = tk.Frame(self.canvas)
        self.marco_principal.configure(bg="#DDF4E7")

        self.canvas.create_window((0,0), window=self.marco_principal, anchor="nw")

        self.marco_principal.bind(
            "<Configure>",
            lambda evento:
            self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        
        marco_superior = tk.Frame(self.marco_principal)
        marco_superior.configure(bg="#DDF4E7", width=600, height=80)
        marco_superior.pack(padx=0, pady=(20,10))
        marco_superior.pack_propagate(False)
        
        
        boton_regresar = ctk.CTkButton(marco_superior,text="←",width=50,height=50,corner_radius=25,fg_color="white",
                                        hover_color="#E5E7EB",text_color="black",font=("Arial",24,"bold"),command=self.regresar)
        boton_regresar.pack(side="left")
        
        #-------------------- TITULO --------------------#

        marco_titulo = tk.Frame(marco_superior)
        marco_titulo.configure(bg="#DDF4E7", width=300, height=81)
        marco_titulo.pack(side="left", padx=30, expand=True)
        marco_titulo.pack_propagate(False)

        etiqueta_categoria = tk.Label(marco_titulo,text="FISICA")
        etiqueta_categoria.configure(bg="#DDF4E7",fg="dim gray",font=("Quicksand",12,"bold"))
        etiqueta_categoria.pack()

        etiqueta_titulo = tk.Label(marco_titulo,text="Ejercicios")
        etiqueta_titulo.configure(bg="#DDF4E7",fg="black",font=("Quicksand",22,"bold"))
        etiqueta_titulo.pack()
        
        
        #zona de ejercicio activo
        marco_activo= ctk.CTkFrame(self.marco_principal)
        marco_activo.configure(width=600, height=200, fg_color="red", corner_radius=30, border_width=2,border_color="lime green")
        marco_activo.pack(padx=10)
        
        marco_lista= tk.Frame(self.marco_principal)
        marco_lista.configure(width=600, height=30, bg="#DDF4E7")
        marco_lista.pack()
        
        informacion = tk.Label(marco_lista, text="Lista de ejercicios", bg="#DDF4E7")
        informacion.configure(fg="dim gray", font=("Arial",15))
        informacion.pack(side="left",pady=5)
        
        #lista de ejercicios
        #respiracion profunda
        
        marco_tarjeta_respiracion = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_respiracion.configure(width=600,height=130,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_respiracion.pack(pady=(0,20),padx=10)
        marco_tarjeta_respiracion.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_respiratorio = tk.Frame(marco_tarjeta_respiracion)
        contenedor_respiratorio.configure(bg="white")
        contenedor_respiratorio.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_respiratorio)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono1 = ctk.CTkFrame(marco_izquierdo,width=100,height=100,
        corner_radius=35,fg_color="#E9D5FF")
        marco_icono1.pack(expand=True)
        marco_icono1.pack_propagate(False)

        etiqueta_numero1 = tk.Label(marco_icono1, text="1", bg="#E9D5FF")
        etiqueta_numero1.configure(fg="purple", font=("Arial",50,"bold"))
        etiqueta_numero1.pack(anchor="center", pady=(5,5))
#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_respiratorio)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_recordatorio = tk.Label(marco_centro,text="Respiracion profunda")
        etiqueta_titulo_recordatorio.configure(bg="white",fg="#22C55E",
        font=("Quicksand",20,"bold"))
        etiqueta_titulo_recordatorio.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion_recordatorio = tk.Label(marco_centro,
        text="Inhala 4s, manten 4s, exhala 6s.\n                                          Total=60s")
        etiqueta_descripcion_recordatorio.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_recordatorio.pack(anchor="w", pady=0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_respiratorio)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_recordatorios = ctk.CTkButton(marco_derecho,text="-->",width=85,height=85,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"))

        boton_recordatorios.pack(expand=True)
        
        #estiramiento de cuello
        
        marco_tarjeta_cuello = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_cuello.configure(width=600,height=130,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_cuello.pack(pady=(0,20),padx=10)
        marco_tarjeta_cuello.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_cuello = tk.Frame(marco_tarjeta_cuello)
        contenedor_cuello.configure(bg="white")
        contenedor_cuello.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_cuello)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono2 = ctk.CTkFrame(marco_izquierdo,width=100,height=100,
        corner_radius=35,fg_color="#E9D5FF")
        marco_icono2.pack(expand=True)
        marco_icono2.pack_propagate(False)

        etiqueta_numero2 = tk.Label(marco_icono2, text="2", bg="#E9D5FF")
        etiqueta_numero2.configure(fg="purple", font=("Arial",50,"bold"))
        etiqueta_numero2.pack(anchor="center", pady=(5,5))
#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_cuello)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_cuello = tk.Label(marco_centro,text="Estiramiento de cuello")
        etiqueta_titulo_cuello.configure(bg="white",fg="#22C55E",
        font=("Quicksand",20,"bold"))
        etiqueta_titulo_cuello.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion_cuello = tk.Label(marco_centro,
        text="gira suavemente la cabeza a los lados.                                Total=45s")
        etiqueta_descripcion_cuello.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_cuello.pack(anchor="w", pady=0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_cuello)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_cuello = ctk.CTkButton(marco_derecho,text="-->",width=85,height=85,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"))

        boton_cuello.pack(expand=True)
        
        #hombros arriba y abajo
        
        marco_tarjeta_hombros = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_hombros.configure(width=600,height=130,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_hombros.pack(pady=(0,20),padx=10)
        marco_tarjeta_hombros.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_hombros = tk.Frame(marco_tarjeta_hombros)
        contenedor_hombros.configure(bg="white")
        contenedor_hombros.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_hombros)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono3 = ctk.CTkFrame(marco_izquierdo,width=100,height=100,
        corner_radius=35,fg_color="#E9D5FF")
        marco_icono3.pack(expand=True)
        marco_icono3.pack_propagate(False)

        etiqueta_numero3 = tk.Label(marco_icono3, text="3", bg="#E9D5FF")
        etiqueta_numero3.configure(fg="purple", font=("Arial",50,"bold"))
        etiqueta_numero3.pack(anchor="center", pady=(5,5))
#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_hombros)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_hombros = tk.Label(marco_centro,text="Hombros arriba y abajo")
        etiqueta_titulo_hombros.configure(bg="white",fg="#22C55E",
        font=("Quicksand",18,"bold"))
        etiqueta_titulo_hombros.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion_hombros = tk.Label(marco_centro,
        text="sube y baja los hombros lentamente.                      Total=45s")
        etiqueta_descripcion_hombros.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_hombros.pack(anchor="w", pady=0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_hombros)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_hombros = ctk.CTkButton(marco_derecho,text="-->",width=85,height=85,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"))

        boton_hombros.pack(expand=True)
        
        #marchar suave en el lugar
        
        marco_tarjeta_marchar = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_marchar.configure(width=600,height=130,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_marchar.pack(pady=(0,20),padx=10)
        marco_tarjeta_marchar.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_marchar = tk.Frame(marco_tarjeta_marchar)
        contenedor_marchar.configure(bg="white")
        contenedor_marchar.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_marchar)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono4 = ctk.CTkFrame(marco_izquierdo,width=100,height=100,
        corner_radius=35,fg_color="#E9D5FF")
        marco_icono4.pack(expand=True)
        marco_icono4.pack_propagate(False)

        etiqueta_numero4 = tk.Label(marco_icono4, text="4", bg="#E9D5FF")
        etiqueta_numero4.configure(fg="purple", font=("Arial",50,"bold"))
        etiqueta_numero4.pack(anchor="center", pady=(5,5))
#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_marchar)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_marchar = tk.Label(marco_centro,text="Marcha suave en el lugar")
        etiqueta_titulo_marchar.configure(bg="white",fg="#22C55E",
        font=("Quicksand",17,"bold"))
        etiqueta_titulo_marchar.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion_marchar = tk.Label(marco_centro,
        text="marcha en el sitio a paso comodo.                       Total=60s")
        etiqueta_descripcion_marchar.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_marchar.pack(anchor="w", pady=0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_marchar)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_marchar = ctk.CTkButton(marco_derecho,text="-->",width=85,height=85,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"))

        boton_marchar.pack(expand=True)
        
        #estiramiento de brazos
        
        marco_tarjeta_brazos = ctk.CTkFrame(self.marco_principal)
        marco_tarjeta_brazos.configure(width=600,height=130,fg_color="white",
        corner_radius=25,border_width=3,border_color="#22C55E")
        marco_tarjeta_brazos.pack(pady=(0,20),padx=10)
        marco_tarjeta_brazos.pack_propagate(False)

#-------------------- CONTENEDOR --------------------#

        contenedor_brazos = tk.Frame(marco_tarjeta_brazos)
        contenedor_brazos.configure(bg="white")
        contenedor_brazos.pack(fill="both",expand=True,padx=20,pady=20)

#-------------------- MARCO IZQUIERDO --------------------#

        marco_izquierdo = tk.Frame(contenedor_brazos)
        marco_izquierdo.configure(width=120,height=130,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono5 = ctk.CTkFrame(marco_izquierdo,width=100,height=100,
        corner_radius=35,fg_color="#E9D5FF")
        marco_icono5.pack(expand=True)
        marco_icono5.pack_propagate(False)

        etiqueta_numero5 = tk.Label(marco_icono5, text="5", bg="#E9D5FF")
        etiqueta_numero5.configure(fg="purple", font=("Arial",50,"bold"))
        etiqueta_numero5.pack(anchor="center", pady=(5,5))
#-------------------- MARCO CENTRO --------------------#

        marco_centro = tk.Frame(contenedor_brazos)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_titulo_brazos = tk.Label(marco_centro,text="Estiramiento de brazos")
        etiqueta_titulo_brazos.configure(bg="white",fg="#22C55E",
        font=("Quicksand",20,"bold"))
        etiqueta_titulo_brazos.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion_brazos = tk.Label(marco_centro,
        text="alza los brazos y estiralos hacia el techo                          Total=45s")
        etiqueta_descripcion_brazos.configure(bg="white",fg="dim gray",
        font=("Quicksand",12),justify="left",wraplength=250)
        etiqueta_descripcion_brazos.pack(anchor="w", pady=0)

#-------------------- MARCO DERECHO --------------------#

        marco_derecho = tk.Frame(contenedor_brazos)
        marco_derecho.configure(width=110,height=130,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton_brazos = ctk.CTkButton(marco_derecho,text="-->",width=85,height=85,
        corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",
        text_color="white",font=("Arial",28,"bold"))

        boton_brazos.pack(expand=True)

    def regresar(self):

        self.ventana.destroy()

        try:
            from actividades import juegos
            juegos(self.root)
        except Exception:
            pass
        

if __name__ =="__main__":
    ventana = tk.Tk()
    app = ejercicios_fisicos(ventana)
    ventana.mainloop()