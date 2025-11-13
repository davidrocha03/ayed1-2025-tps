def des_clave(c: str) -> tuple[str, str]:
    c1 = [num for ind, num in enumerate(c) if ind %2 == 0]
    c2 = [num for ind, num in enumerate(c) if ind %2 != 0]
    return (' '.join(c1), ' '.join(c2))

def main():
    while True:
        clave = input("Ingrese una clave (min 8 caracteres, -1 para salir): ") 
        if not clave.strip():
            print("No se admiten espacios vacios") 
        elif len(clave) < 4:
            print("Muy pocos caracteres. Vuelva a intentarlo")
        elif clave == "-1":
            break
        else:
            print(des_clave(clave))

if __name__ == "__main__":
    main()