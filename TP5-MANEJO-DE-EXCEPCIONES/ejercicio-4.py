def interrupcion():
    i = 1
    while i <= 100000:
        try:
            print(i)
            i += 1
        except KeyboardInterrupt:
            confirmar = input("Desea continuar? (s/n): ")
            if confirmar.lower() == "s":
                print("continuando..")
            else:
                print("Detenido")
                break
            

def main():
    interrupcion()
if __name__ == "__main__":
    main()