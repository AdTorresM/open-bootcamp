class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar(self):
        print('Nombre del alumno: ', self.nombre)
        print('Nota: ', self.nota)

    def resultado(self):
        if self.nota>=6:
            print('El alumno ', self.nombre, ' aprobo la asignatura')
        else:
            print('El alumno ', self.nombre, ' NO aprobo la asignatura')


a1 = Alumno('Adrian', 5)
a1.mostrar()
a1.resultado()