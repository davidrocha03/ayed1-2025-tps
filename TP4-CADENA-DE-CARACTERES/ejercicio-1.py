class SoloLetrasError(Exception):
    """Excepción personalizada para indicar que la entrada debe contener solo letras."""
    pass


def es_capicua(p: str) -> bool:
    """
    PRE: p es una cadena de texto válida.
    POST: devuelve True si la palabra es capicúa, False en caso contrario.
    """
    for l in range(0, len(p) // 2):
        if p[l] != p[len(p) - 1 - l]:
            return False
    return True


def programa() -> None:
    """
    PRE: No recibe parámetros.
    POST: Solicita palabras hasta ingresar una válida y muestra si es capicúa.
    """
    while True:
        try:
            palabra = input("Ingrese palabra: ")
            if not palabra.strip():
                print("No debe ser un espacio vacio")
            elif palabra.isdigit():
                raise SoloLetrasError("Debe ser una palabra")
            elif len(palabra) <= 2:
                print("La cantidad de caracteres debe ser al menos 3")
            else:
                l = es_capicua(palabra)
                print(l)
                break
        except SoloLetrasError as e:
            print(e)
        except TypeError:
            print("Debe ser una cadena de texto")
        except EOFError:
            print("No se recibio ninguna entrada")
        except KeyboardInterrupt:
            print("Entrada interrumpida por el usuario")
        except Exception:
            print("Ocurrio algun error")
        finally:
            print("Se finalizo el manejo de excepciones")


if __name__ == "__main__":
    programa()
