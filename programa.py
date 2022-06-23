from app import *

bebida = Bebida("Vino", 450)
proteina = Pollo("Carne")
acompaniamiento = Ensalada("Ensalada")
principal = Principal("Carne con ensalada", 2000, proteina, acompaniamiento)

menu1 = Menu(principal, bebida)

bebida = Bebida("Gaseosa", 450)
proteina = Pollo("Pollo")
acompaniamiento = Ensalada("Ensalada")
principal = Principal("Pollo con sopa", 500, proteina, acompaniamiento)
postre = Postre("Porcion de Torta", 300)

menu2 = Menu(principal, bebida, postre)
