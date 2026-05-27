import random

class User:
    def __init__(self, id_user, tipo, saldo):
        self.id = int(id_user)
        self.tipo = int(tipo)
        self.saldo = float(saldo)