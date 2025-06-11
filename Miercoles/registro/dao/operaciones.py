import modelos.clases as c

class ProductoDao:
    def __init__(self):
        self.registros = []

    def agregar (self, producto):
        self.registros.append(producto)

    def mostrar (self):
        return self.registros
    
    def buscar_por_nombre(self, nombre):
        nombre = nombre.lower()
        return [
           producto for producto in self.registros
           if nombre in producto.nombre.lower() 

           ]
    