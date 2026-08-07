import tkinter as tk

ventana = tk.Tk()

ventana.title("ejemplo grid")
ventana.geometry("600x500+200+50")

label1 = tk.Label(ventana, text="label 1")
label1.place(x=50, y=50)

label2 = tk.Label(ventana, text="label 2")
label2.place(x=100, y=50)



ventana.mainloop()