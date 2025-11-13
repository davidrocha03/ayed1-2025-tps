def suma_cadenas(c1: str, c2: str) -> float:
    """
    Pre: c1 y c2 son cadenas de caracteres que deberían representar números reales.
    Post: Devuelve la suma como número real. 
          Devuelve -1 si alguna cadena no es un número válido, mostrando un mensaje específico.
    """
    try:
        n1 = float(c1)
    except ValueError:
        print("la primera cadena no es un número válido")
        return -1.0
    try:
        n2 = float(c2)
    except ValueError:
        print("la segunda cadena no es un número válido")
        return -1.0
    return n1 + n2


def main():
    c1 = input("Ingrese primer número como cadena: ")
    c2 = input("Ingrese segundo número como cadena: ")
    resultado = suma_cadenas(c1, c2)
    if resultado != -1:
        print(f"La suma es: {resultado}")


if __name__ == "__main__":
    main()
