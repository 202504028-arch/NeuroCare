from tkinter import messagebox
from conexion import conectarBD
import tkinter as tk


class Registro:
    def __init__(self, root):

        self.ventana = tk.Toplevel(root)

        self.ventana.title("Registro de usuario")
        self.ventana.geometry("500x500+400+50")
        self.ventana.config(bg="lavender")

        self.crear_interfaz()

    def crear_interfaz(self):

        # Título
        etiqueta_titulo = tk.Label(
            self.ventana,
            text="REGISTRO DE USUARIO",
            font=("Arial", 20, "bold"),
            bg="lavender"
        )
        etiqueta_titulo.pack(pady=20)


        # Nombre
        etiqueta_nombre = tk.Label(
            self.ventana,
            text="Nombre:",
            font=("Arial", 12),
            bg="lavender"
        )
        etiqueta_nombre.pack()

        self.entrada_nombre = tk.Entry(
            self.ventana,
            font=("Arial", 14),
            width=30
        )
        self.entrada_nombre.pack(pady=5)


        # Teléfono
        etiqueta_telefono = tk.Label(
            self.ventana,
            text="Teléfono:",
            font=("Arial", 12),
            bg="lavender"
        )
        etiqueta_telefono.pack(pady=(15, 0))

        self.entrada_telefono = tk.Entry(
            self.ventana,
            font=("Arial", 14),
            width=30
        )
        self.entrada_telefono.pack(pady=5)


        # Contraseña
        etiqueta_contraseña = tk.Label(
            self.ventana,
            text="Contraseña:",
            font=("Arial", 12),
            bg="lavender"
        )
        etiqueta_contraseña.pack(pady=(15, 0))

        self.entrada_contraseña = tk.Entry(
            self.ventana,
            font=("Arial", 14),
            width=30,
            show="*"
        )
        self.entrada_contraseña.pack(pady=5)


        # Botón
        boton_registrar = tk.Button(
            self.ventana,
            text="REGISTRARSE",
            font=("Arial", 12, "bold"),
            command=self.registrar_usuario
        )
        boton_registrar.pack(pady=25)

    def registrar_usuario(self):
        nombre = self.entrada_nombre.get()
        telefono = self.entrada_telefono.get()
        contraseña = self.entrada_contraseña.get()
        
        if nombre == "" or telefono == "" or contraseña == "":
            messagebox.showwarning("campos incompletos",
                                   "debes de completar todos los campos")
            return
        
        conexion = conectarBD()
        cursor = conexion.cursor()
        
        sql = "SELECT * FROM usuarios WHERE telefono=%s"
        valores =(telefono,)
        cursor.execute(sql, valores)
        usuario = cursor.fetchone()
        
        if usuario:
            messagebox.showwarning(
                "telefono registrado",
                "este numero de telefono ya esta registrado"
            )
            cursor.close()
            conexion.close()
            return
        
        
        sql = """
        INSERT INTO usuarios (nombre,
        telefono, contraseña)
        VALUES (%s,%s,%s)
        """
        valores =(nombre,telefono,contraseña)
        cursor.execute(sql, valores)
        conexion.commit()
        
        print("usuario registrado correctamente")
        
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Registro(ventana)
    ventana.mainloop()