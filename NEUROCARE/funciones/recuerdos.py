
from tkinter import messagebox
from conexion import conectarBd
import tkinter as tk
                                                #python NEUROCARE/funciones/recuerdos.py
class avisos:
    
    def __init__ (self,root):
            self.root = root
            self.ventana = tk.Toplevel(root)
        

            self.ventana.title(" NEUROCARE -- RECUERDOS")
            self.ventana.geometry("450x700+520+60")
            self.ventana.config(bg="lavender")

            self.ventana.minsize(450,580)
            self.ventana.maxsize(900,700)
            self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
            
            self.crear_interfaz()

    def crear_interfaz(self):
        hi= tk.Label(self.ventana, text="recuerdos")
        hi.pack()
#MENÚ INFERIOR 

        marco_menu = tk.Frame(self.ventana)
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
        boton_avisos.configure(bg="white", fg="medium purple", font=("Quicksand",12), relief="flat", bd=0 )
        boton_avisos.pack(side="left", expand=True)

#BOTÓN PERFIL

        boton_perfil = tk.Button(marco_menu, text="👤\nPerfil")
        boton_perfil.configure(bg="white", fg="dim gray", font=("Quicksand",12), relief="flat", bd=0, command=self.abrir_perfil)
        boton_perfil.pack(side="left", expand=True)
        

        
        

    def abrir_actividades(self):
        from actividades import juegos
        self.ventana.withdraw()
        juegos(self.ventana)

    def abrir_inicio(self):
        from principal_paciente import principal
        self.ventana.withdraw()
        principal(self.ventana)
        
    def abrir_perfil(self):
        from perfil import usuario_perfil
        self.ventana.withdraw()
        usuario_perfil(self.ventana)



if __name__ =="__main__":
    ventana = tk.Tk()
    app = avisos(ventana)
    ventana.mainloop()
    