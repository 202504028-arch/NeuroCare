import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class registrar_familiar:

    def __init__(self, root):

        self.root = root
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- REGISTRO FAMILIAR/CUIDADOR")
        self.ventana.geometry("650x780+400+10")
        self.ventana.configure(bg="#EAFBF0")

        self.ventana.minsize(620,700)
        self.ventana.maxsize(800,900)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")

        self.crear_interfaz()

    def crear_interfaz(self):

        #-------------------- CANVAS --------------------#

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="#EAFBF0", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        #-------------------- BARRA DE SCROLL --------------------#

        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical", command=self.canvas.yview)
        barra_scroll.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=barra_scroll.set)

        #-------------------- MARCO PRINCIPAL --------------------#

        self.marco_principal = tk.Frame(self.canvas)
        self.marco_principal.configure(bg="#EAFBF0")

        self.canvas.create_window((0,0), window=self.marco_principal, anchor="nw")

        self.marco_principal.bind("<Configure>",
            lambda evento:
            self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        #-------------------- ENCABEZADO --------------------#

        marco_encabezado = tk.Frame(self.marco_principal)
        marco_encabezado.configure(width=600, height=90, bg="#EAFBF0")
        marco_encabezado.pack(pady=(15,20))
        marco_encabezado.pack_propagate(False)

#-------------------- BOTÓN REGRESAR --------------------#

        boton_regresar = tk.Button(marco_encabezado, text="<--")
        boton_regresar.configure(fg="black", bg="white", font=("Quicksand", 10, "bold"), command=self.volver_rol)
        boton_regresar.pack(side="left", padx=(10,20))

#-------------------- LOGO --------------------#

        marco_logo = tk.Frame(marco_encabezado)
        marco_logo.configure(bg="#EAFBF0")
        marco_logo.pack(side="left")

        self.imagen_logo = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_logo = self.imagen_logo.subsample(5,5)

        etiqueta_logo = tk.Label(marco_logo, image=self.imagen_logo)
        etiqueta_logo.configure(bg="#EAFBF0")
        etiqueta_logo.pack(side="left", padx=(0,10))

        marco_texto_logo = tk.Frame(marco_logo)
        marco_texto_logo.configure(bg="#EAFBF0")
        marco_texto_logo.pack(side="left")

        etiqueta_titulo = tk.Label(marco_texto_logo, text="NEUROCARE")
        etiqueta_titulo.configure(bg="#EAFBF0", fg="medium purple", font=("Quicksand",18,"bold"))
        etiqueta_titulo.pack(anchor="w")

        etiqueta_subtitulo = tk.Label(marco_texto_logo, text="Familiar / Cuidador")
        etiqueta_subtitulo.configure(bg="#EAFBF0", fg="dim gray", font=("Quicksand",11))
        etiqueta_subtitulo.pack(anchor="w")

#-------------------- CREAR CUENTA --------------------#

        marco_bienvenida = tk.Frame(self.marco_principal)
        marco_bienvenida.configure(width=600, height=180, bg="#EAFBF0")
        marco_bienvenida.pack(pady=(5,20))
        marco_bienvenida.pack_propagate(False)

#-------------------- TEXTO --------------------#

        marco_texto = tk.Frame(marco_bienvenida)
        marco_texto.configure(width=360, height=180, bg="#EAFBF0")
        marco_texto.pack(side="left", fill="y")
        marco_texto.pack_propagate(False)

        etiqueta_titulo = tk.Label(marco_texto, text="Crear cuenta")
        etiqueta_titulo.configure(bg="#EAFBF0", fg="black", font=("Quicksand",22,"bold"))
        etiqueta_titulo.pack(anchor="w", pady=(20,10), padx=10)

        etiqueta_descripcion = tk.Label(marco_texto,text="Ayúdanos a conocerte para que cuides\nmejor a tu ser querido.")
        etiqueta_descripcion.configure(bg="#EAFBF0",fg="dim gray",font=("Quicksand",12),justify="left")
        etiqueta_descripcion.pack(anchor="w", padx=10)

#-------------------- MASCOTA --------------------#

        marco_mascota = tk.Frame(marco_bienvenida)
        marco_mascota.configure(width=180, height=180, bg="#EAFBF0")
        marco_mascota.pack(side="right")
        marco_mascota.pack_propagate(False)

        self.imagen_mascota = tk.PhotoImage(file="NEUROCARE/funciones/recursos/masc.png")
        self.imagen_mascota = self.imagen_mascota.zoom(3,3)

        etiqueta_mascota = tk.Label(marco_mascota, image=self.imagen_mascota)
        etiqueta_mascota.configure(bg="#EAFBF0")
        etiqueta_mascota.pack(expand=True)


#-------------------- FORMULARIO --------------------#

        marco_formulario = tk.Frame(self.marco_principal)
        marco_formulario.configure(width=600, height=500, bg="white", relief="solid", bd=1)
        marco_formulario.pack(pady=(5,20))
        marco_formulario.pack_propagate(False)

#-------------------- NOMBRE --------------------#

        marco_nombre = tk.Frame(marco_formulario, bg="white")
        marco_nombre.configure(width=520, height=70)
        marco_nombre.pack(pady=(20,5))
        marco_nombre.pack_propagate(False)

        etiqueta_nombre = tk.Label(marco_nombre, text="Nombre completo")
        etiqueta_nombre.configure(bg="white", fg="black", font=("Quicksand",14,"bold"))
        etiqueta_nombre.pack(anchor="w")

        self.entry_nombre = tk.Entry(marco_nombre)
        self.entry_nombre.configure(font=("Arial",16), width=35, relief="solid")
        self.entry_nombre.pack(pady=(5,0))

#-------------------- CONTACTO --------------------#

        marco_contacto = tk.Frame(marco_formulario, bg="white")
        marco_contacto.configure(width=520, height=70)
        marco_contacto.pack(pady=(5,5))
        marco_contacto.pack_propagate(False)

        etiqueta_contacto = tk.Label(marco_contacto, text="Número de teléfono o correo electrónico")
        etiqueta_contacto.configure(bg="white", fg="black", font=("Quicksand",14,"bold"))
        etiqueta_contacto.pack(anchor="w")

        self.entry_contacto = tk.Entry(marco_contacto)
        self.entry_contacto.configure(font=("Arial",16), width=35, relief="solid")
        self.entry_contacto.pack(pady=(5,0))

#-------------------- PARENTESCO --------------------#

        marco_parentesco = tk.Frame(marco_formulario, bg="white")
        marco_parentesco.configure(width=520, height=70)
        marco_parentesco.pack(pady=(5,5))
        marco_parentesco.pack_propagate(False)

        etiqueta_parentesco = tk.Label(marco_parentesco, text="Parentesco con el paciente")
        etiqueta_parentesco.configure(bg="white", fg="black", font=("Quicksand",14,"bold"))
        etiqueta_parentesco.pack(anchor="w")

        self.combo_parentesco = ttk.Combobox(
            marco_parentesco,
            values=["Hijo(a)",
        "Padre / Madre",
        "Hermano(a)",
        "Abuelo(a)",
        "Nieto(a)",
        "Esposo(a)",
        "Cuidador(a)",
        "Otro familiar"
        ],state="readonly",width=33,font=("Arial",16))

        self.combo_parentesco.pack(pady=(5,0))
        self.combo_parentesco.set("Selecciona")

#-------------------- CONTRASEÑA --------------------#

        marco_contrasena = tk.Frame(marco_formulario, bg="white")
        marco_contrasena.configure(width=520, height=70)
        marco_contrasena.pack(pady=(5,5))
        marco_contrasena.pack_propagate(False)

        etiqueta_contrasena = tk.Label(marco_contrasena, text="Contraseña")
        etiqueta_contrasena.configure(bg="white", fg="black", font=("Quicksand",14,"bold"))
        etiqueta_contrasena.pack(anchor="w")

        self.entry_contrasena = tk.Entry(marco_contrasena)
        self.entry_contrasena.configure(font=("Arial",16), width=35, relief="solid", show="*")
        self.entry_contrasena.pack(pady=(5,0))

#-------------------- CONFIRMAR CONTRASEÑA --------------------#

        marco_confirmar = tk.Frame(marco_formulario, bg="white")
        marco_confirmar.configure(width=520, height=70)
        marco_confirmar.pack(pady=(5,10))
        marco_confirmar.pack_propagate(False)

        etiqueta_confirmar = tk.Label(marco_confirmar, text="Confirmar contraseña")
        etiqueta_confirmar.configure(bg="white", fg="black", font=("Quicksand",14,"bold"),)
        etiqueta_confirmar.pack(anchor="w")

        self.entry_confirmar = tk.Entry(marco_confirmar)
        self.entry_confirmar.configure(font=("Arial",16), width=35, relief="solid", show="*")
        self.entry_confirmar.pack(pady=(5,0))


#-------------------- BOTÓN CREAR CUENTA --------------------#

        marco_boton = tk.Frame(self.marco_principal)
        marco_boton.configure(width=600, height=80, bg="#EAFBF0")
        marco_boton.pack(pady=(5,20))
        marco_boton.pack_propagate(False)

        boton_crear = tk.Button(marco_boton, text="CREAR CUENTA")
        boton_crear.configure(bg="medium sea green",fg="white",font=("Quicksand",15,"bold"),relief="flat",bd=0, command=self.mensaje_proximo)
        boton_crear.config(width=24, height=2)
        boton_crear.pack(expand=True)


        
        
    def volver_rol(self):
        from seleccion_rol import rol
        self.ventana.withdraw()
        rol(self.ventana)
        
    def mensaje_proximo(self):
        messagebox.showinfo(
            "🛠️PROXIMAMENTE🛠️",
            "Esta funcion estara disponible en futuras versiones"
        )
            
                
            
if __name__ =="__main__":
    ventana = tk.Tk()
    app = registrar_familiar(ventana)
    ventana.mainloop()
    