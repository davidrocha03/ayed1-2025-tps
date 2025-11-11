import random as random

def gen_fabricas() -> list[list[int]]:

    n = rn.randint(1, 7)
    return [[rn.randint(0, 150) for _ in range(7)]for _ in range(n)]

def cant_bicis_por_fabrica(matriz: list[list[int]]) -> list[list[int]]:
    
    totales = [sum(fila) for fila in matriz]
    return totales


def fab_mas_produjo(matriz: list[list[int]]):
    dia = len(matriz) 
    fabrica = len(matriz[0])  

    mayor = matriz[0][0]
    fabrica_dia = [0,0]

    for fila in range(dia):
        for col in range(fabrica):
            if matriz[fila][col] >  mayor:
                mayor = matriz[fila][col]
                fabrica_dia = [fila, col]
    return fabrica_dia  



def dia_mas_productivo(matriz: list[list[int]]) -> tuple[int,int]:
    agrupado = zip(*matriz)
    suma = [sum(valor) for valor in agrupado]
    mayor = max(suma)
    indice = suma.index(mayor)
    dia = indice + 1
    return (dia, mayor)

def menor_comprension(matriz: list[list[int]]) -> list[int]:
    
    return [min(valor)for valor in matriz] 