import tkinter as tk

ventana = tk.Tk()

ventana.title("radio buttun")
ventana.geometry("600x500+200+50")

variable_chek1 = tk.BooleanVar()

def habilitar_boton():
    if variable_chek1.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")
        
chek1 = tk.Checkbutton(ventana, text="habilitar botton", variable=variable_chek1, command=habilitar_boton)
boton = tk.Button(ventana, text="boton", state="disabled")


chek1.pack()
boton.pack()


ventana.mainloop()

#la diferencia es que se puede escoguer mas de una opcion e igual aplica el command