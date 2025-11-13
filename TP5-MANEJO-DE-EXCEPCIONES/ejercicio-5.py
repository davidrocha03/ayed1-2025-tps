import math

def sqrt(n: float) -> float | None:
    """
    Pre: n debe ser un número real.
    Post: Devuelve la raíz cuadrada de n si n >= 0; 
          de lo contrario imprime un mensaje y devuelve None.
    """
    try:
        return math.sqrt(n)
    except ValueError:
        print("No se puede calcular la raíz de un número negativo")
        return None

def main() -> None:
    """
    Pre: no recibe parametros
    Post: Permite al usuario ingresar números y calcula su raíz cuadrada.
          El bucle termina si el usuario escribe 'exit'.
    """
    while True:
        num = input("Ingrese numero (exit para salir): ")
        if num.lower() == "exit":
            break
        try:
            n = float(num)
            print(sqrt(n))
        except ValueError:
            print("Tipo de dato no válido")

if __name__ == "__main__":
    main()
