
from modelos import clases as c
from dao import operaciones as o

prod1= c.Producto("Cafe", 100, 2)
prod2 = c.Producto("Helado", 55, 4)
prod3= c.Producto("Gaseosa", 30, 5)

carrito = o.ProductoDao()
carrito.agregar(prod1)
carrito.agregar(prod2)
carrito.agregar(prod3)

for p in carrito.mostrar():
    print(p)

buscar = "Cafe"
datos = carrito.buscar_por_nombre(buscar)