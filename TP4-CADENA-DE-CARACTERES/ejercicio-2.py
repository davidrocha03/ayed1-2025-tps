def texto_centrado(p: str):
    return p.center(80)


def main():
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