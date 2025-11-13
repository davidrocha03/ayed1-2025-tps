def fitrar_palabras(frase: str, n: int) -> list[str]:
    palabras = []
    for palabra in frase.split():
        if len(palabra) >= n:
            palabras.append(palabra)
    return palabras


def por_comprension(frase: str, n: int) -> list[str]:
    return [palabra for palabra in frase.split() if len(palabra) >= n]


def con_filter(frase: str, n: int) -> list[str]:
    return list(filter(lambda s: len(s) >= n, frase.split()))


def main():
    pass

l = con_filter("camion helado departamento hola", 4)
print(l)