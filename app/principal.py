from alimento import Alimento


class Principal(Alimento):
    def __init__(self, nombre, precio):
        Alimento.__init__(self, nombre, precio)
