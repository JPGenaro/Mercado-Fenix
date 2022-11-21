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
prod_4 = Producto(
    "Aderesos",
    60
)
prod_5 = Producto(
    "Condimentos",
    85
)
prod_6 = Producto(
    "Fideos",
    40
)
prod_7 = Producto(
    "Chicles",
    5
)        
productos = [prod_1, prod_2, prod_3, prod_4, prod_5, prod_6, prod_7]