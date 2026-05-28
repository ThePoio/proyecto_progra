"""
Clase para representar a los usuarios del sistema de transporte público junto a sus atributos y definicion del tipo de usuario
con el objetivo de facilitar la gestión y el procesamiento de las transacciones y descuentos.
"""

class User: 
    TIPOS_USUARIO = {
        0: "Mi tren, ¡Cuidalo!",
        1: "Niño",
        2: "Estudiante",
        3: "Persona con discapacidad",
        4: "Docente",
        5: "Persona de la tercera edad",
    }

    def __init__(self, id_user, tipo, saldo): 
        self.id = int(id_user)
        self.tipo = int(tipo)
        self.saldo = float(saldo)

    @property #Propiedad para obtener el nombre del tipo de usuario basado en su tipo
    def nombre_tipo(self):
        return self.TIPOS_USUARIO.get(self.tipo, "Desconocido")

    def __str__(self): #Metodo para representar al usuario como una cadena de texto, mostrando su id, tipo y saldo de manera legible
        return (
            f"User(id={self.id}, tipo={self.tipo} - {self.nombre_tipo}, "
            f"saldo={self.saldo:.2f})"
        )

