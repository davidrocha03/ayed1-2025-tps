def des_clave(c: str) -> tuple[str, str]:
    """
    PRE: c es una cadena de texto no vacía.
    POST: devuelve una tupla con dos cadenas:
          - la primera formada por los caracteres ubicados en posiciones pares,
          - la segunda por los caracteres en posiciones impares,
          separados por espacios.
    """
    c1 = [num for ind, num in enumerate(c) if ind % 2 == 0]
    c2 = [num for ind, num in enumerate(c) if ind % 2 != 0]
    return (' '.join(c1), ' '.join(c2))


def main() -> None:
    """
    PRE: No recibe parámetros.
    POST: Solicita una clave al usuario (mínimo 4 caracteres) y,
          si es válida, muestra la tupla generada por des_clave().
          Finaliza cuando el usuario ingresa -1.
    """
    while True:
        clave = input("Ingrese una clave (min 8 caracteres, -1 para salir): ") 
        if not clave.strip():
            print("No se admiten espacios vacíos") 
        elif len(clave) < 4:
            print("Muy pocos caracteres. Vuelva a intentarlo")
        elif clave == "-1":
            break
        else:
            print(des_clave(clave))


if __name__ == "__main__":
    main()
