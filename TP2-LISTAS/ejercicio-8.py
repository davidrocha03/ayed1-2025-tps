def num_impares(r1: int, r2: int) -> list[int]:
    """
    La funcion genera una lista de numeros impares

    Pre: Los parametros deben ser numeros positivos
    Post: Retorna la lista generada de numeros enteros
    """

    return [x for x in range(r1, r2)if x % 2 == 1]

num = num_impares(100, 200 )
print(num)