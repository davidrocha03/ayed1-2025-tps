def sub_cadena(frase: str, n: int, c: int) -> str:
    """
    PRE: 'frase' debe ser una cadena, n y c deben ser enteros no negativos.
    POST: devuelve una subcadena de longitud c empezando desde la posición n.
    """
    return frase[n:n+c]


def sin_rebanada(frase: str, n: int, c: int) -> str:
    """
    PRE: 'frase' debe ser una cadena, n y c deben ser enteros válidos.
    POST: devuelve una subcadena de longitud c comenzando en n sin usar slicing.
    """
    resul = ""
    for i in range(n, n+c):
        resul += frase[i]
    return resul


def main() -> None:
    """
    PRE: No recibe parámetros.
    POST: Pide una frase y parámetros para extraer subcadenas, muestra ambos resultados.
    """
    frase = input("Ingrese una frase: ")
    n = int(input("Posición inicial: "))
    c = int(input("Cantidad de caracteres: "))

    print("Con slicing:", sub_cadena(frase, n, c))
    print("Sin slicing:", sin_rebanada(frase, n, c))


if __name__ == "__main__":
    main()

