from inicio_sesion import iniciar_sesion 
import tkinter as tk
                                    #python NEUROCARE/funciones/Bienvenida.py
class bienvenida:
    def __init__(self,root):
        self.root = root
        self.ventana = tk.Toplevel(root)
        

        self.ventana.title(" NEUROCARE -- BIENVENIDA")
        self.ventana.geometry("500x650+500+60")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        

        marco_titulo = tk.Frame(self.ventana,bg="plum1")
        marco_titulo.pack(pady=5)


        etiqueta_titulo = tk.Label(marco_titulo, text= "BIENVENIDO A ")
        etiqueta_titulo.configure(fg="white", bg="lavender", font= ("Arial",25,"bold"))
        etiqueta_titulo.pack(side="left")

        etiqueta_neuro = tk.Label(marco_titulo, text="NEUROCARE")
        etiqueta_neuro.configure(fg="purple", bg="lavender", font=("Arial",25,"bold"))
        etiqueta_neuro.pack(side="left")


        self.imagen_mascota =tk.PhotoImage(file="NEUROCARE/funciones/recursos/masc.png")
        self.imagen_mascota = self.imagen_mascota.zoom(2,2)
        etiqueta_mascota = tk.Label(self.ventana, image=self.imagen_mascota, bg="lavender")
        etiqueta_mascota.pack()


        etiqueta_texto=tk.Label(self.ventana, text= "Tu guia para el cuidado cognitivo y el bienestar.")
        etiqueta_texto.configure(fg="dim gray", bg= "lavender", font=("Arial", 14))
        etiqueta_texto.pack(pady=5)

        labelframe = tk.LabelFrame(self.ventana, text="", bg="lavender", padx=10, pady=10, bd=0 )
        labelframe.config(width=500, height=400, padx= 20,)
        labelframe.pack()

        marco_cuida = tk.Frame(labelframe, bg="plum1")
        marco_cuida.pack(pady=(5,2))

        etiqueta = tk.Label(marco_cuida, text="CUIDA TU MENTE")
        etiqueta.configure(fg="purple4", bg="plum1", font=("Arial",20))
        etiqueta.pack(side="right", padx=65)

        self.imagen1 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/corazon.png")
        self.imagen1 = self.imagen1.subsample(8,8)
        etiqueta_imagen1 = tk.Label(marco_cuida, image=self.imagen1, bg="plum1")
        etiqueta_imagen1.pack(side="right", padx=10)

        etiqueta1 = tk.Label(labelframe, text="actividades y ejercicios para estimular tu memoria")
        etiqueta1.configure(fg="dim gray", bg="pink", padx=7)
        etiqueta1.config(font=("Quicksand",13))
        etiqueta1.pack(pady=(0,15))

        marco_acompañado = tk.Frame(labelframe, bg="pale green")
        marco_acompañado.pack(pady=(5,2))

        etiqueta2 = tk.Label(marco_acompañado, text="SIEMPRE ACOMPAÑADO")
        etiqueta2.configure(fg="dark green", bg="pale green", font=("Arial",20))
        etiqueta2.config(padx=5)
        etiqueta2.pack(side="right", padx=18 )

        self.imagen2 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/parentesco.png")
        self.imagen2 = self.imagen2.subsample(5,5)
        etiqueta_imagen2 = tk.Label(marco_acompañado, image=self.imagen2, bg="pale green")
        etiqueta_imagen2.pack(side="right", padx=10)

        etiqueta3 = tk.Label(labelframe, text="tu familia puede ayudarte y estar atento a ti")
        etiqueta3.configure(fg="dark green", bg="honeydew2", padx=35)
        etiqueta3.config(font=("Quicksand",13))
        etiqueta3.pack(pady=(0,15))

        marco_facil = tk.Frame(labelframe, bg="peach puff")
        marco_facil.pack(pady=(5,2))

        etiqueta4= tk.Label (marco_facil, text="SEGURO Y FACIL DE USAR")
        etiqueta4.configure(fg="dark orange", bg="peach puff",font=("Arial",18))
        etiqueta4.config(padx=30)
        etiqueta4.pack(side="right")

        self.imagen3 = tk.PhotoImage(file="NEUROCARE/funciones/recursos/perfil.png")
        self.imagen3 = self.imagen3.subsample(5,5)
        etiqueta_imagen3 = tk.Label(marco_facil, image=self.imagen3, bg= "peach puff")
        etiqueta_imagen3.pack(side="right", padx=10)

        etiqueta5 = tk.Label(labelframe, text="interfaz diseñada specialmente para ti")
        etiqueta5.configure(fg="saddle brown", bg="bisque2", padx=60)
        etiqueta5.config(font=("Quicksand",13))
        etiqueta5.pack(pady=(0,10))


        boton = tk.Button(labelframe, text="INICIAR -->")
        boton.configure(fg="white", bg="medium purple", font=("Quicksand",15,"bold"), command=self.abrir_inicio_sesion)
        boton.pack(pady=(5,2))
        
  
    def abrir_inicio_sesion(self):
            self.ventana.withdraw()
            iniciar_sesion(self.ventana)
            
            
    
    
if __name__ =="__main__":
    ventana = tk.Tk()
    ventana.withdraw()
    app = bienvenida(ventana)
    ventana.mainloop()
    