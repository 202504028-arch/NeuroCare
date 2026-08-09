
import tkinter as tk
                                    #python NEUROCARE/zpruebas/config.py
class bienvenida:
    def __init__(self,root):
        self.ventana = root
        

        self.ventana.title(" NEUROCARE -- BIENVENIDA")
        self.ventana.geometry("1920x1080")
        self.ventana.config(bg="lavender")

        self.ventana.minsize(False,False)
        self.ventana.maxsize(False,False)
        self.ventana.iconbitmap("NEUROCARE/funciones/recursos/logotipo.ico")
        
if __name__ =="__main__":
    ventana = tk.Tk()
    app = bienvenida(ventana)
    ventana.mainloop()
    