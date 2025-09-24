import random as rn
def generar_lista_aleatoria(n: int) -> list[int]:
    """
    Genera una lista de N números aleatorios del 1 al 100.
    
    Pre: La cantidad debe se un numero entero positivo
    Post: Retorna una lista de enteros posotivos del y al 100
    """
    lista = [rn.randint(1, 100) for _ in range(n)]
    return lista
    
def tiene_repetidos(lista: list) -> bool:
    """
    Verifica si una lista contiene elementos repetidos.
    Pre: Recibe una lista. La función no debe modificar la lista original.
    Post: Retorna True si hay elementos repetidos, de lo contrario, False.
    """
    # Usando set, elimina los repetidos y luego comparo si la longitud es distinta a la original
    # Y si es distinta es porque hay repetidos

    #return len(lista) != len(set(lista)) 
    

    for i in lista:
        if lista.count(i) > 1:
            return True
    return False

def obtener_elementos_unicos(lista: list) -> list[int]:
    """
    Devuelve una nueva lista con los elementos únicos de la lista original.
    Pre: Recibe una lista.
    Post: Retorna una nueva lista con los elementos únicos, sin importar el orden.
    """

    # Solucion 1
    return list(set(lista))
    
    # Otra solucion
    # unicos = []
    # for i in lista:
    #     if i not in unicos:
    #         unicos.append(i)
    # return unicos

if __name__ == '__main__':
    print("-- RESULTADOS --")
    while True:
        cantidad = int(input("Ingresa la cantidad de numeros a generar: "))
        if cantidad < 5:
            print("Debe ser mayor o igual a 5")
        else:
            break
    print("Respuesta A")
    lista = generar_lista_aleatoria(cantidad)
    print(f"Lista: {lista}")
    print("-"*20)
    print("Respuesta B")
    duplicados = tiene_repetidos(lista)
    print(f"Tiene duplicados? {duplicados}")
    print("-"*20)
    print("Respuesta C")
    unicos = obtener_elementos_unicos(lista)
    print(f"Lista general {lista}")
    print(f"Lista con elementos unicos {unicos}")
    print("-"*20)


     
    