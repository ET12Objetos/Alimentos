from app.alimento import Alimento


class Bebida(Alimento):
    def __init__(self, nombre, precio):
        Alimento.__init__(self, nombre, precio)
