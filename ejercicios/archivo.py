archivo = open("archivo.txt", "w")
archivo.write("Hola Python")
archivo.close()

archivo = open("archivo.txt", "r")
lectura = archivo.read()
print(lectura)

archivo.close()