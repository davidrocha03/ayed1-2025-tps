import random as rn


def encuenta_numero():
    x = rn.randint(1,500)
    c = 0
    print("--ADIVINA EL NUMERO--")
    
    while True:
        try:
            n = int(input("Ingrese Num: "))
            c += 1 
            if n < x: 
                print(f"{n} es menor")
                c += 1
            elif n > x:
                print(f"{n} es mayor")
                c += 1
            else:
                print("Correcto")
                return c
                
        except ValueError:
            print("Ocurrio un error")
            c += 1


def main():
    i = encuenta_numero()
    print(f"En total se intentaron {i + 1} veces")    

if __name__ == "__main__":
    main()

