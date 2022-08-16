dict_coin_country = {
    "argentinos": 134.53,
    "mexicanos": 19.83,
    "colombianos": 4161.67
}


def dap(val):  # multiplicar

    m = float(input("Escribe la cantidad a convertir: "))
    mult = m * val
    mult = round(mult, 2)
    conv = str(mult)
    print("Tu cantidad es de $" + conv)
    print("Gracias por usar el conversor de moneda")


def pad(val):  # dividir

    m = float(input("Escribe la cantidad a convertir: "))
    mult = m / val
    mult = round(mult, 2)
    conv = str(mult)
    print("Tu cantidad es de $" + conv)
    print("Gracias por usar el conversor de moneda")


def select_1():

    opc = """
    ===================================================

    Elegiste la opción 1.

    ¿A qué moneda quieres convertir el monto?
    
    1. Pesos argentinos.
    2. Pesos mexicanos.
    3. Pesos Colombianos.
    4. Volver al menú principal.
    
    Elige una opción: """

    to_conv = int(input(opc))

    try:
        if to_conv == 1:
            dap(float(dict_coin_country["argentinos"]))
        elif to_conv == 2:
            dap(float(dict_coin_country["mexicanos"]))
        elif to_conv == 3:
            dap(float(dict_coin_country["colombianos"]))
        elif to_conv == 4:
            main()
        elif to_conv > 4:
            print("La opción ingresada no es válida")
    except ValueError:
        print("coloca una opcion correcta")


def select_2():

    opc = """
    ===================================================

    Elegiste la opción 2.

    ¿Qué moneda quieres convertir el monto?
    
    1. Pesos argentinos.
    2. Pesos mexicanos.
    3. Pesos Colombianos.
    4. Volver al menú principal.
    
    Elige una opción: """

    to_conv = int(input(opc))

    try:
        if to_conv == 1:
            pad(float(dict_coin_country["argentinos"]))
        elif to_conv == 2:
            pad(float(dict_coin_country["mexicanos"]))
        elif to_conv == 3:
            pad(float(dict_coin_country["colombianos"]))
        elif to_conv == 4:
            main()
        elif to_conv > 4:
            print("La opción ingresada no es válida")
    except ValueError:
        print("coloca una opcion correcta")


def main():

    try:
        menu = """
        ===================================================

        Bienvenido al Conversor.

        1. Dolares a pesos.
        2. Pesos a dolares.

        Elige un numero: """

        inp = int(input(menu))

        if inp == 1:
            select_1()
        elif inp == 2:
            select_2()
        elif inp == 3 or inp > 3:
            print("Escribe una opcion valida")
            inp = int(input(menu))

    except ValueError:
        print("No es un número")


if __name__ == '__main__':
    main()
