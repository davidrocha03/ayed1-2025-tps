def dia_siguiente(dia: int, mes: int, anio: int) -> int:
    """
    la funcion calculara y devolvera la fecha del dia siguiente que se ingreso

    Pre: los valores ingresados deben ser valores numeros positivos validos

    Post: la funcion devolvera una tupla de enteros que representa la fecha del dia siguiente
    """ 
    dia_en_mes = dia_del_mes(mes, anio)
    if dia < dia_en_mes:
        dia += 1
    else:
        dia = 1
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
    return dia, mes, anio
def dias_entre_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    Esta funcion calculara los dias que hay entre las fechas ingresadas

    Pre: Ambas fechas ingresadas deben ser validas para hacer el calculo

    Post: La funcion devolvera la cantidad de dis que hay entre esas dos fechas
    
    """

    contador = 0
    inicio = (dia1, mes1, anio1)
    fin = (dia2, mes2, anio2)
    if inicio > fin:
        inicio, fin = fin, inicio

    while inicio != fin:
        dia1, mes1, anio1 = dia_siguiente(inicio[0], inicio[1], inicio[2])
        inicio = (dia1, mes1, anio1)
        contador += 1
    return contador


def suman_n_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """
    La funcion calculara la fecha que resulta de sumar n dias a una fecha inicial siempre y cuando estas sean validas
    
    Pre: las fechas ingresadas deber ser validad y n debe ser un numero entero

    Post: La funcion devolvera una fecha que es la suma de n dias a la fecha inicial
    
    """
    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio

def dia_del_mes(mes: int, anio: int) -> int:
    """
    La funcion informara la cantidad de dias que tiene un mes especifico 
    teniendo en cuenta los años bisiestos para realizar un buen calculo
    
    Pre: El mes ingresado debe estas en el range de 1 a 12 y el año debe ser un numero entero positivo valido

    Post: La funcion devuelve el total de dias que contiene el mes del año ingresado
    
    """
    dias30 = [4,6,9,11]

    if mes in dias30:
        return 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28
        
    else: 
        return 31
    
while True:
    print("MENU DE OPCIONES")
    print("1. Sumar N dias a una fecha")
    print("2. Calcular la cantidad de días existentes entre dos fechas cualquiera")
    print("3. Para salir")
    op = input("Ingrese la opcion deseada: ")
    if op == "1":
        try:
            dia = int(input("Ingresa fecha inicial: "))
            mes = int(input("Ingresa mes inicial: "))
            anio = int(input("Ingresa año inicial: "))
            n = int(input("Ingresa cantiadad de dias a sumar: "))
            f_final = suman_n_dias(dia, mes, anio, n)
            print(f"Luego de {n} dais la fecha es: {f_final[0]}/{f_final[1]}{f_final[2]}")
        except ValueError:
            print("Debe ingresar numeros enteros")
    elif op == "2":
        try:
            dia1 = int(input("Ingresa dia de primera fecha: "))
            mes1 = int(input("Ingresa mes de primera fecha: "))
            anio1 = int(input("Ingresa año de primera fecha: "))
            dia2 = int(input("Ingresa dia de segunda fecha: ")) 
            mes2 = int(input("Ingresa mes de segunda fecha: ")) 
            anio2 = int(input("Ingresa año de segunda fecha: ")) 
            total = dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
            print(f"En total ahy {total} dias entre las dos fechas")
        except ValueError:
            print("Deben ser numeros enteros")
    elif op == "3":
        print("Saliendo..")
        break
    else:
        print("Opcion no disponible")
