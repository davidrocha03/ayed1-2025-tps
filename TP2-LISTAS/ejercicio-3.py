def ultimos_diez(n: int) -> list[int]:
    """
    Crea una lista de numeros enteros positivos

    Pre: El parametro ingresado debe ser un entero positivo
    Post: Retorna una lista con los ultimos 10 valores elevados al cuadrado
    """

    #Solucion corta
    return [num ** 2 for num in range(1, n+1)][-10:]

    # y de esta manera trabajo sobre los ultimos 10 numeros de forma directa
    # return [num ** 2 for num in range(n - 9, n + 1)]
    
    # Solucion larga
    # cuadrados = [num ** 2 for num in range(1, n+1)]
    # print(f"Lista: {cuadrados}")
    # ult_diez = cuadrados[-10:]
    # return ult_diez


while True:
    num = int(input("Ingresa n: "))
    if num < 1:
        print("Debe ser positivo")
    else:
        break
resul = ultimos_diez(num)
print(resul)