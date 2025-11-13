from tabulate import tabulate
import numpy as np

def cine(filas: int, butacas: int) -> list[list[int]]:
    """Crea una sala vacía con 0 = libre, 1 = ocupada"""
    sala = [[0 for _ in range(butacas)] for _ in range(filas)]
    return sala


def mostrar_butacas(matriz: list[list[int]]) -> list[list[int]]:
    """
    Muestra la matriz de butacas usando tabulate.
    Pre: matriz válida.
    Post: imprime la sala y devuelve la misma matriz.
    """
    print("\n--- ESTADO DE LA SALA ---")
    print(tabulate(matriz, tablefmt="grid"))
    return matriz


def reservar():
    pass

def cargar_sala():
    pass

def butacas_libres():
    pass

def butacs_contiguas():
    pass


s = cine(4, 4)
l = mostrar_butacas(s)
print(l)


