def devolver(frase: str, n: int) -> str:
    return frase[-n:]

def con_for(frase: str, n: int) -> str:
    n_frase = ""
    for l in range(-1, -n-1, -1):
        n_frase += frase[l]
    return n_frase[::-1]

print(con_for("El numero de telefono es 4356-7890", 3))
