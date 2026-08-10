"""
=============================================================================
PROYECTO INTEGRADOR: NEUROCARE (Interfaz de Escritorio con CustomTkinter)
Desarrollado exclusivamente en Python con CustomTkinter
Configuración visual: Vista tipo laptop, tonos lila/lavender, completamente interactiva.
=============================================================================
"""

import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

# Configuración inicial del tema y apariencia de CustomTkinter
ctk.set_appearance_mode("light")  # Modo claro para mantener los tonos pasteles limpios
ctk.set_default_color_theme("blue")  # Tema base seguro de CustomTkinter

class NeuroCareApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NeuroCare | Más que una app, un acompañamiento")
        self.geometry("1200x700x+200+10")
        self.minsize(1000, 600)
        
        # Gama de colores personalizada
        self.bg_lavender = "#f9f6ff"
        self.primary_lila = "#8a63f2"
        self.dark_lila = "#4c1d95"
        self.card_bg = "#ffffff"
        
        self.configure(fg_color=self.bg_lavender)

        # Diccionario para almacenar las referencias de las secciones (para scroll automático)
        self.secciones_frames = {}

        # Construcción de la interfaz con ScrollableFrame
        self.crear_estructura_scroll()

    def crear_estructura_scroll(self):
        # Contenedor principal con scroll estilo página web
        self.scroll_container = ctk.CTkScrollableFrame(
            self, 
            fg_color=self.bg_lavender, 
            corner_radius=0
        )
        self.scroll_container.pack(fill="both", expand=True)

        # Construir cada sección dentro del contenedor
        self.construir_header()
        self.construir_seccion_hero()
        self.construir_seccion_nosotros()
        self.construir_seccion_estadisticas()
        self.construir_seccion_galeria()
        self.construir_seccion_equipo()
        self.construir_seccion_tabs()
        self.construir_footer_con_navegacion()

    def desplazar_a(self, seccion_nombre):
        """Función interactiva para deslizar la vista hacia la sección seleccionada"""
        if seccion_nombre in self.secciones_frames:
            widget = self.secciones_frames[seccion_nombre]
            try:
                y_pos = widget.winfo_y()
                self.scroll_container._parent_canvas.yview_moveto(y_pos / self.scroll_container.winfo_height())
            except Exception:
                pass

    def construir_header(self):
        """1. Header / Barra de Navegación superior"""
        header_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.card_bg, corner_radius=0, height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)

        try:
            logo_raw = Image.open("img/logoNC (1).png")
            ancho_orig, alto_orig = logo_raw.size
            nuevo_alto = 80
            nuevo_ancho = int((ancho_orig / alto_orig) * nuevo_alto)
            
            self.img_logo = ctk.CTkImage(light_image=logo_raw, dark_image=logo_raw, size=(nuevo_ancho, nuevo_alto))
            lbl_logo = ctk.CTkLabel(header_frame, text="", image=self.img_logo)
        except Exception:
            lbl_logo = ctk.CTkLabel(
                header_frame, text="[ LOGO NC ]", 
                font=ctk.CTkFont(family="Poppins", size=16, weight="bold"), 
                text_color=self.dark_lila
            )
            
        lbl_logo.pack(side="left", padx=40)

        # Menú de navegación interactivo
        nav_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        nav_frame.pack(side="right", padx=40)
        
        links = [
            ("Inicio", "inicio"),
            ("Nosotros", "nosotros"),
            ("Funciones", "funciones"),
            ("Equipo", "equipo"),
            ("Contacto", "contacto")
        ]
        
        for texto, target in links:
            btn_link = ctk.CTkButton(
                nav_frame, text=texto, 
                font=ctk.CTkFont(family="Poppins", size=13),
                fg_color="transparent", text_color="#555555",
                hover_color="#e2d9fc", width=80, height=35,
                command=lambda t=target: self.desplazar_a(t)
            )
            btn_link.pack(side="left", padx=5)

        # Botón de Acceder
        btn_acceder = ctk.CTkButton(
            header_frame, text="Acceder", 
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            fg_color=self.primary_lila, text_color="#ffffff",
            hover_color=self.dark_lila, width=100, height=36, corner_radius=6,
            command=self.abrir_app)
        btn_acceder.pack(side="right", padx=10)

    def construir_seccion_hero(self):
        """2. Sección Hero (Bienvenida principal)"""
        hero_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.bg_lavender, corner_radius=0, height=420)
        hero_frame.pack(fill="x", padx=60, pady=30)
        hero_frame.pack_propagate(False)
        self.secciones_frames["inicio"] = hero_frame

        texto_frame = ctk.CTkFrame(hero_frame, fg_color="transparent")
        texto_frame.pack(side="left", fill="both", expand=True)

        lbl_titulo = ctk.CTkLabel(
            texto_frame, text="Más que una app,\nun acompañamiento.", 
            font=ctk.CTkFont(family="Poppins", size=32, weight="bold"), 
            text_color=self.dark_lila, justify="left"
        )
        lbl_titulo.pack(anchor="w", pady=10)

        lbl_desc = ctk.CTkLabel(
            texto_frame, text="NeuroCare es una plataforma diseñada para apoyar a personas con Alzheimer,\nsus familiares y cuidadores mediante tecnología accesible,\nrecordatorios inteligentes y actividades para estimular la memoria.", 
            font=ctk.CTkFont(family="Poppins", size=14), 
            text_color="#555555", justify="left"
        )
        lbl_desc.pack(anchor="w", pady=10)

        # Botones interactivos en el Hero
        botones_hero = ctk.CTkFrame(texto_frame, fg_color="transparent")
        botones_hero.pack(anchor="w", pady=10)

        btn_conocer = ctk.CTkButton(
            botones_hero, text="Conocer más", 
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            fg_color="#e2d9fc", text_color=self.dark_lila,
            hover_color="#d7c1f9", height=40, corner_radius=6,
            command=lambda: self.desplazar_a("nosotros")
        )
        btn_conocer.pack(side="left", padx=(0, 10))

        btn_entrar = ctk.CTkButton(
            botones_hero, text="Entrar a la App", 
            font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
            fg_color=self.primary_lila, text_color="#ffffff",
            hover_color=self.dark_lila, height=40, corner_radius=6,
            command=self.abrir_app)
        
        btn_entrar.pack(side="left")

        # Carga de la imagen de la mascota
        imagen_mascota_frame = ctk.CTkFrame(hero_frame, fg_color="#e2d9fc", width=280, height=280, corner_radius=12)
        imagen_mascota_frame.pack(side="right", padx=20)
        imagen_mascota_frame.pack_propagate(False)
        
        try:
            mascota_raw = Image.open("NEUROCARE/funciones/recursos/mascota.png")
            ancho_orig, alto_orig = mascota_raw.size
            nuevo_alto = 240  
            nuevo_ancho = int((ancho_orig / alto_orig) * nuevo_alto)
            
            self.img_mascota = ctk.CTkImage(light_image=mascota_raw, dark_image=mascota_raw, size=(nuevo_ancho, nuevo_alto))
            lbl_img_mascota = ctk.CTkLabel(imagen_mascota_frame, text="", image=self.img_mascota)
        except Exception:
            lbl_img_mascota = ctk.CTkLabel(
                imagen_mascota_frame, text="[ IMAGEN DE MASCOTA ]", 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"), 
                text_color=self.dark_lila
            )
            
        lbl_img_mascota.place(relx=0.5, rely=0.5, anchor="center")

    def construir_seccion_nosotros(self):
        """3. Sección Sobre Nosotros (¿Qué es NeuroCare?)"""
        sobre_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.card_bg, corner_radius=12)
        sobre_frame.pack(fill="x", padx=60, pady=20, ipady=25)
        self.secciones_frames["nosotros"] = sobre_frame

        lbl_tit = ctk.CTkLabel(
            sobre_frame, text="¿Qué es NeuroCare?", 
            font=ctk.CTkFont(family="Poppins", size=24, weight="bold"), 
            text_color=self.dark_lila
        )
        lbl_tit.pack(pady=10)

        lbl_sub = ctk.CTkLabel(
            sobre_frame, text="NeuroCare es una plataforma desarrollada para apoyar a personas con Alzheimer y a sus familiares\nmediante herramientas que facilitan el cuidado diario, fortalecen la memoria y mejoran la calidad de vida.", 
            font=ctk.CTkFont(family="Poppins", size=13), 
            text_color="#555555"
        )
        lbl_sub.pack(pady=5)

        cards_frame = ctk.CTkFrame(sobre_frame, fg_color="transparent")
        cards_frame.pack(pady=20, fill="x", padx=20)

        beneficios = [
            ("Estimulación Cognitiva", "Ejercicios diseñados para mantener activa la memoria y concentración."),
            ("Recordatorios", "Medicamentos, citas y actividades importantes."),
            ("Familia conectada", "Los familiares pueden acompañar al paciente en todo momento."),
            ("Seguridad", "Información protegida y un entorno fácil de utilizar.")
        ]

        for titulo, desc in beneficios:
            card = ctk.CTkFrame(cards_frame, fg_color=self.bg_lavender, corner_radius=8)
            card.pack(side="left", expand=True, fill="both", padx=8, ipady=15)
            
            lbl_card_tit = ctk.CTkLabel(
                card, text=titulo, 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"), 
                text_color=self.dark_lila
            )
            lbl_card_tit.pack(anchor="w", padx=12, pady=5)
            
            lbl_card_txt = ctk.CTkLabel(
                card, text=desc, 
                font=ctk.CTkFont(family="Poppins", size=12), 
                text_color="#666666", justify="left", wraplength=180
            )
            lbl_card_txt.pack(anchor="w", padx=12, pady=5)

    def construir_seccion_estadisticas(self):
        """4. Sección Estadísticas"""
        stats_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.primary_lila, corner_radius=12)
        stats_frame.pack(fill="x", padx=60, pady=20, ipady=20)

        estadisticas_datos = [
            ("17.1 M", "Adultos mayores en México."),
            ("7.9%", "Presentan algún tipo de demencia."),
            ("60-70%", "De los casos corresponden a Alzheimer."),
            ("4800+", "Casos estimados en Acapulco.")
        ]

        for num, txt in estadisticas_datos:
            stat_box = ctk.CTkFrame(stats_frame, fg_color="transparent")
            stat_box.pack(side="left", expand=True, fill="both")
            
            lbl_num = ctk.CTkLabel(
                stat_box, text=num, 
                font=ctk.CTkFont(family="Poppins", size=26, weight="bold"), 
                text_color="#ffffff"
            )
            lbl_num.pack()
            
            lbl_txt = ctk.CTkLabel(
                stat_box, text=txt, 
                font=ctk.CTkFont(family="Poppins", size=13), 
                text_color="#e2d9fc"
            )
            lbl_txt.pack()

    def construir_seccion_galeria(self):
        """5. Sección Galería / Pantallas de la Interfaz"""
        galeria_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.card_bg, corner_radius=12)
        galeria_frame.pack(fill="x", padx=60, pady=20, ipady=25)

        lbl_gal_tit = ctk.CTkLabel(
            galeria_frame, text="Conoce NeuroCare", 
            font=ctk.CTkFont(family="Poppins", size=24, weight="bold"), 
            text_color=self.dark_lila
        )
        lbl_gal_tit.pack(pady=5)

        lbl_gal_sub = ctk.CTkLabel(
            galeria_frame, text="Estas son algunas de las pantallas diseñadas para brindar una experiencia sencilla, intuitiva y accesible.", 
            font=ctk.CTkFont(family="Poppins", size=13), 
            text_color="#666666"
        )
        lbl_gal_sub.pack(pady=5)

        mockups_frame = ctk.CTkFrame(galeria_frame, fg_color="transparent")
        mockups_frame.pack(pady=20, fill="x")

        pantallas = ["Bienvenida", "Pantalla Principal", "Funciones"]
        for pantalla in pantallas:
            celular_box = ctk.CTkFrame(mockups_frame, fg_color="transparent")
            celular_box.pack(side="left", expand=True, fill="both", padx=10)
            
            img_interfaz = ctk.CTkFrame(celular_box, fg_color="#d7c1f9", width=200, height=280, corner_radius=12)
            img_interfaz.pack(pady=5)
            img_interfaz.pack_propagate(False)
            
            lbl_img_txt = ctk.CTkLabel(
                img_interfaz, text=f"[ Imagen de Interfaz:\n{pantallas.index(pantalla)+1} ]", 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"), 
                text_color=self.dark_lila
            )
            lbl_img_txt.place(relx=0.5, rely=0.5, anchor="center")
            
            lbl_etiqueta = ctk.CTkLabel(
                celular_box, text=pantalla, 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"), 
                text_color=self.dark_lila
            )
            lbl_etiqueta.pack(pady=8)

    def construir_seccion_equipo(self):
        """6. Sección Nuestro Equipo"""
        equipo_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.bg_lavender, corner_radius=12)
        equipo_frame.pack(fill="x", padx=60, pady=20, ipady=25)
        self.secciones_frames["equipo"] = equipo_frame

        lbl_eq_tit = ctk.CTkLabel(
            equipo_frame, text="Nuestro Equipo", 
            font=ctk.CTkFont(family="Poppins", size=24, weight="bold"), 
            text_color=self.dark_lila
        )
        lbl_eq_tit.pack(pady=10)

        grid_equipo = ctk.CTkFrame(equipo_frame, fg_color="transparent")
        grid_equipo.pack(fill="x", padx=20)

        miembros = [
            ("Jovali Benítez", "Scrum Master"),
            ("Abril Díaz", "Analista"),
            ("María Guadalupe", "Diseñadora UX/UI"),
            ("Yalitzi Estefania", "Administradora de Base de Datos"),
            ("Andry David", "Back"),
            ("Juan Carlos", "Front-End")
        ]

        for i, (nombre, rol) in enumerate(miembros):
            fila = i // 3
            col = i % 3
            
            persona_card = ctk.CTkFrame(grid_equipo, fg_color=self.card_bg, corner_radius=8)
            persona_card.grid(row=fila, column=col, padx=12, pady=12, sticky="nsew")
            
            lbl_nombre = ctk.CTkLabel(
                persona_card, text=nombre, 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"), 
                text_color=self.dark_lila
            )
            lbl_nombre.pack(anchor="w", padx=15, pady=(15, 3))
            
            lbl_rol = ctk.CTkLabel(
                persona_card, text=rol, 
                font=ctk.CTkFont(family="Poppins", size=12), 
                text_color="#666666"
            )
            lbl_rol.pack(anchor="w", padx=15, pady=(0, 15))

        for c in range(3):
            grid_equipo.columnconfigure(c, weight=1)

    def construir_seccion_tabs(self):
        """7. Sección de Pestañas (Tabs) Funcionales"""
        tabs_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.card_bg, corner_radius=12)
        tabs_frame.pack(fill="x", padx=60, pady=20, ipady=25)
        self.secciones_frames["funciones"] = tabs_frame

        lbl_tit = ctk.CTkLabel(
            tabs_frame, text="Explora las Funciones", 
            font=ctk.CTkFont(family="Poppins", size=24, weight="bold"), 
            text_color=self.dark_lila
        )
        lbl_tit.pack(pady=5)

        lbl_sub = ctk.CTkLabel(
            tabs_frame, text="Conoce los apartados principales diseñados para brindar una mejor experiencia y control diario.", 
            font=ctk.CTkFont(family="Poppins", size=13), 
            text_color="#666666"
        )
        lbl_sub.pack(pady=5)

        botones_tabs = ctk.CTkFrame(tabs_frame, fg_color="transparent")
        botones_tabs.pack(pady=15)

        self.contenido_tab_label = ctk.CTkLabel(
            tabs_frame, 
            text="Módulos enfocados en mantener el registro estructurado de las actividades del paciente, asegurando atención puntual y estimulación cognitiva.", 
            font=ctk.CTkFont(family="Poppins", size=13), 
            text_color="#555555", fg_color=self.bg_lavender, corner_radius=8,
            wraplength=750, justify="left", padx=25, pady=25
        )
        self.contenido_tab_label.pack(pady=10, fill="x", padx=40)

        def cambiar_tab(opcion):
            textos = {
                "Pacientes": "Módulos de gestión y registro de perfiles de pacientes con seguimiento clínico personalizado.",
                "Recordatorios": "Sistema de alertas visuales automatizadas para medicamentos, citas y actividades importantes.",
                "Juegos": "Minijuegos cognitivos interactivos (Memorama y Secuencia de Colores) con historial de puntajes."
            }
            self.contenido_tab_label.configure(text=textos.get(opcion, ""))
            for btn, nombre in botones_info:
                if nombre == opcion:
                    btn.configure(fg_color=self.primary_lila, text_color="#ffffff")
                else:
                    btn.configure(fg_color="#e2d9fc", text_color=self.dark_lila)

        botones_info = []
        for opt in ["Pacientes", "Recordatorios", "Juegos"]:
            b = ctk.CTkButton(
                botones_tabs, text=opt, 
                font=ctk.CTkFont(family="Poppins", size=13, weight="bold"),
                fg_color=self.primary_lila if opt == "Pacientes" else "#e2d9fc",
                text_color="#ffffff" if opt == "Pacientes" else self.dark_lila,
                hover_color=self.dark_lila, width=140, height=40, corner_radius=6,
                command=lambda o=opt: cambiar_tab(o)
            )
            b.pack(side="left", padx=10)
            botones_info.append((b, opt))

    def construir_footer_con_navegacion(self):
        """8. Botón inferior de adorno y Footer / Pie de página"""
        footer_action_frame = ctk.CTkFrame(self.scroll_container, fg_color=self.card_bg, corner_radius=12)
        footer_action_frame.pack(fill="x", padx=60, pady=20, ipady=25)
        self.secciones_frames["contacto"] = footer_action_frame

        btn_abrir_app = ctk.CTkButton(
            footer_action_frame, 
            text="Abrir Aplicación NeuroCare", 
            font=ctk.CTkFont(family="Poppins", size=14, weight="bold"), 
            fg_color=self.primary_lila, text_color="#ffffff",
            hover_color=self.dark_lila, width=280, height=45, corner_radius=8,
            command=self.abrir_app)
        
        btn_abrir_app.pack(pady=5)

        lbl_aviso_btn = ctk.CTkLabel(
            footer_action_frame, 
            text="* Botón estático en fase de integración por el equipo de desarrollo.", 
            font=ctk.CTkFont(family="Poppins", size=12, slant="italic"), 
            text_color="#777777"
        )
        lbl_aviso_btn.pack(pady=2)

        # Footer de cierre
        footer_info = ctk.CTkFrame(self.scroll_container, fg_color=self.dark_lila, corner_radius=0)
        footer_info.pack(fill="x", padx=0, pady=(25, 0), ipady=25)
        
        lbl_footer_logo = ctk.CTkLabel(
            footer_info, text="NeuroCare", 
            font=ctk.CTkFont(family="Poppins", size=16, weight="bold"), 
            text_color="#ffffff"
        )
        lbl_footer_logo.pack()

        lbl_footer_info = ctk.CTkLabel(
            footer_info, text="Proyecto Integrador\nUniversidad Tecnológica de Acapulco\n© 2026 Equipo NeuroNova", 
            font=ctk.CTkFont(family="Poppins", size=13), 
            text_color="#e2d9fc", justify="center"
        )
        lbl_footer_info.pack(pady=8)


    def abrir_app(self):
        from Bienvenida import bienvenida

        self.withdraw()
        bienvenida(self)
    
if __name__ == "__main__":
    app = NeuroCareApp()
    app.mainloop()