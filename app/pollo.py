from app.proteina import Proteina


class Pollo(Proteina):
    def __init__(self, nombre):
        Proteina.__init__(self, nombre)
