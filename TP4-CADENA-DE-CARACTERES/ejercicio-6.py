def sub_cadena(frase: str, n: int, c:int) -> str:
    return frase[n:n+c]


def sin_rebanada(frase: str, n: int, c:int) -> str:
    resul = ""
    for i in range(n, n+c):
        resul += frase[i]
    return resul

print(sin_rebanada("El numero de telefono es 4356-7890", 25, 3))