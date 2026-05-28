"""
Programa principal para simular el acceso de usuarios a través de torniquetes en una estacion 
del tren ligero. Tambien define la logica para generar a los usuarios de manera aleatoria y
procesar su acceso utilizando hilos para simular la concurrencia en el sistema. 
Al final, se muestra un resumen de la jornada con el total de usuarios procesados, accesos concedidos y denegados
"""
#Importaciones de las clases y librerias necesarias para el programa
from User import User
from Torniquete import Torniquete
import random
import time
from concurrent.futures import ThreadPoolExecutor

def generar_usuarios(cantidad): #Genera una lista de usuarios con tipos y saldos aleatorios
    usuarios = []
    for i in range(cantidad):
        tipo = random.randint(0, 5)
        saldo = random.uniform(5, 40)
        usuarios.append(User(i, tipo, saldo))
    return usuarios


def procesar_usuario(torniquetes, indice_usuario, usuario): #Selecciona un torniquete basado en el indice del usuario y procesa su acceso
    torniquete = torniquetes[indice_usuario % len(torniquetes)]
    return torniquete.accion(usuario)


def main():
    cantidad_usuarios = 200
    cantidad_torniquetes = 4 #En general, es el numero de torniquetes que hay por estacion, pero se puede ajustar
    usuarios = generar_usuarios(cantidad_usuarios)
    torniquetes = [Torniquete(i + 1, time.time()) for i in range(cantidad_torniquetes)] #Crea los torniquetes con identificadores y hora de registro

    with ThreadPoolExecutor(max_workers=cantidad_torniquetes) as executor: #Utiliza un ThreadPoolExecutor para procesar a los usuarios de manera concurrente, asignando cada usuario a un torniquete basado en su indice
        futuros = [
            executor.submit(procesar_usuario, torniquetes, i, usuario)
            for i, usuario in enumerate(usuarios)
        ]
        #creamos contadores para los accesos concedidos y denegados
        accesos = 0
        rechazos = 0
        for futuro in futuros: 
            if futuro.result():
                accesos += 1
            else:
                rechazos += 1

    #Al finalizar el procesamiento de todos los usuarios, se muestra un resumen de la jornada
    print("\nResumen de jornada")
    print(f"Usuarios procesados: {cantidad_usuarios}")
    print(f"Accesos concedidos: {accesos}")
    print(f"Accesos denegados: {rechazos}")


if __name__ == "__main__": #Ejecuta la función principal para iniciar la simulación
    main()
