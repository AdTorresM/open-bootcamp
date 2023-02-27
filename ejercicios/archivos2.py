import pickle

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

coche = Vehiculo("Mazda", "CX-3", "2020")


with open("coche.pickle", "wb") as archivo:
    pickle.dump(coche, archivo)

with open("coche.pickle", "rb") as archivo:
    cochec = pickle.load(archivo)


print(cochec.marca)
print(cochec.modelo)
print(cochec.anio)