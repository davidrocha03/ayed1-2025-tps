def devolver(frase: str, n: int) -> str:
    """
    Pre: n debe ser un entero positivo dentro del rango de la frase.
    Post: devuelve los últimos n caracteres usando slicing.
    """
    return frase[-n:]


def con_for(frase: str, n: int) -> str:
    """
    Pre: n debe ser un entero positivo dentro del rango de la frase.
    Post: devuelve los últimos n caracteres usando un ciclo for.
    """
    n_frase = ""
    for l in range(-1, -n-1, -1):
        n_frase += frase[l]
    return n_frase[::-1]


def main() -> None:
    """
    Pre: no recibe parámetros.
    Post: muestra el resultado de ambas funciones.
    """
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese cantidad de caracteres desde el final: "))
    print("Con slicing:", devolver(frase, n))
    print("Con for:", con_for(frase, n))


if __name__ == "__main__":
    main()
