def suma_cadenas(c1: str, c2: str) -> float:
    try:
        n1 = float(c1)
        n2 = float(c2)
        return n1 + n2
    except ValueError:
        return -1

def main():
    c1 = input("ingrese primer cadena: ")
    c2 = input("ingrese segunda cadena: ")
    print(suma_cadenas(c1, c2))

if __name__ == "__main__":
    main()