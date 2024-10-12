from tkinter import *

opciones=["Opción 1","Opción 2","Opción 3", "Opción 4"]

window = Tk()

elemento = StringVar(value=opciones)
lista = Listbox(window, listvariable=elemento)
lista.pack()
label = Label(text="Opciones")
label.pack()
window.mainloop()