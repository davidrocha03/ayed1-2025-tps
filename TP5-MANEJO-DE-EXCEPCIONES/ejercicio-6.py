def obtener_posicion(l: list, b: int):
     
    try: 
        return l.index(b)
    except ValueError:
        print(f"La posicion del numero {b} no existe")
        return None



def main():
    lista = []
    while True:
        try:
            num = int(input("Ingrese numeros a cargar (-1 para salir): "))
        except ValueError:
            print("Dato invalido, debe ser un numero")
            continue
        if num == -1:
            break
        lista.append(num)
    try:
        n2 = int(input("Ingrese numero a buscar: "))
    except ValueError:
        print("Tipo de dato no valido")
        return
    pos = obtener_posicion(lista,n2)
    if pos is not None:
        print(f"encontrado: {pos}")

if __name__ == "__main__":
    main()
