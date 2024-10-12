import tkinter
from tkinter import Label, ttk

opciones=["Opción 1","Opción 2","Opción 3", "Opción 4"]

window=tkinter.Tk()

seleccion=tkinter.StringVar()

def seleccionar():
    print(seleccion.get())

def reiniciar():
    seleccion.set(None)

for opcion in opciones:
    ttk.Radiobutton(window, text=opcion, value=opcion, variable=seleccion, command=seleccionar).grid(column=0, row=(opciones.index(opcion)), pady=5, padx=5)

ttk.Button(window, text="Reiniciar", command=reiniciar).grid(column=1, row=len(opciones)+1, sticky=tkinter.E,pady=5, padx=5)

window.mainloop()