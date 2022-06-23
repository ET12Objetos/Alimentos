from app.proteina import Proteina


class Carne(Proteina):
    def __init__(self, nombre):
        Proteina.__init__(self, nombre)
