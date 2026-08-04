import tkinter as tk

ventana = tk.Tk()

ventana.title("ejemplo grid")
ventana.geometry("600x500+200+50")

entero = tk.IntVar(value=50)

print(entero.get())

opcion1 = tk.Radiobutton(ventana, text="opcion 1", variable=entero, value=1)
opcion1.pack()
opcion2 = tk.Radiobutton(ventana, text="opcion 2", variable=entero, value=2)
opcion2.pack()


ventana.mainloop()