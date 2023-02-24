paises = input("Ingresa una lista de paises (Separalos con una coma) ")

lpaises = paises.split(",")
repetidos = set()

for pais in lpaises:
    pais = pais.strip()
    if pais:
        repetidos.add(pais)
        

orden = sorted(repetidos)
paises_final = list(orden)

print(",".join(paises_final))