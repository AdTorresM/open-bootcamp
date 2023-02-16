import time

factual = time.localtime()
hactual = factual.tm_hour
mactual = factual.tm_min


hsalida = 19
msalida = 0

if hactual >= hsalida:
    print('Es hora de ir a casa!')

else:
    mfaltantes = (hsalida - hactual) * 60 + (msalida - mactual)
    hfaltantes = mfaltantes // 60
    mfaltantes = mfaltantes % 60

    print('Faltan ', hfaltantes, ' horas y ', mfaltantes, ' minutos para salir' )