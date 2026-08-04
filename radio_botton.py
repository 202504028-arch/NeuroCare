import tkinter as tk

ventana = tk.Tk()

ventana.title("radio buttun")
ventana.geometry("600x500+200+50")

variable_de_control = tk.IntVar()

opcion1 = tk.Radiobutton(ventana, text="opcion 1", variable=variable_de_control, value=1)
opcion2 = tk.Radiobutton(ventana, text="opcion 2", variable=variable_de_control, value=2)
opcion1.pack()
opcion2.pack()



ventana.mainloop()