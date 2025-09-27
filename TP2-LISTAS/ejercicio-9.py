def generar_A_B(a: int, b: int) -> list[int]:
    """
    La funcon genera numeros entre A y B

    Pre: Los parametros A y B deben ser numeros enteros positivos
    Post: Retorna una lista de enteros multiplos de 7 que no sean multiplos de 5
    """

    return [x for x in range(a, b) if x % 7 == 0 and  x % 5 != 0]

fun = generar_A_B(10,40)
print(fun)