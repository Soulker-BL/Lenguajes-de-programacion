def validar_texto(valor):
    """
    Verifica que un texto no esté vacío.
    """

    while valor.strip() == "":
        print("El campo no puede estar vacío.")
        valor = input("Ingrese nuevamente: ")

    return valor



def validar_respuesta(valor):
    """
    Valida respuestas del test Likert (1-5).
    """

    while True:

        try:

            numero = int(valor)

            if numero >= 1 and numero <= 5:
                return numero

            else:
                print("Ingrese un valor entre 1 y 5.")

        except ValueError:

            print("Debe ingresar un número.")

        valor = input("Respuesta nuevamente: ")



def validar_codigo(valor):
    """
    Valida el código del estudiante.
    """

    while not valor.isdigit():

        print("El código debe contener solamente números.")
        valor = input("Código nuevamente: ")

    return valor