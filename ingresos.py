class Ingresos:
    def __init__(self):
        self.ingresosLista = []

    def registrarIngreso(self, id, monto):
        ingreso = (id, monto)
        self.ingresosLista.append(ingreso)

    def mostrarIngresos(self):
        for ingreso in self.ingresosLista:
            print(f"Id: {ingreso[0]}. Monto: {ingreso[1]}")

    def obtenerIngresos(self):
        return self.ingresosLista
