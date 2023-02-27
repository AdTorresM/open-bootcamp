import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    time.sleep(tiempo_de_espera)
    print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

_thread.start_new_thread(horaActual, ("thread_uno", 1))
_thread.start_new_thread(horaActual, ("threat_dos", 2))

while True:
    pass