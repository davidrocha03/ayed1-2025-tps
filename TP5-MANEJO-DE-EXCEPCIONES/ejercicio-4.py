def interrupcion() -> None:
    """
    Pre: no recibe parametros
    Post: Imprime los números del 1 al 100000.
          Si el usuario presiona Ctrl-C, solicita confirmación para continuar o detener.
    """
    i = 1
    while i <= 100000:
        try:
            print(i)
            i += 1
        except KeyboardInterrupt:
            confirmar = input("Desea continuar? (s/n): ")
            if confirmar.lower() == "s":
                print("Continuando...")
            else:
                print("Detenido por el usuario")
                break


def main() -> None:
    interrupcion()


if __name__ == "__main__":
    main()
