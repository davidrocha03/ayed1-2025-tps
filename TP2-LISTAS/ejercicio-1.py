import random as rn


def cargar_numeros()->list:
    """
    Carga una lista al azar de 4 digitos
    Pre: Necesita el modulo random para su funcionamiento
    Post: retorna la lista generada de numeros al azar
    """
    cantidad = rn.randint(10, 99)
    lista = [rn.randint(1000, 9999) for _ in range(cantidad)]
    return lista

def calcular_producto(lista: list) ->int:
    """
    Calcula y devuelve el producto de todos los elemtenos de una lista
    Pre:La lista debe ser de numeros 
    Post:Retorna el producto de todos los elemtenosd e la lista o 1 si la lista esta vacia
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto 

def eliminar_valor(lista: list, a_eliminar: int) -> None:
    """
    La funcion elimina todas las apariciones de valor que se a ingresado

    Pre: La lista debe ser de numeros
    Post: La funcion debe modificar la lista original y eliminando las coincidencias
    """
    for i in range(len(lista)-1, -1, -1):
        if lista[i] == a_eliminar:
            lista.pop(i)

def es_capicua(lista: list) -> bool:
    """
    La funcnion determina si el contenido de una lista cualquiera es capicua

    Pre:La lista puede estar vacia o contener cualquier tipo de dato
    Post:La funcion retorna True si la lista es capicua y False si no lo es
    La lista original no es modificada
    """
    izquierda = 0
    derecha = len(lista) -1
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha += 1
    return True

if __name__ == "__main__":
    print("--- Carga de la lista de numeros aleatorios ---")
    lista = cargar_numeros()
    print(f"Lista: {len(lista)} Elementos: {lista}")

    lista.extend([3345, 9987, 1234])
    print(f"Lista con duplicados: {lista}")

    print("--- Calculo del produnto ---")
    producto = calcular_producto(lista)
    print(f"El producto de cada elemento es: {producto}")

    print("--- Valor eliminados ---")
    a_eliminar = 3478
    print(f"Se eliminan estas apariciones {a_eliminar}")
    eliminar_valor(lista, a_eliminar)
    print(f"Lista como resultado: {lista}")

    print("--- Verificacion si la lista es capicua ---")
    print(f"Lista actual es capicua? {lista}")
    prueba = [16, 90, 88, 88, 11]
    print(f"Esta lista {prueba} es capicua? {es_capicua(prueba)}")
    no_capicua = [5, 6, 7]
    print(f"Lista {no_capicua} es capicua? {es_capicua(no_capicua)}")