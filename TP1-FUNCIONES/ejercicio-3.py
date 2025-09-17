
def control_gastos(viajes: int) -> float:
    """
        Esta funcion lleva un control de gastos en el rango de un mes
        dependiendo cuantos viajes hizo

        Pre: como parametros acepta valores enteros iguales o mayores a uno

        Post: Devuelve el total gastado en viajes en ese mes como valor flotante.

    """
    tarifa_maxima = 1.403

    if viajes >= 1 and viajes <= 20:
        return tarifa_maxima * viajes
    elif viajes >= 21 and viajes <= 30:
        return (tarifa_maxima * viajes) * 0.80 
    elif viajes >= 31 and viajes <= 40:
        return (tarifa_maxima * viajes) * 0.70
    elif viajes > 40:
        return (tarifa_maxima * viajes) * 0.60
    else:
        return None

while True:
    viajes = int(input("engrese cantidad de viajes ( 0 para salir ): ")) 
    if viajes >= 1:
        fun = control_gastos(viajes)
        print(f"Total gastado en el mes es: {fun:.2f}")
    elif viajes == 0:
        break
    else:
        print("ERROR. Numero negativo")