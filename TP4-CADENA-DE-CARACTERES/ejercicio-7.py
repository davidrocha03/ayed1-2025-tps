def sub_cadena(frase: str, n: int, c: int) -> str:
    """
    Pre: n y c deben ser enteros válidos dentro del rango de la frase.
    Post: devuelve la frase sin la subcadena desde n hasta n+c.
    """
    return frase[:n] + frase[n+c:]


def main() -> None:
    """
    Pre: no recibe parámetros.
    Post: ejecuta la función pidiendo los datos al usuario.
    """
    try:
        frase = input("Ingrese una frase: ")
        n = int(input("Posición inicial (n): "))
        c = int(input("Cantidad de caracteres (c): "))
        print(sub_cadena(frase, n, c))
    except ValueError:
        print("n y c deben ser números enteros.")
    except IndexError:
        print("Indice fuera de rango")

if __name__ == "__main__":
    main()
