import random as rn

def es_par(num: int) -> bool:
    return num %2 == 0

def funcion_filter() -> list[int]:
    """
    La funcion crea una lista de pares mediante la funcion filter, lambda

    Pre: Se debe implementar la libreria random
    Post: Returna una lista con los numeros pares de otra lista
    """

    lista1 = [rn.randint(1,100) for _ in range(10)]
    print(lista1)

    # Sin uso de la funcion filter
    #return [ x for x in lista1 if x % 2 == 0]
    
    # Usando Lambda
    return list(filter(lambda x: x % 2 == 0, lista1))
    
    #Implementa con una funcion
    #return list(filter(es_par, lista1))

fun = funcion_filter()
print(fun)