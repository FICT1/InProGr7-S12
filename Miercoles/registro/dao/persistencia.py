class PersistenciaDao:
    def __init__(self, registros, ruta_archivo):
        self.registros = registros
        self.ruta_archivo = ruta_archivo

    def abrir_archivo(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                self.registros = eval(archivo.read())
        except FileNotFoundError:
            self.registros = []

    def guardar_archivo(self):
        with open (self.ruta_archivo, 'w') as archivo:
            archivo.write(str(self.registros))