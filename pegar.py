import tkinter as tk
from tkinter import ttk

class MiPerfilPaciente:
    def __init__(self, root):
        self.root = root
        self.root.title("NeuroCare - Mi Perfil")
        self.root.geometry("400x700")
        self.root.configure(bg="white smoke")
        
        self.crear_interfaz()

    def crear_interfaz(self):
        # ----------------------------------------
        # FRAME PRINCIPAL (CONTENEDOR CON SCROLL)
        # ----------------------------------------
        self.main_canvas = tk.Canvas(self.root, bg="white smoke", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas, bg="white smoke")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )

        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # ----------------------------------------
        # TITULO
        # ----------------------------------------
        self.frame_titulo = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_titulo.pack(fill="x", padx=20, pady=(20, 10))
        self.frame_titulo.pack_propagate(False)
        self.frame_titulo.configure(height=40)

        tk.Label(
            self.frame_titulo, 
            text="Mi perfil", 
            font=("Quicksand", 22, "bold"), 
            bg="white smoke", 
            fg="black"
        ).pack(anchor="w")

        # ----------------------------------------
        # TARJETA INFORMACION PERSONAL
        # ----------------------------------------
        self.frame_tarjeta_perfil = tk.Frame(
            self.scrollable_frame, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_tarjeta_perfil.pack(fill="x", padx=20, pady=10)
        self.frame_tarjeta_perfil.pack_propagate(False)
        self.frame_tarjeta_perfil.configure(height=260)

        # Franja superior de la tarjeta (Púrpura)
        self.frame_header_tarjeta = tk.Frame(self.frame_tarjeta_perfil, bg="MediumPurple3")
        self.frame_header_tarjeta.pack(fill="x", padx=10, pady=10)
        self.frame_header_tarjeta.pack_propagate(False)
        self.frame_header_tarjeta.configure(height=65)

        tk.Label(
            self.frame_header_tarjeta, 
            text="PACIENTE NEUROCARE", 
            font=("Quicksand", 9, "bold"), 
            bg="MediumPurple3", 
            fg="Lavender"
        ).pack(anchor="nw", padx=15, pady=(8, 0))

        tk.Label(
            self.frame_header_tarjeta, 
            text="Sisi", 
            font=("Quicksand", 16, "bold"), 
            bg="MediumPurple3", 
            fg="white"
        ).pack(anchor="nw", padx=15, pady=(0, 8))

        # Cuerpo de datos clínicos de la tarjeta
        self.frame_datos_grid = tk.Frame(self.frame_tarjeta_perfil, bg="white")
        self.frame_datos_grid.pack(fill="both", expand=True, padx=15, pady=10)

        # Columna Izquierda
        self.frame_col_izq = tk.Frame(self.frame_datos_grid, bg="white")
        self.frame_col_izq.pack(side="left", fill="both", expand=True)

        tk.Label(self.frame_col_izq, text="EDAD", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="72", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="CELULAR", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="1234537890", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="ETAPA DE ALZHEIMER", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_izq, text="MÉDICO", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_izq, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w")

        # Columna Derecha
        self.frame_col_der = tk.Frame(self.frame_datos_grid, bg="white")
        self.frame_col_der.pack(side="right", fill="both", expand=True)

        tk.Label(self.frame_col_der, text="TIPO DE SANGRE", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_der, text="—", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_der, text="EMERGENCIA", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w")
        tk.Label(self.frame_col_der, text="123456789", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w", pady=(0, 8))

        tk.Label(self.frame_col_der, text="ALERGIAS", font=("Quicksand", 8, "bold"), bg="white", fg="dim gray").pack(anchor="w", pady=(18, 0))
        tk.Label(self.frame_col_der, text="Ninguna", font=("Quicksand", 12, "bold"), bg="white", fg="black").pack(anchor="w")

        # ----------------------------------------
        # RESUMEN SEMANAL
        # ----------------------------------------
        self.frame_titulo_resumen = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_titulo_resumen.pack(fill="x", padx=20, pady=(15, 5))
        self.frame_titulo_resumen.pack_propagate(False)
        self.frame_titulo_resumen.configure(height=30)

        tk.Label(
            self.frame_titulo_resumen, 
            text="Resumen semanal", 
            font=("Quicksand", 16, "bold"), 
            bg="white smoke", 
            fg="black"
        ).pack(anchor="w")

        self.frame_resumen_contenedor = tk.Frame(self.scrollable_frame, bg="white smoke")
        self.frame_resumen_contenedor.pack(fill="x", padx=20, pady=5)
        self.frame_resumen_contenedor.pack_propagate(False)
        self.frame_resumen_contenedor.configure(height=110)

        # Tarjeta Actividades completadas
        self.frame_card_act = tk.Frame(
            self.frame_resumen_contenedor, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_card_act.pack(side="left", fill="both", expand=True, padx=(0, 5))
        self.frame_card_act.pack_propagate(False)

        tk.Label(self.frame_card_act, text="0", font=("Quicksand", 16, "bold"), bg="white", fg="black").pack(pady=(25, 0))
        tk.Label(self.frame_card_act, text="Actividades completadas", font=("Quicksand", 8), bg="white", fg="dim gray").pack()

        # Tarjeta Ejercicios realizados
        self.frame_card_ej = tk.Frame(
            self.frame_resumen_contenedor, 
            bg="white", 
            highlightbackground="gainsboro", 
            highlightthickness=1
        )
        self.frame_card_ej.pack(side="right", fill="both", expand=True, padx=(5, 0))
        self.frame_card_ej.pack_propagate(False)

        tk.Label(self.frame_card_ej, text="0", font=("Quicksand", 16, "bold"), bg="white", fg="black").pack(pady=(25, 0))
        tk.Label(self.frame_card_ej, text="Ejercicios realizados", font=("Quicksand", 8), bg="white", fg="dim gray").pack()

        # ----------------------------------------
        # BARRA DE NAVEGACION INFERIOR (NAVBAR)
        # ----------------------------------------
        self.frame_navbar = tk.Frame(self.root, bg="white", height=60, highlightbackground="gainsboro", highlightthickness=1)
        self.frame_navbar.pack(side="bottom", fill="x")
        self.frame_navbar.pack_propagate(False)

        # Se distribuyen los 5 botones del menú inferior de forma uniforme
        self.frame_navbar.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        tk.Button(self.frame_navbar, text="🏠\nInicio", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=0, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🧠\nRecuerdos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=1, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🖼️\nRecuerdos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=2, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="🔔\nAvisos", font=("Quicksand", 8), bg="white", fg="dim gray", bd=0, relief="flat").grid(row=0, column=3, sticky="nsew", pady=5)
        tk.Button(self.frame_navbar, text="👤\nPerfil", font=("Quicksand", 8, "bold"), bg="white", fg="MediumPurple3", bd=0, relief="flat").grid(row=0, column=4, sticky="nsew", pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiPerfilPaciente(root)
    root.mainloop()