import random as rn
def normalizar(lista: list[int]) -> list[float]:
    """
    La funcion normaliza una lista de numeros

    Pre: El parámetro debe ser una lista de enteros
    Post: La función retorna una lista con los valores normalizados (decimales)
    """
    low = []
    for i in lista:
        down = i / 4
        low.append(round(down, 2)) 
    return low
    # Método con Listas por comprensión
    # return [i / 4 for i in lista]

if __name__ == '__main__':
    lista = [1,1,2]#[rn.randint(1,10) for i in range(10)]
    print(lista)
    fun = normalizar(lista)
    print(fun)
