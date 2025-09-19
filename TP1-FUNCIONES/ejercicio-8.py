def dia_del_mes(mes: int, anio: int) ->int:
    """
    La funcion informa la cantidad de dias del mes y tiene en cuenta el año bisiesto
    
    Pre: El mes que se ingresa debe encontrarse en el rango de 1 a 12 
    y el año debe ser positivo y valido

    Post: La funcion devolvera el total de dias que tiene el mes del año que ingreso
    
    """   
    dias30 = [4, 6, 9, 11]
    if mes in dias30:
        return 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28
    else:
        return 31

def dia_de_la_semana(dia: int, mes: int, anio: int) -> int:
    """
    La funcion calculara el dia de una fecha determinada y devuelve 0 para Domingo, 1 Lunes, 2 Martes, etc.

    Pre: La fecha que se ingresa debesr valida tanto (dia, mes, anio)

    Post: La funcion devolvera unnnumero entero 0 y 6 la cual representara el dia de la semana
    
    """

    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    anio_a = anio // 100
    anio_b = anio % 100
    dia_semana = (((26 * mes -2) // 10) + dia + anio_b + (anio_b // 4) + (anio_a // a) - (2 * anio_a)) % 7
    if dia_semana < 0:
        dia_semana += 7
    return dia_semana


def muestra_calendario(mes: int, anio: int) -> None:
    """
    La funcion mostrara el caliendario completo para el mes y año que se ingresaroon
    
    Pre: El mes y el año que se ingresa deben ser numero enteros validos 

    Post: La funcion mostrara el calendario

    """

    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    semana = ("DOM", "LUN", "MAR", "MIE", "JUE", "VIE", "SAB")

    print(f"\n---{meses[mes-1]} de {anio}}---")
    print(' '.join(semana))
    total = dia_del_mes(mes, anio)
    inicio = dia_de_la_semana(1, mes, anio)

    print('    ' * inicio, end='')

    for dia in range(1, total + 1):
        print(f'{dia:3}', end=" ")
        if (inicio + dia) % 7 == 0:
            print()
    print('\n')

try:
    mes = int(input("Ingresa el mes: "))
    anio = int(input("Ingresa el año: "))
    muestra_calendario(mes, anio)
except ValueError:
    print("Deben ser solo numeros")

