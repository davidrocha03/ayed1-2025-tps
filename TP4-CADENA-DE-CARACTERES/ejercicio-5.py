def fitrar_palabras(frase: str, n: int) -> list[str]:
    """
    PRE: frase debe ser una cadena de texto y n un entero positivo.
    POST: devuelve una lista con las palabras de 'frase'
          cuya longitud es mayor o igual a n.
    """
    palabras = []
    for palabra in frase.split():
        if len(palabra) >= n:
            palabras.append(palabra)
    return palabras


def por_comprension(frase: str, n: int) -> list[str]:
    """
    PRE: frase debe ser una cadena y n un entero positivo.
    POST: devuelve una lista por comprensión con palabras
          cuya longitud es mayor o igual a n.
    """
    return [palabra for palabra in frase.split() if len(palabra) >= n]


def con_filter(frase: str, n: int) -> list[str]:
    """
    PRE: frase debe ser una cadena y n un entero positivo.
    POST: devuelve una lista con palabras filtradas mediante filter(),
          manteniendo solo las que tienen longitud >= n.
    """
    return list(filter(lambda s: len(s) >= n, frase.split()))


def main() -> None:
    """
    PRE: no recibe parámetros.
    POST: pide una frase y un número, y muestra el resultado
          usando las tres funciones.
    """
    frase = input("Ingrese una frase: ")
    n = int(input("Longitud mínima: "))

    print("Filtrar normal:", fitrar_palabras(frase, n))
    print("Por comprensión:", por_comprension(frase, n))
    print("Con filter:", con_filter(frase, n))


if __name__ == "__main__":
    main()
