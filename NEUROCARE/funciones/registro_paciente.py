from conexion import conectarBd
from principal_paciente import principal
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
                                    #  python NEUROCARE/funciones/registro_paciente.py
class registrar_paciente:
    
    def __init__(self,root):
        self.root = root
        self.ventana = tk.Toplevel(root)
        
        self.ventana.title(" NEUROCARE -- REGISTRO PACIENTE")
        self.ventana.geometry("650x780+500+10")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        
# BOTÓN VOLVER

        marco_boton_volver = tk.Frame(self.ventana, bg="lavender")
        marco_boton_volver.configure(width=650, height=50)
        marco_boton_volver.pack(fill="x", pady=(10, 0))
        marco_boton_volver.pack_propagate(False)

        boton_volver = tk.Button(marco_boton_volver,text="<--")
        boton_volver.configure(fg="black", bg="white", font=("Quicksand", 10, "bold"), command=self.volver_rol)
        boton_volver.pack(side="left",)

#CANVAS 
        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="lavender", highlightthickness=0)
        self.canvas.pack(side="left",fill="both", expand=True)
        
        self.scrollbar = tk.Scrollbar(self.ventana, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.configure(command=self.canvas.yview)
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        #kness hace que el tkinter no dibuje un borde negro en el canvas
        #fill "both" ocupar todo el espacio y expand crece cuando la ventana se expande 
        #fill y = hace que la barra ocupe todo el alto de la ventana
       
        
# MARCO DEL FORMULARIO

        self.marco_formulario = tk.Frame(self.canvas, bg="lavender")
        self.marco_formulario.configure(width=560, height=680)
        self.canvas.create_window((325,0), window=self.marco_formulario, anchor="n")
        
        self.marco_formulario.bind("<Configure>",
                                   self.actualizar_scroll)
        
        # el frame se queda guardado en el canva y canvas no usa pack normalmente, xy
        # para mostrar los frame,
         #el windos es decirle a canva que cree un espacio para colocar un widgets 
         # y se le dice con window= cual colocar, el (0,0) es para indicar las coordenadas
         #bbxo = calculael tamaño de todo el contenido que hay dentro del canvas


        marco_logo = tk.Frame(self.marco_formulario, bg="lavender")
        marco_logo.configure(width=560, height=90)
        marco_logo.pack(pady=(10, 15))
        marco_logo.pack_propagate(False)
        
# Imagen del logo
        marco_imagen_logo = tk.Frame(marco_logo, bg="lavender")
        marco_imagen_logo.configure(width=90, height=90)
        marco_imagen_logo.pack(side="left", padx=(20, 15))
        marco_imagen_logo.pack_propagate(False)

        self.imagen_logo = tk.PhotoImage(file="NEUROCARE/funciones/recursos/cerebro.png")
        self.imagen_logo = self.imagen_logo.subsample(2,2)
        etiqueta_logo = tk.Label(marco_imagen_logo, image=self.imagen_logo, bg="lavender")
        etiqueta_logo.pack(anchor="center")



# Texto del logo
        marco_texto_logo = tk.Frame(marco_logo, bg="lavender")
        marco_texto_logo.configure(width=300, height=90)
        marco_texto_logo.pack(side="left")
        marco_texto_logo.pack_propagate(False)
        
        etiqueta_neuro = tk.Label(marco_texto_logo, text="NEUROCARE")
        etiqueta_neuro.configure(fg="purple", bg= "lavender", font=("Quicksand",26,"bold"))
        etiqueta_neuro.pack(side="top", anchor="w")
        
        etiqueta_paciente = tk.Label(marco_texto_logo, text="Paciente")
        etiqueta_paciente.configure(fg="dim gray", bg="lavender", font=("Arial", 15))
        etiqueta_paciente.pack(side="top", anchor="w", pady=3)

# TÍTULO

        marco_titulo = tk.Frame(self.marco_formulario, bg="lavender")
        marco_titulo.configure(width=560, height=80)
        marco_titulo.pack(pady=(0, 20))
        marco_titulo.pack_propagate(False)
        
        etiqueta_crear_cuenta = tk.Label(marco_titulo, text="Crear Cuenta")
        etiqueta_crear_cuenta.configure(fg="black", bg="lavender", font=("Arial", 22, "bold"))
        etiqueta_crear_cuenta.pack(side="top", anchor="w")
        
        etiqueta_cuenta_texto = tk.Label(marco_titulo, text="Completa tus datos para comenzar.")
        etiqueta_cuenta_texto.configure(fg="dim gray", bg="lavender", font=("Arial", 15,))
        etiqueta_cuenta_texto.pack(side="top", anchor="w", pady=3)
        

# NOMBRE COMPLETO

        marco_nombre = tk.Frame(self.marco_formulario, bg="lavender")
        marco_nombre.configure(width=560, height=80)
        marco_nombre.pack(pady=(0, 10))
        marco_nombre.pack_propagate(False)

        etiqueta_nombre_completo = tk.Label(marco_nombre, text="Nombre Completo")
        etiqueta_nombre_completo.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_nombre_completo.pack(side="top", anchor="w")
        
        self.entry_nombre = tk.Entry(marco_nombre, bd=1)
        self.entry_nombre.configure( bg="white", font=("Arial",18), width=40, relief="solid", fg="gray")
        self.entry_nombre.insert(0,"ej.panfilo pancracio de la cruz")
        self.entry_nombre.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_nombre(event):
            if self.entry_nombre.get() =="ej.panfilo pancracio de la cruz":
                self.entry_nombre.delete(0, tk.END)
                self.entry_nombre.configure(fg="black")
        
        def poner_transfondo_nombre(event):
            if self.entry_nombre.get()=="":
                self.entry_nombre.insert(0,"ej.panfilo pancracio de la cruz")
                self.entry_nombre.configure(fg="gray")
            else:
                self.entry_nombre.configure(fg="black")
        
        self.entry_nombre.bind("<FocusIn>",
                            quitar_transfondo_nombre)
        
        self.entry_nombre.bind("<FocusOut>",
                            poner_transfondo_nombre)
                


# ==========================
# FILA DE DATOS PERSONALES
# ==========================

        marco_fila_datos = tk.Frame(self.marco_formulario, bg="lavender")
        marco_fila_datos.configure(width=560, height=80)
        marco_fila_datos.pack(pady=(0, 10))
        marco_fila_datos.pack_propagate(False)

# --------------------------
# EDAD
# --------------------------

        marco_edad = tk.Frame(marco_fila_datos, bg="lavender")
        marco_edad.configure(width=170, height=80)
        marco_edad.pack(side="left")
        marco_edad.pack_propagate(False)

        etiqueta_edad = tk.Label(marco_edad, text="Edad")
        etiqueta_edad.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_edad.pack(side="top", anchor="w")
        
        self.entry_edad = tk.Entry(marco_edad, bd=1)
        self.entry_edad.configure( bg="white", font=("Arial",18), width=20, relief="solid", fg="gray")
        self.entry_edad.insert(0,"ej.72")
        self.entry_edad.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_edad(event):
            if self.entry_edad.get() =="ej.72":
                self.entry_edad.delete(0, tk.END)
                self.entry_edad.configure(fg="black")
        
        def poner_transfondo_edad(event):
            if self.entry_edad.get()=="":
                self.entry_edad.insert(0,"ej.72")
                self.entry_edad.configure(fg="gray")
            else:
                self.entry_edad.configure(fg="black")
            
        
        self.entry_edad.bind("<FocusIn>",
                            quitar_transfondo_edad)
        
        self.entry_edad.bind("<FocusOut>",
                            poner_transfondo_edad)
        
    
# --------------------------
# FECHA DE NACIMIENTO
# --------------------------

        marco_fecha_nacimiento = tk.Frame(marco_fila_datos, bg="lavender")
        marco_fecha_nacimiento.configure(width=370, height=80)
        marco_fecha_nacimiento.pack(side="right")
        marco_fecha_nacimiento.pack_propagate(False)

        etiqueta_fecha_nacimiento = tk.Label(marco_fecha_nacimiento, text="Fecha de nacimiento")
        etiqueta_fecha_nacimiento.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_fecha_nacimiento.pack(side="top", anchor="w")
        
        self.entry_nacimiento = tk.Entry(marco_fecha_nacimiento, bd=1)
        self.entry_nacimiento.configure( bg="white", font=("Arial",18), width=25, relief="solid", fg="gray")
        self.entry_nacimiento.insert(0,"ej.2000-03-25")
        self.entry_nacimiento.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_nacimiento(event):
            if self.entry_nacimiento.get() =="ej.2000-03-25":
                self.entry_nacimiento.delete(0, tk.END)
                self.entry_nacimiento.configure(fg="black")
        
        def poner_transfondo_nacimiento(event):
            if self.entry_nacimiento.get()=="":
                self.entry_nacimiento.insert(0,"ej.2000-03-25")
                self.entry_nacimiento.configure(fg="gray")
            else:
                self.entry_nacimiento.configure(fg="black")
            
        
        self.entry_nacimiento.bind("<FocusIn>",
                            quitar_transfondo_nacimiento)
        
        self.entry_nacimiento.bind("<FocusOut>",
                            poner_transfondo_nacimiento)


# ==========================
# contacto
# ==========================

        marco_contacto = tk.Frame(self.marco_formulario, bg="lavender")
        marco_contacto.configure(width=560, height=80)
        marco_contacto.pack(pady=(0, 10))
        marco_contacto.pack_propagate(False)
        
        etiqueta_contacto = tk.Label(marco_contacto, text="Correo o numero telefonico")
        etiqueta_contacto.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_contacto.pack(side="top", anchor="w")
        
        self.entry_contacto = tk.Entry(marco_contacto, bd=1)
        self.entry_contacto.configure( bg="white", font=("Arial",18), width=40, relief="solid", fg="gray")
        self.entry_contacto.insert(0,"ej.74412 or panfilo@gmail.com")
        self.entry_contacto.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_contacto(event):
            if self.entry_contacto.get() =="ej.74412 or panfilo@gmail.com":
                self.entry_contacto.delete(0, tk.END)
                self.entry_contacto.configure(fg="black")
        
        def poner_transfondo_contacto(event):
            if self.entry_contacto.get()=="":
                self.entry_contacto.insert(0,"ej.74412 or panfilo@gmail.com")
                self.entry_contacto.configure(fg="gray")
            else:
                self.entry_contacto.configure(fg="black")
            
        
        self.entry_contacto.bind("<FocusIn>",
                            quitar_transfondo_contacto)
        
        self.entry_contacto.bind("<FocusOut>",
                            poner_transfondo_contacto)
                

# ==========================
# INFORMACIÓN ADICIONAL
# ==========================

        marco_info_adicional = tk.Frame(self.marco_formulario, bg="lavender")
        marco_info_adicional.configure(width=560, height=40)
        marco_info_adicional.pack(pady=(0, 10))
        marco_info_adicional.pack_propagate(False)
        
        etiqueta_adicional = tk.Label(marco_info_adicional, text="Informacion adicional (Opcional)")
        etiqueta_adicional.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_adicional.pack(side="left")


# ==========================
# FILA MÉDICA 1
# ==========================

        marco_fila_medica1 = tk.Frame(self.marco_formulario, bg="lavender")
        marco_fila_medica1.configure(width=560, height=80)
        marco_fila_medica1.pack(pady=(0, 10))
        marco_fila_medica1.pack_propagate(False)


# --------------------------
# SEXO
# --------------------------

        marco_sexo = tk.Frame(marco_fila_medica1, bg="lavender")
        marco_sexo.configure(width=260, height=80)
        marco_sexo.pack(side="left")
        marco_sexo.pack_propagate(False)
        
        etiqueta_sexo = tk.Label(marco_sexo, text="Sexo")
        etiqueta_sexo.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_sexo.pack(side="top", anchor="w")
        
        self.combo_sexo = ttk.Combobox(marco_sexo, values=["Femenino","Masculino","Otro"], state="readonly",width=18, 
                                       font=("Arial", 18))
        self.combo_sexo.pack(anchor="w", pady=5)
        self.combo_sexo.set("selecciona")
        
# --------------------------
# ALTURA
# --------------------------

        marco_altura = tk.Frame(marco_fila_medica1, bg="lavender")
        marco_altura.configure(width=260, height=80)
        marco_altura.pack(side="right")
        marco_altura.pack_propagate(False)

        etiqueta_altura = tk.Label(marco_altura, text="Altura (cm)")
        etiqueta_altura.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_altura.pack(side="top", anchor="w")
        
        self.entry_altura = tk.Entry(marco_altura, bd=1)
        self.entry_altura.configure( bg="white", font=("Arial",18), width=17, relief="solid", fg="gray")
        self.entry_altura.insert(0,"172")
        self.entry_altura.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_altura(event):
            if self.entry_altura.get() =="172":
                self.entry_altura.delete(0, tk.END)
                self.entry_altura.configure(fg="black")
        
        def poner_transfondo_altura(event):
            if self.entry_altura.get()=="":
                self.entry_altura.insert(0,"172")
                self.entry_altura.configure(fg="gray")
            else:
                self.entry_altura.configure(fg="black")
            
        
        self.entry_altura.bind("<FocusIn>",
                            quitar_transfondo_altura)
        
        self.entry_altura.bind("<FocusOut>",
                            poner_transfondo_altura)


# ==========================
# FILA MÉDICA 2
# ==========================

        marco_fila_medica2 = tk.Frame(self.marco_formulario, bg="lavender")
        marco_fila_medica2.configure(width=560, height=80)
        marco_fila_medica2.pack(pady=(0, 10))
        marco_fila_medica2.pack_propagate(False)


# --------------------------
# TIPO DE SANGRE
# --------------------------

        marco_tipo_sangre = tk.Frame(marco_fila_medica2, bg="lavender")
        marco_tipo_sangre.configure(width=260, height=80)
        marco_tipo_sangre.pack(side="left")
        marco_tipo_sangre.pack_propagate(False)
        
        etiqueta_sangre = tk.Label(marco_tipo_sangre, text="Tipo de sangre")
        etiqueta_sangre.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_sangre.pack(side="top", anchor="w")
        
        self.combo_sangre = ttk.Combobox(marco_tipo_sangre, values=["A+","A-","B+","B-","AB+","AB-","O+","O-"],
                                         state="readonly",width=18, 
                                       font=("Arial", 18))
        self.combo_sangre.pack(anchor="w", pady=5)
        self.combo_sangre.set("selecciona")

# --------------------------
# ALERGIAS
# --------------------------

        marco_alergias = tk.Frame(marco_fila_medica2, bg="lavender")
        marco_alergias.configure(width=260, height=80)
        marco_alergias.pack(side="right")
        marco_alergias.pack_propagate(False)
        
        etiqueta_alergias = tk.Label(marco_alergias, text="Alergias")
        etiqueta_alergias.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_alergias.pack(side="top", anchor="w")
        
        self.entry_alergias = tk.Entry(marco_alergias, bd=1)
        self.entry_alergias.configure( bg="white", font=("Arial",18), width=17, relief="solid", fg="gray")
        self.entry_alergias.insert(0,"ej.ninguna")
        self.entry_alergias.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_alergias(event):
            if self.entry_alergias.get() =="ej.ninguna":
                self.entry_alergias.delete(0, tk.END)
                self.entry_alergias.configure(fg="black")
        
        def poner_transfondo_alergias(event):
            if self.entry_alergias.get()=="":
                self.entry_alergias.insert(0,"ej.ninguna")
                self.entry_alergias.configure(fg="gray")
            else:
                self.entry_alergias.configure(fg="black")
            
        
        self.entry_alergias.bind("<FocusIn>",
                            quitar_transfondo_alergias)
        
        self.entry_alergias.bind("<FocusOut>",
                            poner_transfondo_alergias)

# ENFERMEDAD CRÓNICA

        marco_enfermedad = tk.Frame(self.marco_formulario, bg="lavender")
        marco_enfermedad.configure(width=560, height=80)
        marco_enfermedad.pack(pady=(0, 20))
        marco_enfermedad.pack_propagate(False)

        etiqueta_enfermedad = tk.Label(marco_enfermedad, text="enfermedad cronica")
        etiqueta_enfermedad.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_enfermedad.pack(side="top", anchor="w")
        
        self.entry_enfermedad = tk.Entry(marco_enfermedad, bd=1)
        self.entry_enfermedad.configure( bg="white", font=("Arial",18), width=40, relief="solid", fg="gray")
        self.entry_enfermedad.insert(0,"ej.Diabetes, Hipertension,Etc")
        self.entry_enfermedad.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_enfermedad(event):
            if self.entry_enfermedad.get() =="ej.Diabetes, Hipertension,Etc":
                self.entry_enfermedad.delete(0, tk.END)
                self.entry_enfermedad.configure(fg="black")
        
        def poner_transfondo_enfermedad(event):
            if self.entry_enfermedad.get()=="":
                self.entry_enfermedad.insert(0,"ej.Diabetes, Hipertension,Etc")
                self.entry_enfermedad.configure(fg="gray")
            else:
                self.entry_enfermedad.configure(fg="black")
            
        
        self.entry_enfermedad.bind("<FocusIn>",
                            quitar_transfondo_enfermedad)
        
        self.entry_enfermedad.bind("<FocusOut>",
                            poner_transfondo_enfermedad)

# ==========================
# CONTRASEÑA
# ==========================

        marco_emergencia = tk.Frame(self.marco_formulario, bg="lavender")
        marco_emergencia.configure(width=560, height=100)
        marco_emergencia.pack(pady=(0, 20))
        marco_emergencia.pack_propagate(False)

        etiqueta_emergencia = tk.Label(marco_emergencia, text="Contacto de emergencia")
        etiqueta_emergencia.configure(fg="black", bg="lavender", font=("Arial", 19,))
        etiqueta_emergencia.pack(side="top", anchor="w")
        
        self.entry_emergencia = tk.Entry(marco_emergencia, bd=1)
        self.entry_emergencia.configure( bg="white", font=("Arial",18), width=40, relief="solid", fg="gray")
        self.entry_emergencia.insert(0,"ej.744123467")
        self.entry_emergencia.pack(side="top", anchor="w", pady=5, padx=2)
        
        def quitar_transfondo_emergencia(event):
            if self.entry_emergencia.get() =="ej.744123467":
                self.entry_emergencia.delete(0, tk.END)
                self.entry_emergencia.configure(fg="black")
        
        def poner_transfondo_emergencia(event):
            if self.entry_emergencia.get()=="":
                self.entry_emergencia.insert(0,"ej.744123467")
                self.entry_emergencia.configure(fg="gray")
            else:
                self.entry_emergencia.configure(fg="black")
            
        
        self.entry_emergencia.bind("<FocusIn>",
                            quitar_transfondo_emergencia)
        
        self.entry_emergencia.bind("<FocusOut>",
                            poner_transfondo_emergencia)
        
        etiqueta_informativa_emergencia = tk.Label(marco_emergencia, text="(Debes rellenar este campo para acceder al boton SOS)")
        etiqueta_informativa_emergencia.configure(fg="dim gray", bg="lavender", font=("Arial",14))
        etiqueta_informativa_emergencia.pack(side="bottom", anchor="s")

        marco_contrasena = tk.Frame(self.marco_formulario,bg="lavender")
        marco_contrasena.pack(pady=10)
    

# ---------- Contraseña ----------

        marco_pass = tk.Frame(marco_contrasena,bg="lavender")
        marco_pass.pack(side="left", padx=20)

        tk.Label(marco_pass,text="Contraseña (obligatorio)",font=("Arial", 14, "bold"),
        bg="lavender").pack(anchor="w")

        self.entry_contrasena = tk.Entry(marco_pass,font=("Arial", 18),width=20, bd=1, relief="solid", fg="gray")
        self.entry_contrasena.insert(0,"Min.6")
        self.entry_contrasena.pack(pady=5)
        
        def quitar_transfondo_contraseña(event):
            if self.entry_contrasena.get() =="Min.6":
                self.entry_contrasena.delete(0, tk.END)
                self.entry_contrasena.configure(fg="black")
            
        
        def poner_transfondo_contraseña(event):
            if self.entry_contrasena.get()=="":
                self.entry_contrasena.insert(0,"Min.6")
                self.entry_contrasena.configure(fg="gray")
            else:
                self.entry_contrasena.configure(fg="black")
                
            
        
        self.entry_contrasena.bind("<FocusIn>",
                            quitar_transfondo_contraseña)
        
        self.entry_contrasena.bind("<FocusOut>",
                            poner_transfondo_contraseña)

# ---------- Confirmar ----------

        marco_confirmar = tk.Frame(marco_contrasena,bg="lavender")
        marco_confirmar.pack(side="left", padx=20)

        tk.Label(marco_confirmar,text="Confirmar",font=("Arial", 14, "bold"),bg="lavender").pack(anchor="w")

        self.entry_confirmar = tk.Entry(marco_confirmar,font=("Arial", 18),width=15, bd=1, relief="solid", fg="gray")
        self.entry_confirmar.insert(0,"Repite")
        self.entry_confirmar.pack(pady=5)

        def quitar_transfondo_confirmar(event):
            if self.entry_confirmar.get() =="Repite":
                self.entry_confirmar.delete(0, tk.END)
                self.entry_confirmar.configure(fg="black")
        
        def poner_transfondo_confrimar(event):
            if self.entry_confirmar.get()=="":
                self.entry_confirmar.insert(0,"Repite")
                self.entry_confirmar.configure(fg="gray")
            else:
                self.entry_confirmar.configure(fg="black")
            
        
        self.entry_confirmar.bind("<FocusIn>",
                            quitar_transfondo_confirmar)
        
        self.entry_confirmar.bind("<FocusOut>",
                            poner_transfondo_confrimar)

# BOTÓN REGISTRAR


        marco_boton_registro = tk.Frame(self.marco_formulario, bg="lavender")
        marco_boton_registro.configure(width=560, height=80)
        marco_boton_registro.pack(pady=(10, 15))
        marco_boton_registro.pack_propagate(False)

        boton_registro = tk.Button(marco_boton_registro,text="Registrarse")
        boton_registro.configure(fg="white", bg="purple", font=("Quicksand", 18, "bold"), width=50, command=self.registrar_datos )
        boton_registro.pack(pady=10)


# ESPACIO INFERIOR VISUAL


        marco_espacio_final = tk.Frame(self.marco_formulario, bg="lavender")
        marco_espacio_final.configure(width=560, height=30)
        marco_espacio_final.pack()
        marco_espacio_final.pack_propagate(False)
        
    def actualizar_scroll(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def volver_rol(self):
        from seleccion_rol import rol
        self.ventana.withdraw()
        rol(self.ventana)
    
    def registrar_datos(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.entry_edad.get()
        fecha_nacimiento = self.entry_nacimiento.get()
        contacto = self.entry_contacto.get()
        sexo = self.combo_sexo.get()
        altura = self.entry_altura.get()
        sangre = self.combo_sangre.get()
        alergias = self.entry_alergias.get()
        enfermedad = self.entry_enfermedad.get()
        contraseña = self.entry_contrasena.get()
        confirmar = self.entry_confirmar.get()
        
        if (nombre =="ej.panfilo pancracio de la cruz" or edad =="ej.72" or 
            fecha_nacimiento =="ej.2000-03-25" or
            contacto =="ej.74412 or panfilo@gmail.com" or  
            contraseña =="Min.6" or confirmar =="Repite"):
            messagebox.showwarning("campos incompletos",
                                           "debes de completar todos los campos")
            return
        
        #nombre
        if len(nombre) <3:
            messagebox.showwarning(
                "Nombre",
                "El nombre debe de tener minimo 3 caracteres"
            )
            return
        if len(nombre)>30:
            messagebox.showwarning(
                "Nombre",
                "El nombre no debe de tener mas de 30 caracteres"
            )
            return
         
        #contraseña
        if len(contraseña) <6:
            messagebox.showwarning(
                "contraseña",
                "la contraseña debe de tener minimo 6 caracteres."
            )
            return
        
        if len(contraseña)>30:
            messagebox.showwarning(
                "Contraseña",
                "La contraseña no debe de contener mas de 30 caracteres"
            )
            return
        
        #este igual
        if contraseña != confirmar:
            messagebox.showwarning(
                "contraseña",
                "la contraseñas no coinciden."
            )
            return
        
        #edad
        if not edad.isdigit():
            messagebox.showwarning(
                "Edad",
                "La edad debe de ser un numero."
            )
            return
        
        if int(edad)<1 or int(edad)>100:
            messagebox.showwarning(
                "Edad",
                "La edad debe de estar entre 1 a 100 años."
            ) 
            return
        
        #altura
        try:
            float(altura)
        except ValueError:
            messagebox.showwarning(
                "Altura",
                "La altura debe ser un numero"
            )
            return
        
        if float(altura)<50 or float(altura)> 300:
            messagebox.showwarning(
                "Altura",
                "La altura debe estar entre 50 a 300 cm."
            )
            return
         #opcionales
        if sexo=="selecciona":
            sexo = None
            
        if sangre =="selecciona":
            sangre = None
        
        if alergias == "ej.ninguna" or alergias =="":
            alergias = None
        
        if enfermedad =="ej.Diabetes, Hipertension,Etc" or enfermedad =="":
            enfermedad = None
            
        if altura =="172" or altura =="":
            altura = None
        
        #fecha
        try:
            datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning(
                "Fecha",
                "La fecha debe de tener el formato AAAA-MM-DD"
            )
            return
        
        if "@" in contacto:
            if ("@" not in contacto or "." not in contacto or len(contacto)<6):
                messagebox.showwarning(
                    "Correo",
                    "Ingresa un correo electronico valido."
                )
                return
        else:
            if not contacto.isdigit():
                messagebox.showwarning(
                    "Telefono",
                    "El telefono solo debe de contener numeros."
                )
                return
            if len(contacto) != 10:
                messagebox.showwarning(
                    "Telefono",
                    "El telefono debe tener exactamente 10 digitos."
                )
                return
                
        
        conexion = conectarBd()
        cursor = conexion.cursor()
        
        try:
            sql = "SELECT * FROM paciente WHERE contacto=%s"
            valores =(contacto,)
            cursor.execute(sql, valores)
            usuario = cursor.fetchone()
        
            if usuario:
                messagebox.showwarning(
                    "contacto registrado",
                    "este contacto ya se encuentra registrado"
                )
                return
        
            sql ="""
            INSERT INTO paciente (nombreCompleto,
                    edad,fechaNacimiento,contacto,contrasena)
                    VALUES (%s,%s,%s,%s,%s)"""
        
            valores =(nombre, edad,fecha_nacimiento,contacto,contraseña)
            cursor.execute(sql, valores)
            conexion.commit()
        
            id_paciente = cursor.lastrowid
        
            sql = """
            INSERT INTO caracteristicasPaciente (idpaciente,sexo,
            altura,tipoSangre,alergias,enfermedadCronica)
            VALUES (%s,%s,%s,%s,%s,%s)"""
        
            valores =(id_paciente,sexo,altura,sangre,alergias,enfermedad)
            cursor.execute(sql, valores)
            conexion.commit()
            
            messagebox.showinfo(
            "Registro exitoso",
            "El paciente se registro correctamente :)"
        )
        
            self.ventana.destroy()
            from principal_paciente import principal
            principal(self.root)
        
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"ocurrio un error: \n{e}"
            )
        
        finally:
            cursor.close()
            conexion.close()
        


        
        
if __name__ =="__main__":
    ventana = tk.Tk()
    app = registrar_paciente(ventana)
    ventana.mainloop()