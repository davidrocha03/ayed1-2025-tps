def texto_centrado(p: str) -> str:
    """
    PRE: p es una cadena de texto válida.
    POST: devuelve la misma cadena centrada en un ancho de 80 caracteres.
    """
    return p.center(80)


def main() -> None:
    """
    PRE: No recibe parámetros.
    POST: Solicita palabras al usuario y muestra cada una centrada,
          hasta que se ingrese -1 para salir.
    """
    while True:
        letra = input("Ingrese una palabra (-1 para salir): ")
        if letra == "-1":
            break
        elif not letra.strip():
            print("No debe ser vacio")
        else:
            print(texto_centrado(letra))


if __name__ == "__main__":
    main()
