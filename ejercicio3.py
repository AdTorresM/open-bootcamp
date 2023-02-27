peso = float(input('Introduce tu peso en Kg: '))
alt = float(input('Introduce tu estatura en Metros: '))

imc = peso / (alt**2)
print('Tu indice de masa corporal es: ', imc)
