from finanzas import Finanzas

while True:
    print("Instrucciones:")
    print("0. Salir.")
    print("1. Iniciar cuenta a $0.00.")
    print("2. Registrar Ingreso o Egreso.")
    print("3. Registro de Ingresos.")
    print("4. Registro de Egresos.")
    print("5. Registro de transacciones.")
    print("6. Total en cuenta.")
    option = input("Ingrese una opción: ")

    if option == "0":
        break
    elif option == "1":
        id = input("Ingrese el Id de su cuenta: ")
        nombre = input("Ingrese su nombre: ")
        monto = 0.00
        finanza = Finanzas(id, nombre, monto)
        print("Se ha inicializado su cuenta a $0.00")
    elif option == "2":
        option1 = input(
            "1. Registrar Ingreso. 2. Registrar Egreso. Ingrese una opción: "
        )
        if option1 == "1":
            id = input("Ingrese el id del Ingreso: ")
            monto = float(input("Ingrese el monto del Ingreso: "))
            finanza.registrarIngreso(id, monto)
        elif option1 == "2":
            id = input("Ingrese el id del Egreso: ")
            monto = float(input("Ingrese el monto del Egreso: "))
            finanza.registrarEgreso(id, monto)
    elif option == "3":
        print("Registro de ingresos: ")
        finanza.registroIngresos()
    elif option == "4":
        print("Registro de Egresos: ")
        finanza.registroEgresos()
    elif option == "5":
        print("Registro de transacciones: ")
        print("Registro de ingresos: ")
        finanza.registroIngresos()
        print("Registro de Egresos: ")
        finanza.registroEgresos()
    elif option == "6":
        nombre = finanza.obtenerNombre()
        id = finanza.obtenerId()
        montoFinal = finanza.montoFinal()
        print(f"El monto actual de la cuenta con Id {id} de {nombre} es: ${montoFinal}")
