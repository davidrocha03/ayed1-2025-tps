def baraja_espaniola():
    palos = ["Oro", "Copas", "Espada", "Bastos"]
    valores = [1,2,3,4,5,6,7,8,9,10,11,12]
    return [f"{valor} {palo}" for palo in palos for valor in valores]


print(baraja_espaniola())