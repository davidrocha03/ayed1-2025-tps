def obtener_posicion(l: list[int], b: int) -> int | None:
    """
    Pre: 'l' debe ser una lista de enteros y 'b' un entero a buscar.
    Post: Devuelve la posición de 'b' en 'l' si existe, imprime mensaje sino devuelve None
    """
    try:
        return l.index(b)
    except ValueError:
        print(f"La posición del número {b} no existe")
        return None

def main() -> None:
    """
    Pre: Ninguna.
    Post: Permite al usuario cargar una lista de enteros y buscar un valor,
          mostrando su posición si existe. Maneja errores de entrada.
    """
    lista: list[int] = []
    while True:
        try:
            num = int(input("Ingrese números a cargar (-1 para salir): "))
        except ValueError:
            print("Dato inválido, debe ser un número")
            continue
        if num == -1:
            break
        lista.append(num)

    try:
        n2 = int(input("Ingrese número a buscar: "))
    except ValueError:
        print("Tipo de dato no válido")
        return

    pos = obtener_posicion(lista, n2)
    if pos is not None:
        print(f"Encontrado en la posición: {pos}")

if __name__ == "__main__":
    main()
