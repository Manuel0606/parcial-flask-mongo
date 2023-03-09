class Registro:

    def __init__(self, nombre, altura):
        self.nombre = nombre
        self.altura = altura
    
    def formato_doc(self):
        return {
            'nombre': self.nombre,
            'altura': self.altura
        }