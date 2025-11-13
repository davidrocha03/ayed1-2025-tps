def baraja_espaniola() -> list[str]:
    """
    Pre: No recibe parámetros.
    Post: Devuelve una lista con todas las cartas de la baraja española,
          cada carta representada como "valor palo", con valores del 1 al 12
          y palos: Oro, Copas, Espada, Bastos.
    """
    palos = ["Oro", "Copas", "Espada", "Bastos"]
    valores = [1,2,3,4,5,6,7,8,9,10,11,12]
    return [f"{valor} {palo}" for palo in palos for valor in valores]


def main():
    cartas = baraja_espaniola()
    print(cartas)


if __name__ == "__main__":
    main()
