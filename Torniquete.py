"""
La clase `Torniquete` representa un torniquete en una estación de tren. Cada torniquete 
tiene un identificador único y una hora de registro. Incluye métodos para calcular 
la tarifa que un usuario debe pagar para acceder a la estación dependiendo su tipo (los cuales representan
un tipo diferente de usuario), así como para procesar la acción de un usuario al intentar pasar por el torniquete.
"""

import time

class Torniquete:
    def __init__(self, id, hora=None):
        self.id = id
        self.hora = hora if hora is not None else time.time()

    def calcular_tarifa(self, usuario): #Calcula la tarifa que un usuario debe pagar para acceder a la estación dependiendo su tipo
        tarifa_base = 11
        if usuario.tipo == 0:
            return tarifa_base

        descuento_por_tipo = {
            1: 5.5,
            2: 6,
            3: 5.5,
            4: 5.5,
            5: 5.5,
        }
        descuento = descuento_por_tipo.get(usuario.tipo, 0)
        return tarifa_base - descuento

    def accion(self, usuario): #Procesa la acción de un usuario al intentar pasar por el torniquete

        time.sleep(0.75)  # Simula el tiempo que tarda el torniquete en procesar al usuario
        tarifa = self.calcular_tarifa(usuario) #Calcula la tarifa que el usuario debe pagar para acceder a la estación dependiendo su tipo
        tipo_usuario = f"{usuario.tipo} - {usuario.nombre_tipo}" #Obtiene el nombre del tipo de usuario para mostrarlo en los mensajes

        if usuario.saldo < tarifa: #Funcion que verifica el saldo del usuario y determina si se concede o deniega el acceso
            print(
                f"[Torniquete {self.id}] Usuario {usuario.id} ({tipo_usuario}): "
                f"saldo insuficiente para pagar {tarifa:.2f}"
            )
            return False

        usuario.saldo -= tarifa #Se resta la tarifa correspondiente al saldo del usuario y se imprime el menaje aprobatorio junto con el saldo restante

        print(
            f"[Torniquete {self.id}] Usuario {usuario.id} ({tipo_usuario}): "
            f"acceso concedido | tarifa {tarifa:.2f} | saldo restante {usuario.saldo:.2f}"
        )

        return True