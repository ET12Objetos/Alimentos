from alimento import Alimento


class Postre(Alimento):
    def __init__(self, nombre, precio):
        Alimento.__init__(self, nombre, precio)
