import random as rn
def eliminar_numeros(L1: list[int], L2: list[int]) -> None:
    """
    La funcion elimina los numeros que se encuentran en una segunda lista

    Pre: La lista L1 y L2 deben ser de números enteros
    Post: La funcion Imprime la Lista Original luego:
        - Lista de valores a eliminar
        - Lista con los valores no eliminados 
    """
    print(f"Lista Original: {L1}")
    for num in L2:
        while num in L1:
            L1.remove(num)
    print(f"Lista de valores a eliminar: {L2}")
    print(f"Lista con valores no eliminados: {L1}")

if __name__ == '__main__':
    lis1 = [rn.randint(1,15)for n in range(10)]
    lis2 = [rn.randint(1,15)for n in range(10)]
    eliminar_numeros(lis1, lis2)