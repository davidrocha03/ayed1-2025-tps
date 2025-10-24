def cargar_matriz(n: int) -> list[list[int]]:
    """
    La funcion genera una matriz de N x N
    
    Pre: N debe ser un numero entero positivo
    Post: retorna una matriz con los valores que se ingresó
    """

    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            while True:
                try:
                    valor = int(input(f"Ingrese valor para la posicion ({i} : {j}): "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Solo se admiten numeros enteros.")
        matriz.append(fila)
    return matriz


def ordenar_filas(lista: list[list[int]]) -> list[list[int]]:
    """
    Ordena cada fila de la matriz en forma ascendente.

    Pre:
        - La matriz debe ser una lista de listas de números.
    Post:
        - Retorna una nueva matriz, con cada una de sus filas ordenada de forma ascendente.
    """
    return [sorted(lum) for lum in lista]

    # matriz = []
    # for fila in lista:
    #     matriz.append(sorted(fila))
    # return matriz

def intercambiar_filas(matriz: list[list[int]], n1: int, n2: int) -> list[list[int]]:
    """
    La funcion intercambia filas mediante las posiciones dadas
    Args:
        matriz (list[list[int]]): Debe estar previamente cargada con numeros enteros 
        n1 (int): Debe ser una posicion valida
        n2 (int): Debe ser una posicion valida

    Returns:
        list[list[int: retorna una matriz con las filas interncambiadas
    """

    matriz[n1], matriz[n2] = matriz[n2], matriz[n1] 
    return matriz

def intercambiar_columnas(matriz: list[list[int]], n1: int, n2: int) -> list[list[int]]:
    """
    La funcion intectambia columas
    
    Pre:
        La matriz debe estar cargada previamente
        n1 y n2: Deben ser una posicion valida
    Post:
        Retorna una matriz con las columnas intercambiadas
    """
    for i in range(len(matriz)):
        matriz[i][n1], matriz[i][n2] = matriz[i][n2], matriz[i][n1]
    return matriz

def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    La funcion Transpone una matriz NxN 

    Pre: La matriz debe estar cargada previamente 
    Post: Retorna una matriz Transpuesta
    """
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz


def calcular_promedio(matriz: list[list[int]], indice: int) -> int:
    """
    La funcion calcula el promedio de los valores de una columna determinada

    Pre:
        - La matriz debe estar cargada previamente
        - El indice debe ser valido (0 <= indice < cantidad de columnas)
    Post:
        - Retorna el promedio redondeado de los valores de la columna indicada
    """
    col = [fila[indice]for fila in matriz]
    if not matriz:
        return 0
    promedio = sum(col) / len(col)
    return round(promedio)  
    
    

def calcular_porcentaje(matriz: list[list[int]], indice: int) -> float:
    """
    La funcion calcula el porcentaje de elementos impares en una columna

    Pre:
        - La matriz debe estar cargada previamente
        - El indice debe ser valido (0 <= indice < cantidad de columnas)
    Post:
        - Retorna el porcentaje de valores impares respecto al total de la columna
    """
    col = [fila[indice]for fila in matriz]
    if not col:
        return 0.0
    imp = [x for x in col if x % 2 != 0]
    porcentaje = (len(imp) / len(col)) * 100
    return porcentaje


def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    """
    La funcion verifica si una matriz es simetrica respecto a su diagonal principal

    Pre:
        - La matriz debe ser cuadrada y estar cargada previamente
    Post:
        - Retorna True si la matriz es simetrica, False en caso contrario
    """  
    n = len(matriz)
    for i in range(n):
        for j in range(i + 1, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

# def es_simetrica_secundaria():
#     pass


# def es_palindromos_capicua():
#     pass
if __name__ == "__main__":
    while True:
        n = int(input("Ingresa N: "))
        if n <= 0:
            print("Debe ser positivo")
        else:
            b = cargar_matriz(n)
            print("--- MATRIZ GENERADA Y CARGADA ---")
            for i, fila in enumerate(b):
                print(f"Fila {i}: {fila}")
            print("--- MATRIZ ORDENADA DE FORMA ASCENDENTE ---")
            l = ordenar_filas(b)
            for p ,q in enumerate(l):
                print(f"Fila {p}: {q}")
        while True:
            n1 = int(input("Ingresa n1: "))
            if 0 <= n1 < len(b):
                break
            print("Indice no existente.")
        while True:
            n2 = int(input("Ingresa n2: "))
            if 0 <= n2 < len(b):
                break
            print("Indice no existente.")
        print("--- FILAS INTERCAMBIADAS ---")
        resul = intercambiar_filas(b, n1, n2)
        for i in resul:
            print(i)
        while True: 
            v1 = int(input("INgrese valor 1: "))
            if 0 <= v1 <len(b):
                break
            print("Indice no existente")
        while True: 
            v2 = int(input("INgrese valor 2: "))
            if 0 <= v2 < len(b):
                break
            print("Indice no existente")
        print("--- COLUMNAS INTERCAMBIADAS ---")
        col = intercambiar_columnas(b, v1, v2)
        for l in col:
            print(l)
        q = transponer_matriz(b)
        print("--- MATRIZ TRANSPUESTA ---")
        for fila in q:
            print(fila)
        while True:
            num = int(input("Ingrese indice de fila: "))
            if 0 <= num < len(b):
                break
            print("Indice no existente")
        print(f"El promedio es: {calcular_promedio(b,num)}")
        while True:
            cp = int(input("Ingrese indice de columna: "))
            if 0 <= cp < len(b):
                break
            print("Indice no existente")
        print(f"El porcentaje es: {calcular_porcentaje(b, cp)}")
        if es_simetrica_principal(b) == True:
            print("Es simetrica")
        print("No es simetrica")
