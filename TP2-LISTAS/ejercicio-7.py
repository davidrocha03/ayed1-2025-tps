import random as rn
from itertools import zip_longest
def intercalar(lista1: list[int], lista2: list[int]) -> list[int]:
    """
      La función intercala elementos de una lista

    Pre: La Lista 1 y 2 deben contener numeros enteros positivos
    Post: Retorna la Lista 1 con los elementos concatenados e intercalados
    """
    print(lista1)
    print(lista2)
    lista1[:] = [ x for elemento in zip(lista1, lista2) for x in elemento ]
    return f"Lista Concatenara e intercalada: {lista1}"
    # Para casos de que las longistudes son distintas se usa herramienta de zip que es #zip_longest
    # lista1[:] = [x for elemento in zip_longest(lista1, lista2, fillvalue= None) for x in elemento if x is not None]
    # zip_longest con fillvalue en un decir "Fuerza a entrar" los elementos sobrantes de la lista larga

lista1 = [rn.randint(1,10) for _ in range(3)]
lista2 = [rn.randint(1,10) for _ in range(4)]
fun = intercalar(lista1, lista2)
print(fun)

