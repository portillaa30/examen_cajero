saldototal=1000


def consultar_saldo():
    print("1.Consultar saldo")
    print("Su saldo actual es", saldototal)
    menu()
    return saldototal

def retirar():
    cantidad_retiro=int(input("Ingrese la cantidad a retirar"))
    retiro(cantidad_retiro)
    print("Su saldo restante es: ", retiro(cantidad_retiro))

def depositar():
    cantidad_deposito=int(input("Ingrese la cantidad a depositar:"))
    deposito(cantidad_deposito)
    print("Su saldo actual es de",deposito(cantidad_deposito))

def deposito(num):
    if num <= 0:
        print("Debe depositar una cantidad mayor a cero")
        print(menu())
    else:
        saldo_act=saldototal+num
    return saldo_act

def retiro(num):
    if num>saldototal:
        print("No se puede retirar mas dinero del disponible")
        menu()
    else:
        saldo_act_=saldototal-num
    return saldo_act_

def menu():
    print("""

MENU

1.CONSULTAR SALDO
2.DEPOSITAR DINERO
3.RETIRAR DINERO
0.SALIR

""")


def leer_opcion():
    opcion=int(input("Ingrese un numero: "))
    if opcion > 3 or opcion<0:
        print("Opcion invalida, ingrese otra")
        input("Presione enter para continuar")
        print(menu())
        opcion=int(input("Ingrese un numero: "))
    else:
        return int(opcion)




while True:
    menu()
    opcion=leer_opcion()
    match opcion:
        case 1:
            consultar_saldo()
        case 2:
            depositar()
        case 3:
            retirar()
        case 0:
            print("Gracias por usar el cajero")
            break

    break
