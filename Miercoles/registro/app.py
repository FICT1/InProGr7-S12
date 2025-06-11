from modelos import clases as c
from dao import operaciones as o
from dao import persistencia as p

mi_archivo = p.PersistenciaDao([], "carrito.txt")
mi_archivo.abrir_archivo()

prod1 = c.Producto("Cafe", 100, 2)
prod2 = c.Producto("Helado", 55, 4)
prod3 = c.Producto("Gaseosa", 30, 5)

carrito = o.ProductoDao()
carrito.agregar(prod1)
carrito.agregar(prod2)
carrito.agregar(prod3)

# Usar otro nombre que no sea "p"
for producto in carrito.mostrar():
    print(producto)

buscar = "Cafe"
print(f"Dato a buscar: {buscar}")
datos = carrito.buscar_por_nombre(buscar)

if datos:
    for producto in datos:
        print(producto)
else:
    print("No se encontraron datos")

# Ya no sobreescribiste el módulo "p", así que esto funcionará
mi_archivo = p.PersistenciaDao(carrito.mostrar(), "carrito.txt")
mi_archivo.guardar_archivo()
