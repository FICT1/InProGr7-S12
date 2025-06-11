class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


    def __str__(self):
        return f"Producto: {self.nombre}, \nPrecio: {self.precio}, \nExistencia: {self.cantidad}"