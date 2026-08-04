import tkinter as tk

ventana = tk.Tk()

ventana.title("ejemplo grid")
ventana.geometry("600x500+200+50")

label1 = tk.Label(ventana, text="label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(ventana, text="label 2")
label2.grid(row=0, column=1)

label3 = tk.Label(ventana, text="label 3")
label3.grid(row=1, column=0)

label4 = tk.Label(ventana, text="label 4")
label4.grid(row=1, column=1)

label5 = tk.Label(ventana, text="label 5")
label5.grid(row=0, column=2)


label6 = tk.Label(ventana, text="label 6")
label6.grid(row=1, column=2)


label7 = tk.Label(ventana, text="label 7")
label7.grid(row=0, column=3)

label8 = tk.Label(ventana, text="label 8")
label8.grid(row=1, column=3)

marco = tk.Frame(ventana, bg="red")
marco.config(width=100,height=100)
marco.grid(row=10, column=10)

ventana.mainloop()

