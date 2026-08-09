from seleccion_rol import rol
from tkinter import messagebox
from conexion import conectarBd
import tkinter as tk

class iniciar_sesion:
                                                                            #python NEUROCARE/funciones/inicio_sesion.py
    def __init__ (self,root):
            self.root = root
            self.ventana = tk.Toplevel(root)
        

            self.ventana.title(" NEUROCARE -- INICIO DE SESION")
            self.ventana.geometry("450x700+520+60")
            self.ventana.config(bg="lavender")

            self.ventana.minsize(False,False)
            self.ventana.maxsize(False,False)
            self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")


            self.crear_interfaz1()
            
    def crear_interfaz1(self):
        
        marco_neuro = tk.Frame(self.ventana, bg="lavender")
        marco_neuro.configure(width=200, height= 60)
        marco_neuro.pack(pady=(10,5))
        marco_neuro.pack_propagate(False)
        
        etiqueta_neuro = tk.Label(marco_neuro, text="NEUROCARE")
        etiqueta_neuro.configure(fg="purple", bg= "lavender", font=("Quicksand",15,"bold"))
        etiqueta_neuro.pack(side="right",padx=5)
        
        self.imagen = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen = self.imagen.subsample(4,4)
        etiqueta_imagen = tk.Label(marco_neuro, image=self.imagen, bg="lavender")
        etiqueta_imagen.pack(side="left",padx=0)
        
        marco_sesion = tk.Frame(self.ventana, bg="lavender")
        marco_sesion.configure(width=400, height=60)
        marco_sesion.pack(pady=(5,5))
        marco_sesion.pack_propagate(False)
        
        etiqueta1 = tk.Label(marco_sesion, text="Iniciar Sesion")
        etiqueta1.configure(fg="black", bg="lavender", font=("Quicksand", 18, "bold"))
        etiqueta1.pack(side="top", anchor="w")
        
        etiqueta2 =tk.Label(marco_sesion, text="Nos alegra verte de nuevo :)")
        etiqueta2.configure(fg="dim gray", bg="lavender", font=("Quicksand", 11, "bold"))
        etiqueta2.pack(side="top", anchor="w")
        
        marco_principal = tk.Frame(self.ventana, bg="lavender")
        marco_principal.configure(width=500, height=500)
        marco_principal.pack(pady=(10,20))
        marco_principal.pack_propagate(False)
        
        marco_telefono = tk.Frame(marco_principal, bg="lavender", )
        marco_telefono.configure(width=400, height=50, )
        marco_telefono.pack(pady=(30,0))
        marco_telefono.pack_propagate(False)
        
        marco_entrada1 = tk.Frame(marco_principal, bg="lavender")
        marco_entrada1.configure(width=400, height=50, )
        marco_entrada1.pack(pady=(0,15))
        marco_entrada1.pack_propagate(False)
        
        self.imagen1 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/celular.png")
        self.imagen1 = self.imagen1.subsample(4,4)
        etiqueta_imagen1 = tk.Label(marco_telefono, image=self.imagen1, bg="lavender")
        etiqueta_imagen1.pack(side="left", anchor="n")
        
        etiqueta3 = tk.Label(marco_telefono, text="Numero de celular o correo")
        etiqueta3.configure(fg="black", bg="lavender", font=("Quicksand",18))
        etiqueta3.pack(side="left", anchor="n", pady=(0,10))
        
        self.entry_contacto = tk.Entry(marco_entrada1, bd=2)
        self.entry_contacto.configure( bg="white", font=("Arial",18), width=28, relief="solid", fg="gray")
        
        self.entry_contacto.insert(0, "74412 o panfilo@gmail")
        self.entry_contacto.pack(anchor="w")
        
        def quitar_transfondo(event):
            if self.entry_contacto.get() =="74412 o panfilo@gmail":
                self.entry_contacto.delete(0, tk.END)
                self.entry_contacto.configure(fg="black")
            
            #el evento es cuando el usuario interactua con algo, como una letra, el mause o dentro de la interfaz
        
        def poner_transfondo(event):
            if self.entry_contacto.get()=="":
                self.entry_contacto.insert(0,"74412 o panfilo@gmail")
                self.entry_contacto.configure(fg="gray")
            else:
                self.entry_contacto.configure(fg="black")
            
        
        self.entry_contacto.bind("<FocusIn>",
                            quitar_transfondo)
                                               #bind = si ocurre este evento lo asosias con esta funcion
                                               #foco = widget que esta listo para recibir la entrada del usuario
                                               #In = entraste al widgets , out = saliste del widget
                                               
        self.entry_contacto.bind("<FocusOut>",
                            poner_transfondo)
           
        
        marco_contraseña = tk.Frame(marco_principal, bg="lavender")
        marco_contraseña.configure(width=400, height=50)
        marco_contraseña.pack(pady=(30,0))
        marco_contraseña.pack_propagate(False)
        
        marco_entrada2 = tk.Frame(marco_principal, bg="lavender")
        marco_entrada2.configure(width=400, height=50, )
        marco_entrada2.pack(pady=(0,15))
        marco_entrada2.pack_propagate(False)
        
        self.imagen2 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/celular.png")
        self.imagen2 = self.imagen2.subsample(4,4)
        etiqueta_imagen2 = tk.Label(marco_contraseña, image=self.imagen2, bg="lavender")
        etiqueta_imagen2.pack(side="left", anchor="n")
        
        etiqueta4 = tk.Label(marco_contraseña, text="Contraseña")
        etiqueta4.configure(fg="black", bg="lavender", font=("Quicksand",18))
        etiqueta4.pack(side="left", anchor="n", pady=(0,10))
        
        self.entry_contraseña = tk.Entry(marco_entrada2, bd=2)
        self.entry_contraseña.configure( bg="white", font=("Arial",18), width=28, relief="solid", fg="gray")
        
        self.entry_contraseña.insert(0, "ingrese su contraseña")
        self.entry_contraseña.pack(anchor="w")
        
        def quitar_tranfondo1(event):
            if self.entry_contraseña.get()=="ingrese su contraseña":
                self.entry_contraseña.delete(0, tk.END)
                self.entry_contraseña.configure(fg="black")
                
        def poner_transfondo1(event):
            if self.entry_contraseña.get() =="":
                self.entry_contraseña.insert(0,"ingrese su contraseña")
                self.entry_contraseña.configure(fg="gray")
            else:
                self.entry_contraseña.configure(fg="black")
                
        self.entry_contraseña.bind("<FocusIn>",
                              quitar_tranfondo1)
        self.entry_contraseña.bind("<FocusOut>",
                              poner_transfondo1)
        
        
        boton_entrar = tk.Button(marco_principal, text="ENTRAR -->")
        boton_entrar.configure(fg="white", bg="medium purple", font=("Quicksand",15,"bold"), command=self.entrar_principal)
        boton_entrar.config(padx=100)
        boton_entrar.pack(pady=(10,5))
        
        marco_extra = tk.Frame(marco_principal,bg="lavender")
        marco_extra.configure(width=350, height=30)
        marco_extra.pack(pady=(10,5))

        etiqueta_extra = tk.Label(marco_extra, text="¿No tienes cuenta todavia?")
        etiqueta_extra.configure(fg="dim gray", bg="lavender", font=("Quicksand",12))
        etiqueta_extra.pack()

        boton_registro = tk.Button(marco_principal, text="CREAR CUENTA")
        boton_registro.configure(fg="medium purple", bg="white", font=("Quicksand", 15, "bold"), command= self.abrir_rol)
        boton_registro.config(padx=80)
        boton_registro.pack(pady=(2,5))
        boton_registro.pack_propagate(False)
    
    def abrir_rol(self):
        self.ventana.withdraw()
        rol(self.ventana)
    
    def entrar_principal(self):
        contacto = self.entry_contacto.get()
        contraseña = self.entry_contraseña.get()
        
        if (contacto =="" or contacto =="74412 o panfilo@gmail"
            or contraseña =="" or contraseña=="ingrese su contraseña"):
            messagebox.showwarning(
                "Campos inconpletos",
                "Debes de completar todos los campos"
            )
            return

        conexion = conectarBd()
        cursor = conexion.cursor()
        
        try:
            sql= """
            SELECT * FROM paciente
            where contacto = %s
            and contrasena = %s
            """
            valores =(contacto,contraseña)
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
            
            print("contacto",contacto)
            print("contraseña", contraseña)
            print("resultado", usuario)
            
            if usuario:
                messagebox.showinfo(
                    "BIENVENIDO",
                    "Inicio de sesion exitoso"
                )
                self.ventana.destroy()
                from principal_paciente import principal
                principal(self.root)
                
            else:
                messagebox.showwarning(
                    "Error",
                    "Contacto o contraseña incorrectos"
                )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrio un error:\n{e}"
            )
        finally:
            cursor.close()
            conexion.close()
        
        
        

        
if __name__ =="__main__":
    ventana = tk.Tk()
    app = iniciar_sesion(ventana)
    ventana.mainloop()
    