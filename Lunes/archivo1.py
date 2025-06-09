try:
    mi_archivo = open('C:\\Users\\isaqu\\Downloads\\Hola.txt', 'r')
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close()
except FileNotFoundError:
    print('El archivo no existe')

   