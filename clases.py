class Usuario:
    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra
        self.dinero = 0

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

#Productos
prod_1 = Producto(
    "Galletas",
    20
)
prod_2 = Producto(
    "Jugos",
    30
)
prod_3 = Producto(
    "Gaseosas",
    50
)
productos = [prod_1, prod_2, prod_3]