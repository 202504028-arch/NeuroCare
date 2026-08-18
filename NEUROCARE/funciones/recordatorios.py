import tkinter as tk
import customtkinter as ctk
from conexion import conectarBd
from tkinter import ttk
#python NEUROCARE/funciones/recordatorios.py

class recordatorios1:

    def __init__(self, root, idPaciente):

        self.root = root
        self.idPaciente = idPaciente
        self.ventana = tk.Toplevel(root)

        self.ventana.title("NEUROCARE -- RECORDATORIOS")
        self.ventana.geometry("640x700+0+0")
        # Centrar ventana en pantalla
        self.ventana.update_idletasks()
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.resizable(False, False)

        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")

        self.crear_interfaz()
        

    def crear_interfaz(self):

#MENÚ INFERIOR (fijo, fuera del área con scroll)

        marco_menu = tk.Frame(self.ventana)
        marco_menu.configure(width=600, height=80, bg="white", relief="solid", bd=1)
        marco_menu.pack(side="bottom", pady=(0,10), padx=10)
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

#CANVAS 

        self.canvas = tk.Canvas(self.ventana)
        self.canvas.configure(bg="lavender", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

#BARRA DE SCROLL

        barra_scroll = ttk.Scrollbar(self.ventana)
        barra_scroll.configure(orient="vertical", command=self.canvas.yview)
        barra_scroll.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=barra_scroll.set)

#RUEDA DEL MOUSE (SCROLL)

        self.canvas.bind("<Enter>", lambda evento: self.canvas.bind_all(
            "<MouseWheel>",
            lambda e: self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")))
        self.canvas.bind("<Leave>", lambda evento: self.canvas.unbind_all("<MouseWheel>"))

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
            fg_color="#7C3AED",hover_color="#6D28D9",font=("Arial",28,"bold"),
            command=self.abrir_formulario)
        boton_agregar.pack(side="right")

#------------------------------------------------#
#                 FILTROS                        #
#------------------------------------------------#

        marco_filtros = tk.Frame(self.marco_principal,bg="lavender")

        marco_filtros.pack(fill="x",padx=20,pady=(5,20))

        self.btn_todos = ctk.CTkButton(marco_filtros,text="Todos",width=120,height=42,corner_radius=20,
                                       fg_color="#7C3AED",hover_color="#6D28D9",text_color="black",font=("Quicksand",15,"bold"))
        self.btn_todos.pack(side="left", padx=(40,30))

        self.btn_actividad = ctk.CTkButton(marco_filtros,text="Actividades",width=140,height=42,corner_radius=20,
                                           fg_color="white",hover_color="#6D28D9",text_color="black",border_width=2,border_color="#DDDDDD",
                                           font=("Quicksand",15), command=self.recordatorios_actividades)
        self.btn_actividad.pack(side="left", padx=(30,30))
        
        self.btn_medicos = ctk.CTkButton(marco_filtros,text="Medicos",width=140,height=42,corner_radius=20,
                                           fg_color="white",hover_color="#6D28D9",text_color="black",border_width=2,border_color="#DDDDDD",
                                           font=("Quicksand",15), command=self.recordatorios_medicos)
        self.btn_medicos.pack(side="left", padx=(20,40))

#------------------------------------------------#
#        CONTENEDOR RECORDATORIOS                #
#------------------------------------------------#

        self.contenedor = tk.Frame(self.marco_principal, bg="lavender")
        self.contenedor.configure(height=350)
        self.contenedor.pack(fill="both", expand=True, padx=20, pady=10)

        self.cargar_recordatorios()


    def abrir_actividades(self):
        from actividades import juegos
        self.ventana.withdraw()
        juegos(self.ventana, self.idPaciente)

    def abrir_inicio(self):
        from principal_paciente import principal
        self.ventana.withdraw()
        principal(self.ventana,self.idPaciente)
        
    def abrir_perfil(self):
        from perfil import usuario_perfil
        self.ventana.withdraw()
        usuario_perfil(self.ventana,self.idPaciente)



    def cargar_recordatorios(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()
        try:
            conexion = conectarBd()
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT idRecordatorio, titulo, tipoRecordatorio, descripcion, fechaHora, estado "
                "FROM recordatorio WHERE idPaciente = %s ORDER BY fechaHora ASC",
                (self.idPaciente,)
            )
            recordatorios = cursor.fetchall()
            cursor.close()
            conexion.close()
        except Exception as e:
            tk.Label(self.contenedor, text=f"Error: {e}",
                     bg="lavender", fg="red", font=("Quicksand", 11)).pack(pady=20)
            return
        if not recordatorios:
            tk.Label(self.contenedor, text="No hay recordatorios registrados.",
                     bg="lavender", fg="dim gray",
                     font=("Quicksand", 13)).pack(pady=40)
            return
        for rec in recordatorios:
            self.crear_tarjeta(rec)

    def crear_tarjeta(self, rec):
        import customtkinter as ctk2
        idRec, titulo, tipo, descripcion, fecha_hora, estado = rec
        if tipo == "Medico" or tipo == "Médico":
            color_borde = "#7C3AED"
            color_tag   = "#E9D5FF"
            color_tag_fg = "#7C3AED"
            emoji = "💊"
        else:
            color_borde = "#3B82F6"
            color_tag   = "#DBEAFE"
            color_tag_fg = "#1D4ED8"
            emoji = "🧠"
        color_estado = "#22C55E" if estado == "Completado" else "#F59E0B"
        tarjeta = ctk2.CTkFrame(self.contenedor, fg_color="white",
                                corner_radius=15, border_width=2,
                                border_color=color_borde)
        tarjeta.pack(fill="x", padx=5, pady=6)
        fila_top = tk.Frame(tarjeta, bg="white")
        fila_top.pack(fill="x", padx=15, pady=(12, 4))
        tk.Label(fila_top, text=emoji, bg="white", font=("Quicksand", 16)).pack(side="left")
        tk.Label(fila_top, text=titulo, bg="white", fg="black",
                 font=("Quicksand", 14, "bold")).pack(side="left", padx=(8, 0))
        import customtkinter as ctk3
        texto_estado = f"● {estado}"
        ctk3.CTkButton(fila_top, text=texto_estado, width=110, height=28,
                       corner_radius=20, fg_color=color_estado,
                       hover_color=color_estado, text_color="white",
                       font=("Quicksand", 11, "bold"),
                       command=lambda i=idRec, e=estado: self.toggle_estado(i, e)
                       ).pack(side="right")
        fila_mid = tk.Frame(tarjeta, bg="white")
        fila_mid.pack(fill="x", padx=15, pady=2)
        tk.Label(fila_mid, text=tipo, bg=color_tag, fg=color_tag_fg,
                 font=("Quicksand", 10, "bold"), padx=6, pady=2).pack(side="left")
        if descripcion:
            tk.Label(fila_mid, text=descripcion, bg="white", fg="dim gray",
                     font=("Quicksand", 11)).pack(side="left", padx=(10, 0))
        if fecha_hora:
            fecha_str = fecha_hora.strftime("%d/%m/%Y  %I:%M %p")
            tk.Label(tarjeta, text=f"🕐 {fecha_str}", bg="white", fg="gray",
                     font=("Quicksand", 11)).pack(anchor="w", padx=15, pady=(2, 4))
        fila_bot = tk.Frame(tarjeta, bg="white")
        fila_bot.pack(fill="x", padx=15, pady=(4, 12))
        ctk2.CTkButton(fila_bot, text="Eliminar", width=90, height=30,
                       corner_radius=8, fg_color="#FEE2E2", hover_color="#FECACA",
                       text_color="#DC2626", font=("Quicksand", 12),
                       command=lambda i=idRec: self.eliminar(i)).pack(side="right", padx=(8, 0))
        ctk2.CTkButton(fila_bot, text="Editar", width=90, height=30,
                       corner_radius=8, fg_color="#EDE9FE", hover_color="#DDD6FE",
                       text_color="#7C3AED", font=("Quicksand", 12),
                       command=lambda i=idRec, t=titulo: self.editar(i, t)).pack(side="right")

    def toggle_estado(self, idRecordatorio, estado_actual):
        nuevo_estado = "Pendiente" if estado_actual == "Completado" else "Completado"
        try:
            conexion = conectarBd()
            cursor = conexion.cursor()
            cursor.execute("UPDATE recordatorio SET estado = %s WHERE idRecordatorio = %s",
                           (nuevo_estado, idRecordatorio))
            conexion.commit()
            cursor.close()
            conexion.close()
            self.cargar_recordatorios()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showerror("Error", str(e), parent=self.ventana)

    def eliminar(self, idRecordatorio):
        from tkinter import messagebox
        if messagebox.askyesno("Eliminar", "¿Seguro que quieres eliminar este recordatorio?", parent=self.ventana):
            try:
                conexion = conectarBd()
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM recordatorio WHERE idRecordatorio = %s", (idRecordatorio,))
                conexion.commit()
                cursor.close()
                conexion.close()
                self.cargar_recordatorios()
            except Exception as e:
                from tkinter import messagebox as mb
                mb.showerror("Error", str(e), parent=self.ventana)

    def editar(self, idRecordatorio, titulo_actual):
        from tkinter import simpledialog, messagebox
        nuevo = simpledialog.askstring("Editar título", "Nuevo título:",
                                       initialvalue=titulo_actual, parent=self.ventana)
        if nuevo and nuevo.strip():
            try:
                conexion = conectarBd()
                cursor = conexion.cursor()
                cursor.execute("UPDATE recordatorio SET titulo = %s WHERE idRecordatorio = %s",
                               (nuevo.strip(), idRecordatorio))
                conexion.commit()
                cursor.close()
                conexion.close()
                self.cargar_recordatorios()
            except Exception as e:
                messagebox.showerror("Error", str(e), parent=self.ventana)

    def abrir_formulario(self):
        self.dialogo_tipo = tk.Toplevel(self.ventana)
        self.dialogo_tipo.title("Nuevo recordatorio")
        self.dialogo_tipo.geometry("340x220+560+280")
        self.dialogo_tipo.config(bg="lavender")
        self.dialogo_tipo.resizable(False, False)
        self.dialogo_tipo.transient(self.ventana)
        self.dialogo_tipo.grab_set()

        tk.Label(self.dialogo_tipo, text="¿Qué tipo de recordatorio\nquieres crear?",
                 bg="lavender", fg="black",
                 font=("Quicksand", 15, "bold"), justify="center").pack(pady=(25, 20))

        ctk.CTkButton(self.dialogo_tipo, text="🧠  Actividad", width=220, height=42,
                      corner_radius=12, fg_color="#3B82F6", hover_color="#2563EB",
                      font=("Quicksand", 13, "bold"),
                      command=self.elegir_actividad).pack(pady=6)

        ctk.CTkButton(self.dialogo_tipo, text="💊  Médico", width=220, height=42,
                      corner_radius=12, fg_color="#7C3AED", hover_color="#6D28D9",
                      font=("Quicksand", 13, "bold"),
                      command=self.elegir_medico).pack(pady=6)

    def elegir_actividad(self):
        self.dialogo_tipo.destroy()
        from agregar_recordatorio_actividad import agregar_recordatorio_actividad
        agregar_recordatorio_actividad(self.ventana, self.idPaciente, self.cargar_recordatorios)

    def elegir_medico(self):
        self.dialogo_tipo.destroy()
        from agregar_recordatorio import agregar_recordatorio
        agregar_recordatorio(self.ventana, self.idPaciente, self.cargar_recordatorios)

    def recordatorios_actividades(self):
        from recordatorios_actividades import recordatorios_actividadees
        self.ventana.withdraw()
        recordatorios_actividadees(self.ventana,self.idPaciente)

    def recordatorios_medicos(self):
        from recordatorios_medicos import recordatorios_medicoos
        self.ventana.withdraw()
        recordatorios_medicoos(self.ventana,self.idPaciente)
    
if __name__ == "__main__":

    ventana = tk.Tk()
    ventana.withdraw()

    idPaciente = 1

    app = recordatorios1(
        ventana,
        idPaciente
    )

    ventana.mainloop()