from tkinter import *

"""
En este segundo ejercicio, tendréis que crear una interfaz sencilla 
la cual debe de contener una lista de elementos seleccionables, 
también debe de tener un label con el texto que queráis.
"""

root = Tk()
root.title('Lista')
root.geometry('300x300')

l = Label(root, text = 'Menú desplegable')
l.pack()
lista = [
    'Elige un elemento',
    'Elemento 1',
    'Elemento 2',
    'Elemento 3',
    'Elemento 4',
    'Elemento 5'
]

elemento = StringVar()
elemento.set(lista[0])

contenedor = OptionMenu(root, elemento, *lista)
contenedor.pack()

opc = Label(root, textvariable= elemento)
opc.pack()


root.mainloop()
