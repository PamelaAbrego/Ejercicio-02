class Egresos:
    def __init__(self):
        self.egresosLista = []

    def registrarEgreso(self, id, monto):
        egreso = (id, monto)
        self.egresosLista.append(egreso)

    def mostrarEgresos(self):
        for egreso in self.egresosLista:
            print(f"Id: {egreso[0]}. Monto: {egreso[1]}")

    def obtenerEgresos(self):
        return self.egresosLista
