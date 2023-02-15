class Vehiculo:
        color = 'rojo'
        ruedas = 4
        puertas = 5

class Coche(Vehiculo):
        vehiculo = Vehiculo()
        velocidad = 180
        cilindrada = 6
        
coche = Coche()

print('La velocidad máxima del vehiculo es: ', coche.velocidad)
print('El vehiculo tiene: ',coche.cilindrada , 'cilindros.')
print('El vehiculo es de color: ', coche.vehiculo.color)
print('El automovil tiene: ', coche.vehiculo.ruedas, 'ruedas')
print('Tiene: ', coche.vehiculo.puertas, 'puertas')