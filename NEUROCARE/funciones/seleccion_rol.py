from registro_paciente import registrar_paciente
from registro_familiar import registrar_familiar
from PIL import Image, ImageTk
import tkinter as tk

class rol:
    def __init__(self,root):
        self.root = root
        self.ventana = tk.Toplevel(root)
        
        self.ventana.title(" NEUROCARE -- SELECCION DE ROL")
        self.ventana.geometry("500x650+500+60")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        
        marco_boton = tk.Frame(self.ventana, bg="lavender")
        marco_boton.configure(width=600, height=40)
        marco_boton.pack(pady=(4,0))
        marco_boton.pack_propagate(False)
        
        boton_volver = tk.Button(marco_boton,text="<--")
        boton_volver.configure(fg="black", bg="white", font=("Quicksand", 10, "bold"), command=self.volver_sesion)
        boton_volver.pack(side="left",)
        
        marco_principal= tk.Frame(self.ventana, bg="lavender")
        marco_principal.configure(width=500, height=550)
        marco_principal.pack(pady=(0,10))
        marco_principal.pack_propagate(False)
        
        marco_info = tk.Frame(marco_principal, bg="lavender")
        marco_info.configure(width=400, height=80)
        marco_info.pack( padx=20, pady=(5,5))
        marco_info.pack_propagate(False)
        
        etiqueta_selecion = tk.Label(marco_info, text="Selecciona tu rol",)
        etiqueta_selecion.configure(fg="black", bg="lavender", font=("Quicksand", 18, "bold"))
        etiqueta_selecion.pack(side="top", anchor="w", pady=(2,2))
        
        etiqueta_text = tk.Label(marco_info, text="Elige como vas a usar NeuroCare")
        etiqueta_text.configure(fg="gray", bg="lavender", font=("Arial", 12))
        etiqueta_text.pack(side="bottom", anchor="w", pady=(2,5))
        
        marco_paciente = tk.Frame(marco_principal, bg="#EDE7F6")
        marco_paciente.configure(width=400, height=190,  highlightbackground="purple",
                                 highlightthickness=3)
        marco_paciente.pack(pady=(15,10))
        marco_paciente.pack_propagate(False)
        
        marco_izquierdo = tk.Frame(marco_paciente, bg="#EDE7F6")
        marco_izquierdo.configure(width=250, height=180)
        marco_izquierdo.pack(side="left", anchor="nw", padx=10, pady=5)
        marco_izquierdo.pack_propagate(False)
        
        marco_texto1 =tk.Frame(marco_izquierdo, bg="#EDE7F6")
        marco_texto1.configure(width=230, height=100)
        marco_texto1.pack(anchor="nw")
        marco_texto1.pack(pady=(10,10), padx=5)
        
        
        marco_titulo = tk.Frame(marco_texto1, bg="#EDE7F6")
        marco_titulo.pack(anchor="nw", padx=5)
        
        etiqueta_soy = tk.Label(marco_titulo, text= "Soy")
        etiqueta_soy.configure(fg="black", bg="#EDE7F6", font=("Quicksand",22))
        etiqueta_soy.pack( side="left")
        
        etiqueta_text_paciente = tk.Label(marco_titulo, text="Paciente")
        etiqueta_text_paciente.configure(fg="purple", bg="#EDE7F6", font=("Arial", 22))
        etiqueta_text_paciente.pack( side="left", padx=(1,0), pady=(5,0))
        
        etiqueta_texto_info = tk.Label(marco_texto1, text="Quiero cuidar mi mente \ny mi bienestar")
        etiqueta_texto_info.configure(fg="black", bg="#EDE7F6", font=("Arial",15))
        etiqueta_texto_info.pack(anchor="nw", pady=(6,2))

        marco_boton1 = tk.Frame(marco_izquierdo, bg="#EDE7F6")
        marco_boton1.configure(width=150,height=60)
        marco_boton1.pack( anchor="nw")
        marco_boton1.pack(pady=(5,2), padx=20)
        marco_boton1.pack_propagate(False)
        
        
        boton_elegir = tk.Button(marco_boton1, text="Elegir -->")
        boton_elegir.configure(fg="#7E57C2", bg="white", font=("Arial",18), padx=45, command=self.abrir_rol_paciente)
        boton_elegir.pack(pady=5)
        
        marco_imagen_paciente = tk.Frame(marco_paciente, bg="MediumPurple3")
        marco_imagen_paciente.configure(width=120, height=130)
        marco_imagen_paciente.pack(side="right", anchor="ne", padx=(5,5), pady=25)
        marco_imagen_paciente.pack_propagate(False)
        
        
        self.imagen_paciente = tk.PhotoImage( file="NEUROCARE/funciones/recursos/perfil.png")
        self.imagen_paciente.subsample(5,5)
        etiqueta_imagen_paciente = tk.Label(marco_imagen_paciente, image=self.imagen_paciente, bg="#EDE7F6")
        etiqueta_imagen_paciente.pack()
        
        marco_familiar = tk.Frame(marco_principal, bg="#E8F5E9")
        marco_familiar.configure(width=400, height=190, highlightbackground="green", highlightthickness=3)
        marco_familiar.pack(pady=(10,5))
        marco_familiar.pack_propagate(False)
        
        marco_izquierdo1 = tk.Frame(marco_familiar, bg="#E8F5E9")
        marco_izquierdo1.configure(width=250, height=180)
        marco_izquierdo1.pack(side="left", anchor="nw", padx=10, pady=5)
        marco_izquierdo1.pack_propagate(False)
        
        marco_texto2 =tk.Frame(marco_izquierdo1, bg="#E8F5E9")
        marco_texto2.configure(width=230, height=100)
        marco_texto2.pack(anchor="nw")
        marco_texto2.pack(pady=(10,10), padx=5)
        marco_texto2.pack_propagate(False)
        
        marco_titulo1 = tk.Frame(marco_texto2, bg="#E8F5E9")
        marco_titulo1.configure(width=60, height=30)
        marco_titulo1.pack(anchor="nw", padx=5)
        
        etiqueta_soy1 = tk.Label(marco_titulo1, text= "Soy")
        etiqueta_soy1.configure(fg="black", bg="#E8F5E9", font=("Quicksand",17))
        etiqueta_soy1.pack( side="left", padx=(5,2))
        
        etiqueta_text_familiar = tk.Label(marco_titulo1, text="Familiar/Cuidador")
        etiqueta_text_familiar.configure(fg="green", bg="#E8F5E9", font=("Arial", 16))
        etiqueta_text_familiar.pack( side="left", padx=(3,0), pady=(5,0))
        
        etiqueta_texto_info1 = tk.Label(marco_texto2, text="Quiero ayudar y apoyar a\n mi ser querido")
        etiqueta_texto_info1.configure(fg="black", bg="#E8F5E9", font=("Arial",15))
        etiqueta_texto_info1.pack(anchor="nw", pady=(6,2))
        
        marco_boton2 = tk.Frame(marco_izquierdo1, bg="#E8F5E9")
        marco_boton2.configure(width=100,height=10)
        marco_boton2.pack( anchor="nw")
        marco_boton2.pack(pady=(10,10), padx=20)
        
            
        boton_elegir1 = tk.Button(marco_boton2, text="Elegir -->")
        boton_elegir1.configure(fg="#7E57C2", bg="white", font=("Arial",16), padx=30, command=self.abrir_rol_familia)
        boton_elegir1.pack(pady=5)
        
        marco_imagen_familiar = tk.Frame(marco_familiar, bg="#E8F5E9")
        marco_imagen_familiar.configure(width=120, height=130)
        marco_imagen_familiar.pack(side="right", anchor="ne", padx=(5,5), pady=25)
        marco_imagen_familiar.pack_propagate(False)
        
        self.imagen_familiar = tk.PhotoImage( file="NEUROCARE/funciones/recursos/parentesco.png")
        self.imagen_familiar.subsample(2,2)
        etiqueta_imagen_familiar = tk.Label(marco_imagen_familiar, image=self.imagen_familiar, bg="#EDE7F6")
        etiqueta_imagen_familiar.pack()
        
    def abrir_rol_familia(self):
        self.ventana.withdraw()
        registrar_familiar(self.ventana)
        
    def abrir_rol_paciente(self):
        self.ventana.withdraw()
        registrar_paciente(self.ventana)
        
    def volver_sesion(self):
        from inicio_sesion import iniciar_sesion
        self.ventana.withdraw()
        iniciar_sesion(self.ventana)
        
        

        
        
        
        
        
if __name__ =="__main__":
    ventana = tk.Tk()
    app = rol(ventana)
    ventana.mainloop()