from tkinter import messagebox
from conexion import conectarBd
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk


class editar_perfil:
        def __init__(self,root, idPaciente):
            self.root = root
            self.idPaciente = idPaciente
            self.ventana = tk.Toplevel(root)

            self.ventana.title("NEUROCARE -- EDITAR PERFIL")
            self.ventana.geometry("600x650+300+60")
            self.ventana.config(bg="lavender")
        
            self.crear_interfaz()


        def crear_interfaz(self):
                ##
                conexion = conectarBd()
                cursor = conexion.cursor()
                cursor.execute("SELECT alergias, enfermedadCronica FROM caracteristicaspaciente WHERE idPaciente = %s", (self.idPaciente,))
                resultado = cursor.fetchone()

                etiqueta_alergias = tk.Label(self.ventana, text="Alergias:")
                etiqueta_alergias.pack()

                self.campo_alergias = tk.Entry(self.ventana)
                self.campo_alergias.pack()
                self.campo_alergias.insert(0, resultado[0] if resultado else "no disponible")

                
                #ENFERMEDAD CRONICA#
                etiqueta_enfermedad = tk.Label(self.ventana, text="Enfermedad crónica:")
                etiqueta_enfermedad.pack()

                self.campo_enfermedad = tk.Entry(self.ventana)
                self.campo_enfermedad.pack()
                self.campo_enfermedad.insert(0, resultado[1] if resultado else "no disponible")

                        #NUMERO DEE EMERGENCIA#
                cursor.execute("SELECT numeroEmergencia FROM paciente WHERE idPaciente = %s", (self.idPaciente,))
                resultado_emergencia = cursor.fetchone()

                etiqueta_contacto = tk.Label(self.ventana, text="Contacto de emergencia:")
                etiqueta_contacto.pack()

                self.campo_contacto = tk.Entry(self.ventana)
                self.campo_contacto.pack()
                self.campo_contacto.insert(0, resultado_emergencia[0] if resultado_emergencia else "")\

                #tipo de sangre#
                cursor.execute("SELECT tipoSangre FROM caracteristicaspaciente WHERE idPaciente = %s", (self.idPaciente,))
                resultado_sangre = cursor.fetchone()
                opciones_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

                self.campo_sangre = ttk.Combobox(self.ventana, values=opciones_sangre)
                self.campo_sangre.pack()
                self.campo_sangre.set(resultado_sangre[0] if resultado_sangre else "")

                cursor.close()
                conexion.close()


                marco_botones = tk.Frame(self.ventana)
                marco_botones.pack(pady=20)

                boton_cancelar = tk.Button(marco_botones, text="Cancelar", command=self.cancelar)
                boton_cancelar.pack(side="left", padx=10)

                boton_confirmar = tk.Button(marco_botones, text="Confirmar", command=self.guardar_cambios)
                boton_confirmar.pack(side="left", padx=10)

        def cancelar(self):
                self.ventana.destroy()
                from perfil import usuario_perfil
                usuario_perfil(self.root, self.idPaciente)

        def guardar_cambios(self):
                conexion = conectarBd()
                cursor = conexion.cursor()

                sql = """
                UPDATE caracteristicaspaciente
                SET tipoSangre = %s, alergias = %s, enfermedadCronica = %s
                WHERE idPaciente = %s
                """
                valores = (self.campo_sangre.get(), self.campo_alergias.get(), self.campo_enfermedad.get(), self.idPaciente)
                cursor.execute(sql, valores)
                conexion.commit()

                sql = """
                UPDATE paciente
                SET numeroEmergencia = %s
                WHERE idPaciente = %s
                """
                valores = (self.campo_contacto.get(), self.idPaciente)
                cursor.execute(sql, valores)
                conexion.commit()

                cursor.close()
                conexion.close()

                self.ventana.destroy()
                from perfil import usuario_perfil
                usuario_perfil(self.root, self.idPaciente)


if __name__ == "__main__":

    ventana = tk.Tk()
    ventana.withdraw()

    idPaciente = 1

    app = editar_perfil(
        ventana,
        idPaciente
    )

    ventana.mainloop()