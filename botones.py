from tkinter import Radiobutton, StringVar, Label, Button, Tk

"""
En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
"""
root = Tk()
root.title('Ejercicio 1')
root.geometry('200x200')

def limpiar():
    opciones.set(' ')

OPCIONES = [
    ('1', 'Opcion 1'),
    ('2', 'Opcion 2'),
    ('3', 'Opcion 3'),
    ('4', 'Opcion 4'),
    ('5', 'Opcion 5')
]

opciones = StringVar()
opciones.set(' ')

for id, opcion in OPCIONES:
    Radiobutton(root, text= opcion, variable= opciones, value= opcion).pack()

l = Label(root, textvariable= opciones)
l.pack()

btnclear = Button(root, text = 'Limpiar', command= limpiar)
btnclear.pack()

root.mainloop()
