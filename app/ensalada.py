from app.acompaniamiento import Acompaniamiento


class Ensalada(Acompaniamiento):
    def __init__(self, nombre):
        Acompaniamiento.__init__(self, nombre)
