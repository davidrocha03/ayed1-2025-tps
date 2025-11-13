import math 

def sqrt(n: float):
    try:
        return math.sqrt(n)
    except ValueError:
        print("No se puede sacar la de un numero negativo")
        return None

def main():
    try:
        while True:
            num = input("Ingrese numero (exit para salir): ")
            if num.lower() == "exit":
                break
            print(sqrt(int(num)))
    except ValueError:
        print("Tipo de dato no valido")

if __name__ == "__main__":
    main()