import random as rn
import math


def cargar_numeros()->list:
    """
    La funcion una lista al azar de 4 digitos
    Pre: No precisa parametros, utiliza el modulo random para su funcionamiento
    Post: retorna la lista generada de numeros al azar de 4 digitos
    """
    cantidad = rn.randint(10,99)

    lista = [rn.randint(1000, 9999)for _ in range(cantidad)]
    return(lista) 


def calcular_producto(lista: list[int]) -> int:
    """
    La funcion calcula el producto de todos los elementos en una lista de números.

    Pre: La lista contiene solo números (enteros).
    Post: Retorna el producto de todos los elementos de la lista.
    """
    #return math.prod(lista) Halla el producto con la libreria math
    producto = 1

    for numero in lista:
        producto *= numero
    return producto

def eliminar_valor(lista: list[int], valor: int) -> list[int]:
    """
    Elimina todas las apariciones de un valor específico en la lista.

    Pre: La lista debe estar cargada y el valor debe ser un entero 
    Post: Retorna la lista de enteros, sin los numeros que se ingresó
    """
    while valor in lista:
        lista.remove(valor)
    return lista



def es_capicua(lista: list[int]) -> bool:
    """
    La funcion verifica si la lista es capicúa 

    Pre: Debe tener la lista cargada de numeros enteros,
    Post: Retorna True si es capucúa, caso contrario retorna False
    """
    return lista == lista[::-1]


if __name__ == '__main__':
    print("Funcion A")
    lista = cargar_numeros()
    print(lista)
    print("-"*20)
    print("Funcion B")
    total = calcular_producto(lista)
    print(total)
    print("-"*20)
    print("Funcion C")
    while True:
        valor = int(input("Ingrese valor numero a eliminar (-1 Para salir): "))
        resul = eliminar_valor(lista,valor)
        print(resul)
        if valor == -1:
            break
    print("-"*20)
    print("Funcion C")
    res = es_capicua(lista)
    print(lista)
    print(res)

    