import modulo_que_no_existe

""" 
Desarrollar una función para ingresar a través del teclado un número
natural. La función rechazará cualquier ingreso inválido de datos
utilizando excepciones y mostrará la razón exacta del error. Controlar
que se ingrese un número, que ese número sea entero y que sea mayor que 0.
Devolver el valor ingresado cuando éste sea correcto. Escribir también un
programa que permita probar el correcto funcionamiento de la misma"
"""

def ingresar_numero_natural():
    while True:
        try:
            numero = input("Ingrese un número natural: ")
            if not numero.isdigit():
                raise ValueError("El valor ingresado no es un número.")
            numero = int(numero)
            if numero <= 0:
                raise ValueError("El número debe ser mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}")

# Programa para probar la función
if __name__ == "__main__":
    numero = ingresar_numero_natural()
    print(f"El número ingresado es: {numero}")
    """
    Errores que pueden ser manejados con excepciones en Python:

    1. ValueError: Se lanza cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado.
    2. TypeError: Se lanza cuando una operación o función se aplica a un objeto de tipo inapropiado.
    3. IndexError: Se lanza cuando se intenta acceder a un índice que está fuera del rango de una secuencia.
    4. KeyError: Se lanza cuando se intenta acceder a una clave que no existe en un diccionario.
    5. AttributeError: Se lanza cuando se intenta acceder a un atributo que no existe en un objeto.
    6. ImportError: Se lanza cuando una declaración de importación no encuentra el módulo que se intenta importar.
    7. IOError: Se lanza cuando una operación de E/S falla, como cuando un archivo no se puede abrir.
    8. ZeroDivisionError: Se lanza cuando se intenta dividir un número por cero.
    9. FileNotFoundError: Se lanza cuando se intenta abrir un archivo que no existe.
    10. Exception: Clase base para todas las excepciones en Python. Puede ser utilizada para manejar cualquier excepción no específica.

    En el contexto del código proporcionado, se manejan los siguientes errores:
    - ValueError: Se utiliza para manejar entradas que no son números y números que no son mayores que 0.
    # Ejemplos de manejo de excepciones

    # Ejemplo de ValueError
    try:
        numero = int("abc")
    except ValueError as e:
        print(f"ValueError: {e}")

    # Ejemplo de TypeError
    try:
        resultado = "2" + 2
    except TypeError as e:
        print(f"TypeError: {e}")

    # Ejemplo de IndexError
    try:
        lista = [1, 2, 3]
        elemento = lista[5]
    except IndexError as e:
        print(f"IndexError: {e}")

    # Ejemplo de KeyError
    try:
        diccionario = {"clave": "valor"}
        valor = diccionario["otra_clave"]
    except KeyError as e:
        print(f"KeyError: {e}")

    # Ejemplo de AttributeError
    try:
        objeto = None
        objeto.metodo()
    except AttributeError as e:
        print(f"AttributeError: {e}")

    # Ejemplo de ImportError
    try:
    except ImportError as e:
        print(f"ImportError: {e}")

    # Ejemplo de IOError
    try:
        with open("archivo_que_no_existe.txt", "r") as archivo:
            contenido = archivo.read()
    except IOError as e:
        print(f"IOError: {e}")

    # Ejemplo de ZeroDivisionError
    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    # Ejemplo de FileNotFoundError
    try:
        with open("archivo_que_no_existe.txt", "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

    # Ejemplo de Exception
    try:
        raise Exception("Este es un error general.")
    except Exception as e:
        print(f"Exception: {e}")
"""