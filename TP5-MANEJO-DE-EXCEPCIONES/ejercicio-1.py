class CeroMayorError(Exception):
    """Excepción para números menores que 0."""
    pass

def datos_invalidos() -> int:
    """
    Pre: Ninguna
    Post: Devuelve un número entero mayor o igual a 0 ingresado por el usuario.
          Muestra mensajes claros si el dato ingresado es inválido.
    """
    while True:
        try: 
            num = int(input("Ingrese un número: "))
            if num < 0:
                raise CeroMayorError("El número debe ser mayor o igual a cero")
            return num
        except CeroMayorError as e:
           print(e) 
        except ValueError:
            print("Error: Debe ingresar un número entero")
        except Exception as e:
            print(f"Error desconocido: {e}")

def main():
    numero = datos_invalidos()
    print(f"Número ingresado correctamente: {numero}")

if __name__ == "__main__":
    main()
