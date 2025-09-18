def calcular_vuelto(costo_total: int, dinero_recibido: int) ->  dict:
    """
    El costo total y el dinero recibido  deben ser numeros positivos
    si el dinero recibido es menor al costo total no debe realiazar el cálculo
    y moestraran la cantidad de billetes con su denominacion correspondiente
    
    Pre: Ambos parametros deber ser numeros enteros positivos
    si lo recibido es menor a costo total no calcula nada

    Post: si lo recibido es mayor la funcion devuelve un diccionario
    con la cantidad de billetes y su denominacion correspondiente
    
    """

    billetes = (5000, 1000, 500, 200, 100, 50, 10, 5, 2, 1)
    cantidad_vuelto = {}
    vuelto = dinero_recibido - costo_total
    if vuelto < 0:
        return -1
    for i in billetes:
        cantidad = vuelto // i
        vuelto %= i
        if cantidad > 0:
            cantidad_vuelto[i] = cantidad
    return cantidad_vuelto

while True:
    try:
        total_a_pagar = int(input("Ingrese costro de la compra (0 para salir): "))
        if total_a_pagar == 0:
            print("Saliendo del programa...")
        elif total_a_pagar > 0:
            recibido = int(input("Ingrese el dinero recibido: "))
            resul = calcular_vuelto(total_a_pagar, recibido)
            if resul == -1:
                print("Dinero insuficiente")
            else:
                print(".--- EL VUELTO A ENTREGAR ES: ---. ")
                for billete, cantidad in resul.items():
                    if cantidad > 0:
                        print(f"{cantidad} billete de ${billete}")
        else:
            print("Valor fuera de rango")
    except ValueError:
        print("Entrada invalida. Ingrese numero enteros")
     

