import random as rn

def gen_fabricas() -> list[list[int]]:
    """
    Genera una matriz donde cada fila representa una fábrica y cada columna un día.
    
    Pre: —
    Post: Devuelve una matriz Nx7 (1 ≤ N ≤ 7) con valores aleatorios entre 0 y 150.
    """
    n = rn.randint(1, 7)
    return [[rn.randint(0, 150) for _ in range(7)] for _ in range(n)]


def cant_bicis_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Calcula cuántas bicicletas produjo cada fábrica en la semana.
    
    Pre: La matriz debe contener números enteros.
    Post: Devuelve una lista con la suma de cada fila de la matriz.
    """
    return [sum(fila) for fila in matriz]


def fab_mas_produjo(matriz: list[list[int]]) -> list[int]:
    """
    Determina la posición del valor más alto producido en la matriz.
    
    Pre: La matriz debe ser rectangular y no vacía.
    Post: Devuelve [fila, columna] donde se encuentra el número mayor.
    """
    dia = len(matriz)
    fabrica = len(matriz[0])
    mayor = matriz[0][0]
    fabrica_dia = [0, 0]

    for fila in range(dia):
        for col in range(fabrica):
            if matriz[fila][col] > mayor:
                mayor = matriz[fila][col]
                fabrica_dia = [fila, col]
    return fabrica_dia


def dia_mas_productivo(matriz: list[list[int]]) -> tuple[int, int]:
    """
    Calcula cuál día tuvo mayor producción total.
    
    Pre: La matriz debe tener 7 columnas (un valor por día).
    Post: Devuelve (día, total) donde día es un número de 1 a 7.
    """
    agrupado = zip(*matriz)
    suma = [sum(valor) for valor in agrupado]
    mayor = max(suma)
    indice = suma.index(mayor)
    return (indice + 1, mayor)


def menor_comprension(matriz: list[list[int]]) -> list[int]:
    """
    Calcula el mínimo producido por cada fábrica.
    
    Pre: La matriz debe contener números enteros.
    Post: Devuelve una lista con el mínimo de cada fila.
    """
    return [min(valor) for valor in matriz]

def main():
    matriz = gen_fabricas()
    print("Matriz generada:")
    for fila in matriz:
        print(fila)

    print("\nTotal por fábrica:")
    print(cant_bicis_por_fabrica(matriz))

    print("\nFábrica y día con mayor producción:")
    print(fab_mas_produjo(matriz))

    print("\nDía más productivo:")
    print(dia_mas_productivo(matriz))

    print("\nMenor producción por fábrica:")
    print(menor_comprension(matriz))


if __name__ == "__main__":
    main()
