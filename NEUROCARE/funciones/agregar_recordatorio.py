import tkinter as tk
import customtkinter as ctk
from conexion import conectarBd
from tkinter import messagebox
from tkcalendar import DateEntry

# python NEUROCARE/funciones/agregar_recordatorio.py

class agregar_recordatorio:

    def __init__(self, root, idPaciente, callback_actualizar=None):
        self.root = root
        self.idPaciente = idPaciente
        self.callback_actualizar = callback_actualizar  # Para refrescar la lista al guardar

        self.ventana = tk.Toplevel(root)
        self.ventana.title("NEUROCARE -- NUEVO RECORDATORIO")
        self.ventana.geometry("500x620+550+80")
        self.ventana.config(bg="lavender")
        self.ventana.resizable(False, False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")

        self.crear_interfaz()

    def crear_interfaz(self):

        from tkinter import ttk

        # ── TITULO ──────────────────────────────────────────────
        marco_titulo = tk.Frame(self.ventana, bg="lavender")
        marco_titulo.pack(fill="x", padx=25, pady=(20, 5))

        tk.Label(marco_titulo, text="Nuevo recordatorio",
                 bg="lavender", fg="black",
                 font=("Quicksand", 20, "bold")).pack(anchor="w")

        tk.Label(marco_titulo, text="Ingresa los datos del medicamento",
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

        # Nombre del medicamento
        etiqueta("Nombre del medicamento *")
        self.campo_nombre = campo_entry()

        # Número de piezas
        etiqueta("Número de piezas *")
        self.campo_piezas = campo_entry(ancho=200)

        # Dosis diaria
        etiqueta("Dosis diaria (ej: 1 pastilla cada 8 horas) *")
        self.campo_dosis = campo_entry()

        # Fecha y hora
        etiqueta("Fecha de toma *")

        marco_fecha_hora = tk.Frame(marco_form, bg="lavender")
        marco_fecha_hora.pack(anchor="w")

        self.campo_fecha = DateEntry(marco_fecha_hora, width=14,
                                     background="#7C3AED", foreground="white",
                                     borderwidth=2, date_pattern="yyyy-mm-dd",
                                     font=("Quicksand", 12))
        self.campo_fecha.pack(side="left", padx=(0, 10))

        # Hora (spinboxes de HH y MM)
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

        # Aviso de reabastecimiento
        etiqueta("Avisar cuando se acabe el medicamento")

        self.var_aviso = tk.BooleanVar(value=True)
        ctk.CTkCheckBox(marco_form,
                        text="Sí, quiero que me avisen cuando se termine",
                        variable=self.var_aviso,
                        fg_color="#7C3AED", hover_color="#6D28D9",
                        font=("Quicksand", 12)).pack(anchor="w", pady=(5, 0))

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

    # ── VALIDAR Y GUARDAR ────────────────────────────────────────
    def guardar(self):
        nombre = self.campo_nombre.get().strip()
        piezas = self.campo_piezas.get().strip()
        dosis  = self.campo_dosis.get().strip()
        fecha  = self.campo_fecha.get_date()
        hh_12  = int(self.hora_hh.get())
        mm     = self.hora_mm.get().zfill(2)
        periodo = self.ampm.get()
        aviso  = 1 if self.var_aviso.get() else 0

        # Convertir hora 12h a 24h para MySQL
        if periodo == "AM":
            hh = 0 if hh_12 == 12 else hh_12
        else:
            hh = 12 if hh_12 == 12 else hh_12 + 12
        hh = str(hh).zfill(2)

        # Validaciones básicas
        if not nombre:
            messagebox.showwarning("Campo vacío", "Escribe el nombre del medicamento.", parent=self.ventana)
            return
        if not piezas.isdigit() or int(piezas) <= 0:
            messagebox.showwarning("Valor inválido", "El número de piezas debe ser un número entero mayor a 0.", parent=self.ventana)
            return
        if not dosis:
            messagebox.showwarning("Campo vacío", "Escribe la dosis diaria.", parent=self.ventana)
            return

        fecha_hora_str = f"{fecha} {hh}:{mm}:00"

        try:
            conexion = conectarBd()
            cursor   = conexion.cursor()

            # 1) INSERT en medicamento
            cursor.execute("""
                INSERT INTO medicamento
                    (idPaciente, nombreMedicamento, numeroPiezas, dosisDiaria, fechaHoraToma, avisoReabastecer)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.idPaciente, nombre, int(piezas), dosis, fecha_hora_str, aviso))

            id_medicamento = cursor.lastrowid   # ID generado automáticamente

            # 2) INSERT en recordatorio enlazado al medicamento
            cursor.execute("""
                INSERT INTO recordatorio
                    (idPaciente, idMedicamento, titulo, tipoRecordatorio, descripcion, fechaHora, estado)
                VALUES (%s, %s, %s, 'Médico', %s, %s, 'Pendiente')
            """, (self.idPaciente, id_medicamento,
                  f"Tomar {nombre}",
                  f"Dosis: {dosis}",
                  fecha_hora_str))

            conexion.commit()
            cursor.close()
            conexion.close()

            messagebox.showinfo("Guardado", f"Recordatorio de '{nombre}' guardado correctamente.", parent=self.ventana)

            self.ventana.destroy()

            # Actualizar la lista de recordatorios si hay callback
            if self.callback_actualizar:
                self.callback_actualizar()

        except Exception as e:
            messagebox.showerror("Error al guardar", str(e), parent=self.ventana)

    def cancelar(self):
        self.ventana.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.withdraw()

    idPaciente = 1

    app = agregar_recordatorio(ventana, idPaciente)
    ventana.mainloop()