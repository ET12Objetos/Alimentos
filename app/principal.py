from app.alimento import Alimento


class Principal(Alimento):
    def __init__(self, nombre, precio, proteina, acompaniamiento):
        Alimento.__init__(self, nombre, precio)
        self.proteina = proteina
        self.acompaniamiento = acompaniamiento
        if proteina.nombre == "Pollo" and acompaniamiento.nombre == "Ensalada":
            raise ValueError("El pollo no puede servirse con la ensalada")
