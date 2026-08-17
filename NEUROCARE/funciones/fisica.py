import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from conexion import conectarBd

# python NEUROCARE/funciones/fisica.py

class ejercicios_fisicos:
    def __init__(self,root,idPaciente):
        self.root = root
        self.idPaciente = idPaciente
        self.ventana = tk.Toplevel(root)
        self.ventana.title("NEUROCARE -- Ejercicios físicos")
        self.ventana.geometry("640x700+500+10")
        self.ventana.configure(bg="#DDF4E7")
        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        self.ejercicio_activo = None
        self.tiempo_restante = 0
        self.temporizador = None
        self.crear_interfaz()
        self.cargar_actividades()

    def crear_interfaz(self):
        # CANVAS
        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="#DDF4E7",highlightthickness=0)
        self.canvas.pack(side="left",fill="both",expand=True)

        # BARRA DE SCROLL
        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical",command=self.canvas.yview)
        barra_scroll.pack(side="right",fill="y")
        self.canvas.configure(yscrollcommand=barra_scroll.set)

        # MARCO PRINCIPAL
        self.marco_principal = tk.Frame(self.canvas)
        self.marco_principal.configure(bg="#DDF4E7")
        self.canvas.create_window((0,0),window=self.marco_principal,anchor="nw")
        self.marco_principal.bind("<Configure>",lambda evento:self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # ENCABEZADO
        marco_superior = tk.Frame(self.marco_principal)
        marco_superior.configure(bg="#DDF4E7",width=600,height=80)
        marco_superior.pack(padx=0,pady=(20,10))
        marco_superior.pack_propagate(False)

        boton_regresar = ctk.CTkButton(marco_superior,text="←",width=50,height=50,corner_radius=25,fg_color="white",hover_color="#E5E7EB",text_color="black",font=("Arial",24,"bold"),command=self.regresar)
        boton_regresar.pack(side="left")

        marco_titulo = tk.Frame(marco_superior)
        marco_titulo.configure(bg="#DDF4E7",width=300,height=81)
        marco_titulo.pack(side="left",padx=30,expand=True)
        marco_titulo.pack_propagate(False)

        etiqueta_categoria = tk.Label(marco_titulo,text="FÍSICA")
        etiqueta_categoria.configure(bg="#DDF4E7",fg="dim gray",font=("Quicksand",12,"bold"))
        etiqueta_categoria.pack()

        etiqueta_titulo = tk.Label(marco_titulo,text="Ejercicios")
        etiqueta_titulo.configure(bg="#DDF4E7",fg="black",font=("Quicksand",22,"bold"))
        etiqueta_titulo.pack()

        # EJERCICIO ACTIVO
        self.marco_activo = ctk.CTkFrame(self.marco_principal,width=600,height=220,fg_color="#D1FAE5",corner_radius=30,border_width=2,border_color="#22C55E")
        self.marco_activo.pack(padx=10,pady=(0,15))
        self.marco_activo.pack_propagate(False)

        self.etiqueta_activo = tk.Label(self.marco_activo,text="Selecciona un ejercicio")
        self.etiqueta_activo.configure(bg="#D1FAE5",fg="#16A34A",font=("Quicksand",22,"bold"))
        self.etiqueta_activo.pack(pady=(25,5))

        self.etiqueta_descripcion_activo = tk.Label(self.marco_activo,text="Presiona el botón --> de un ejercicio para comenzar.")
        self.etiqueta_descripcion_activo.configure(bg="#D1FAE5",fg="dim gray",font=("Quicksand",12))
        self.etiqueta_descripcion_activo.pack()

        self.etiqueta_tiempo = tk.Label(self.marco_activo,text="")
        self.etiqueta_tiempo.configure(bg="#D1FAE5",fg="#16A34A",font=("Arial",28,"bold"))
        self.etiqueta_tiempo.pack(pady=5)

        self.boton_iniciar = ctk.CTkButton(self.marco_activo,text="▶ Iniciar",width=180,height=45,corner_radius=22,fg_color="#22C55E",hover_color="#16A34A",font=("Arial",15,"bold"),command=self.iniciar_ejercicio)
        self.boton_iniciar.pack(pady=5)

        # LISTA
        marco_lista = tk.Frame(self.marco_principal)
        marco_lista.configure(width=600,height=40,bg="#DDF4E7")
        marco_lista.pack()
        marco_lista.pack_propagate(False)

        informacion = tk.Label(marco_lista,text="Lista de ejercicios")
        informacion.configure(fg="dim gray",bg="#DDF4E7",font=("Arial",15))
        informacion.pack(side="left",pady=5)

        self.marco_lista_ejercicios = tk.Frame(self.marco_principal)
        self.marco_lista_ejercicios.configure(bg="#DDF4E7",width=600)
        self.marco_lista_ejercicios.pack(fill="x")

    def cargar_actividades(self):
        actividades_fisicas = [
            ("Respiración profunda","Inhala 4s, mantén 4s, exhala 6s.",60),
            ("Estiramiento de cuello","Gira suavemente la cabeza a los lados.",45),
            ("Hombros arriba y abajo","Sube y baja los hombros lentamente.",45),
            ("Marcha suave en el lugar","Marcha en el sitio a paso cómodo.",60),
            ("Estiramiento de brazos","Alza los brazos y estíralos hacia el techo.",45)
        ]

        conexion = None
        cursor = None

        try:
            conexion = conectarBd()
            cursor = conexion.cursor()

            for nombre,descripcion,tiempo in actividades_fisicas:
                cursor.execute("SELECT idActividad FROM actividad WHERE nombreActividad = %s",(nombre,))
                resultado = cursor.fetchone()

                if resultado:
                    idActividad = resultado[0]
                else:
                    cursor.execute("INSERT INTO actividad(nombreActividad,descripcion,tiempoEstimado) VALUES(%s,%s,%s)",(nombre,descripcion,tiempo))
                    conexion.commit()
                    idActividad = cursor.lastrowid

                self.crear_tarjeta(idActividad,nombre,descripcion,tiempo)

        except Exception as error:
            messagebox.showerror("Error","No se pudieron cargar los ejercicios:\n"+str(error))

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    def crear_tarjeta(self,idActividad,nombre,descripcion,tiempo):
        numero = len(self.marco_lista_ejercicios.winfo_children()) + 1

        tarjeta = ctk.CTkFrame(self.marco_lista_ejercicios,width=600,height=140,fg_color="white",corner_radius=25,border_width=3,border_color="#22C55E")
        tarjeta.pack(pady=(0,20),padx=10)
        tarjeta.pack_propagate(False)

        contenedor = tk.Frame(tarjeta)
        contenedor.configure(bg="white")
        contenedor.pack(fill="both",expand=True,padx=20,pady=15)

        # MARCO IZQUIERDO
        marco_izquierdo = tk.Frame(contenedor)
        marco_izquierdo.configure(width=100,height=100,bg="white")
        marco_izquierdo.pack(side="left")
        marco_izquierdo.pack_propagate(False)

        marco_icono = ctk.CTkFrame(marco_izquierdo,width=80,height=80,corner_radius=30,fg_color="#E9D5FF")
        marco_icono.pack(expand=True)
        marco_icono.pack_propagate(False)

        etiqueta_numero = tk.Label(marco_icono,text=str(numero))
        etiqueta_numero.configure(bg="#E9D5FF",fg="purple",font=("Arial",40,"bold"))
        etiqueta_numero.pack(expand=True)

        # MARCO CENTRO
        marco_centro = tk.Frame(contenedor)
        marco_centro.configure(bg="white")
        marco_centro.pack(side="left",fill="both",expand=True,padx=(20,10))

        etiqueta_nombre = tk.Label(marco_centro,text=nombre)
        etiqueta_nombre.configure(bg="white",fg="#22C55E",font=("Quicksand",18,"bold"))
        etiqueta_nombre.pack(anchor="w",pady=(2,2))

        etiqueta_descripcion = tk.Label(marco_centro,text=descripcion+"\nTotal="+str(tiempo)+"s")
        etiqueta_descripcion.configure(bg="white",fg="dim gray",font=("Quicksand",11),justify="left",wraplength=250)
        etiqueta_descripcion.pack(anchor="w")

        # MARCO DERECHO
        marco_derecho = tk.Frame(contenedor)
        marco_derecho.configure(width=90,height=100,bg="white")
        marco_derecho.pack(side="right")
        marco_derecho.pack_propagate(False)

        boton = ctk.CTkButton(marco_derecho,text="-->",width=70,height=70,corner_radius=35,fg_color="#22C55E",hover_color="#16A34A",text_color="white",font=("Arial",22,"bold"),command=lambda:self.seleccionar_ejercicio(idActividad,nombre,descripcion,tiempo))
        boton.pack(expand=True)

    def seleccionar_ejercicio(self,idActividad,nombre,descripcion,tiempo):
        if self.temporizador:
            self.ventana.after_cancel(self.temporizador)
            self.temporizador = None

        self.ejercicio_activo = idActividad
        self.tiempo_restante = tiempo

        self.etiqueta_activo.configure(text=nombre)
        self.etiqueta_descripcion_activo.configure(text=descripcion)
        self.etiqueta_tiempo.configure(text=str(tiempo)+"s")
        self.boton_iniciar.configure(text="▶ Iniciar",state="normal")

        self.canvas.yview_moveto(0)

    def iniciar_ejercicio(self):
        if self.ejercicio_activo is None:
            messagebox.showinfo("Ejercicio","Primero selecciona un ejercicio de la lista.")
            return

        if self.tiempo_restante <= 0:
            return

        self.boton_iniciar.configure(text="Ejercicio en curso...",state="disabled")
        self.contador()

    def contador(self):
        if self.tiempo_restante > 0:
            self.etiqueta_tiempo.configure(text=str(self.tiempo_restante)+"s")
            self.tiempo_restante -= 1
            self.temporizador = self.ventana.after(1000,self.contador)
        else:
            self.temporizador = None
            self.etiqueta_tiempo.configure(text="¡Completado!")
            self.guardar_historial()
            self.boton_iniciar.configure(text="✓ Completado",state="disabled")

    def guardar_historial(self):
        conexion = None
        cursor = None

        try:
            conexion = conectarBd()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO historialActividad(idPaciente,idActividad,fecha,puntuacion,tiempoRealizado,completada) VALUES(%s,%s,CURDATE(),%s,%s,%s)",(self.idPaciente,self.ejercicio_activo,100,0,True))
            conexion.commit()

        except Exception as error:
            messagebox.showerror("Error","No se pudo guardar la actividad:\n"+str(error))

        finally:
            if cursor:
                cursor.close()

            if conexion:
                conexion.close()

    def regresar(self):
        if self.temporizador:
            self.ventana.after_cancel(self.temporizador)
            self.temporizador = None

        self.ventana.destroy()

        if self.root.winfo_exists():
            self.root.deiconify()
            self.root.update_idletasks()
            self.root.lift()
            self.root.focus_force()


if __name__ == "__main__":
    ventana = tk.Tk()
    idPaciente = 1
    app = ejercicios_fisicos(ventana,idPaciente)
    ventana.mainloop()