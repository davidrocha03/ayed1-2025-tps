def sub_cadena(frase: str, n: int, c: int) -> list[str]:
    del frase[n:n+c]


print(sub_cadena("El numero de telefono es 4356-7890", 25, 3))