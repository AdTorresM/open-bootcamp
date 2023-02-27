from functools import reduce

def sumar_impares(numeros):
    nimpares = filter(lambda x: x % 2 != 0, numeros)
    return reduce(lambda x, y: x + y, nimpares)


#Pruebas

numeros = [1, 3, 4, 5, 6, 2, 3, 6, 3, 34, 2, 1, 0]

prueba = sumar_impares(numeros)

print(prueba)