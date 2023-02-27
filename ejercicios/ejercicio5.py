def bisiesto(anio):
    if anio % 4 ==0 and (anio % 100 !=0 or anio % 400 == 0):
        return True
    else:
        return False


print(bisiesto(2023))