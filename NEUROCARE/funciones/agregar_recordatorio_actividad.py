import tkinter as tk
import customtkinter as ctk
from conexion import conectarBd
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

# python NEUROCARE/funciones/agregar_recordatorio_actividad.py

class agregar_recordatorio_actividad:

    def __init__(self, root, idPaciente, callback_actualizar=None):
        self.root = root
        self.idPaciente = idPaciente
        self.callback_actualizar = callback_actualizar

        self.ventana = tk.Toplevel(root)
        self.ventana.title("NEUROCARE -- NUEVO RECORDATORIO")
        self.ventana.geometry("500x560+550+80")
        self.ventana.config(bg="lavender")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")

        self.crear_interfaz()

    def crear_interfaz(self):

        # ── TITULO ──────────────────────────────────────────────
        marco_titulo = tk.Frame(self.ventana, bg="lavender")
        marco_titulo.pack(fill="x", padx=25, pady=(20, 5))

        tk.Label(marco_titulo, text="Nuevo recordatorio",
                 bg="lavender", fg="black",
                 font=("Quicksand", 20, "bold")).pack(anchor="w")

        tk.Label(marco_titulo, text="Ingresa los datos de la actividad",
                 bg="lavender", fg="dim gray",
                 font=("Quicksand", 12)).pack(anchor="w")

        ttk.Separator(self.ventana, orient="horizontal").pack(fill="x", padx=25, pady=(10, 5))

        # ── FORMULARIO ──────────────────────────────────────────
        marco_form = tk.Frame(self.ventana, bg="lavender")
        marco_form.pack(fill="x", padx=25, pady=5)

        def etiqueta(texto):
            tk.Label(marco_form, text=texto, bg="lavender", fg="#3B0764",
                     font=("Quicksand", 12, "bold")).pack(anchor="w", pady=(10, 2))

        def campo_entry(ancho=440):
            e = ctk.CTkEntry(marco_form, width=ancho, height=38,
                             corner_radius=10, fg_color="white",
                             border_color="#C4B5FD", border_width=2,
                             text_color="black",
                             font=("Quicksand", 13))
            e.pack(anchor="w")
            return e

        # Título
        etiqueta("Título *")
        self.campo_titulo = campo_entry()

        # Tipo de actividad
        etiqueta("Tipo de actividad *")
        self.var_tipo = tk.StringVar(value="Memorama")
        marco_tipo = tk.Frame(marco_form, bg="lavender")
        marco_tipo.pack(anchor="w")

        tipos = ["Memorama", "Rompecabezas", "Ejercicio físico"]
        for tipo in tipos:
            ctk.CTkRadioButton(marco_tipo, text=tipo,
                               variable=self.var_tipo, value=tipo,
                               fg_color="#7C3AED", hover_color="#6D28D9",
                               text_color="black",
                               font=("Quicksand", 13)).pack(anchor="w", pady=2)

        # Descripción (opcional)
        etiqueta("Descripción (opcional)")
        self.campo_descripcion = campo_entry()

        # Fecha y hora
        etiqueta("Fecha y hora *")
        marco_fecha_hora = tk.Frame(marco_form, bg="lavender")
        marco_fecha_hora.pack(anchor="w")

        self.campo_fecha = DateEntry(marco_fecha_hora, width=14,
                                     background="#7C3AED", foreground="white",
                                     borderwidth=2, date_pattern="yyyy-mm-dd",
                                     font=("Quicksand", 12))
        self.campo_fecha.pack(side="left", padx=(0, 10))

        tk.Label(marco_fecha_hora, text="Hora:", bg="lavender",
                 fg="#3B0764", font=("Quicksand", 12, "bold")).pack(side="left", padx=(0, 5))

        self.hora_hh = tk.Spinbox(marco_fecha_hora, from_=1, to=12,
                                   width=3, format="%02.0f",
                                   font=("Quicksand", 12), wrap=True)
        self.hora_hh.pack(side="left")

        tk.Label(marco_fecha_hora, text=":", bg="lavender",
                 font=("Quicksand", 14, "bold")).pack(side="left")

        self.hora_mm = tk.Spinbox(marco_fecha_hora, from_=0, to=59,
                                   width=3, format="%02.0f",
                                   font=("Quicksand", 12), wrap=True)
        self.hora_mm.pack(side="left")

        self.ampm = tk.StringVar(value="AM")
        ctk.CTkSegmentedButton(marco_fecha_hora,
                               values=["AM", "PM"],
                               variable=self.ampm,
                               width=90,
                               font=("Quicksand", 12, "bold"),
                               fg_color="#E9D5FF",
                               selected_color="#7C3AED",
                               selected_hover_color="#6D28D9",
                               unselected_color="#E9D5FF",
                               unselected_hover_color="#C4B5FD",
                               text_color="black").pack(side="left", padx=(8, 0))

        # ── BOTONES ─────────────────────────────────────────────
        marco_botones = tk.Frame(self.ventana, bg="lavender")
        marco_botones.pack(fill="x", padx=25, pady=25)

        ctk.CTkButton(marco_botones, text="Cancelar",
                      width=160, height=42, corner_radius=12,
                      fg_color="white", hover_color="#F3E8FF",
                      text_color="#7C3AED", border_width=2,
                      border_color="#C4B5FD",
                      font=("Quicksand", 14),
                      command=self.cancelar).pack(side="left", padx=(0, 15))

        ctk.CTkButton(marco_botones, text="Guardar",
                      width=240, height=42, corner_radius=12,
                      fg_color="#7C3AED", hover_color="#6D28D9",
                      font=("Quicksand", 14, "bold"),
                      command=self.guardar).pack(side="left")

    # ── GUARDAR ─────────────────────────────────────────────────
    def guardar(self):
        titulo      = self.campo_titulo.get().strip()
        tipo        = self.var_tipo.get()
        descripcion = self.campo_descripcion.get().strip()
        fecha       = self.campo_fecha.get_date()
        hh_12       = int(self.hora_hh.get())
        mm          = self.hora_mm.get().zfill(2)
        periodo     = self.ampm.get()

        # Convertir a 24h para MySQL
        if periodo == "AM":
            hh = 0 if hh_12 == 12 else hh_12
        else:
            hh = 12 if hh_12 == 12 else hh_12 + 12
        hh = str(hh).zfill(2)

        if not titulo:
            messagebox.showwarning("Campo vacío", "Escribe un título para el recordatorio.", parent=self.ventana)
            return

        fecha_hora_str = f"{fecha} {hh}:{mm}:00"

        try:
            conexion = conectarBd()
            cursor   = conexion.cursor()

            cursor.execute("""
                INSERT INTO recordatorio
                    (idPaciente, idMedicamento, titulo, tipoRecordatorio, descripcion, fechaHora, estado)
                VALUES (%s, NULL, %s, 'Actividad', %s, %s, 'Pendiente')
            """, (self.idPaciente, titulo,
                  descripcion if descripcion else tipo,
                  fecha_hora_str))

            conexion.commit()
            cursor.close()
            conexion.close()

            messagebox.showinfo("Guardado", f"Recordatorio '{titulo}' guardado correctamente.", parent=self.ventana)
            self.ventana.destroy()

            if self.callback_actualizar:
                self.callback_actualizar()

        except Exception as e:
            messagebox.showerror("Error al guardar", str(e), parent=self.ventana)

    def cancelar(self):
        self.ventana.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.withdraw()
    app = agregar_recordatorio_actividad(ventana, 1)
    ventana.mainloop()