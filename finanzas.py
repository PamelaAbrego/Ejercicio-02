from ingresos import Ingresos
from egresos import Egresos

ingresos = Ingresos()
egresos = Egresos()


class Finanzas:
    def __init__(self, id, nombre, monto):
        self.id = id
        self.nombre = nombre
        self.monto = monto

    def montoFinal(self):
        ingresosLista = ingresos.obtenerIngresos()
        egresosLista = egresos.obtenerEgresos()
        totalIngresos = 0.00
        totalEgresos = 0.00

        for ingreso in ingresosLista:
            totalIngresos = totalIngresos + ingreso[1]

        for egreso in egresosLista:
            totalEgresos = totalEgresos + egreso[1]

        montoFinalCuenta = self.monto + totalIngresos - totalEgresos

        return montoFinalCuenta

    def registrarIngreso(self, id, monto):
        ingresos.registrarIngreso(id, monto)

    def registrarEgreso(self, id, monto):
        egresos.registrarEgreso(id, monto)

    def registroIngresos(self):
        ingresos.mostrarIngresos()

    def registroEgresos(self):
        egresos.mostrarEgresos()

    def registrosTransacciones(self):
        ingresos.mostrarIngresos()
        egresos.mostrarEgresos()

    def obtenerNombre(self):
        return self.nombre

    def obtenerId(self):
        return self.id
