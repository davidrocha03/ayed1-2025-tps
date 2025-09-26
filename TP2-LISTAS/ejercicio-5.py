import random as rn
def es_ordenada(lista: list[int]) -> bool:
    """
    La funcion verifica si la lista esta o no ordenada
    
    Pre: El parametro debe ser una lista de enteros positivos
    Post: si la lista es ascendente retorna True sino False
    """
    return lista == sorted(lista)

lista = [rn.randint(1,3)for _ in range(3)]
print(lista)
resul = es_ordenada(lista)
print(resul) 