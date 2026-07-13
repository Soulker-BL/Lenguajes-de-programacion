from modelos.estudiante import EstudianteEvaluado
from util.validaciones import (
    validar_texto,
    validar_codigo,
    validar_respuesta
)


class AsesorVocacional:

    def __init__(self):

        self.preguntas = {
            1: "Me gusta resolver problemas mediante algoritmos.",
            2: "Disfruto trabajar con matemáticas.",
            3: "Me interesa diseñar interfaces visuales.",
            4: "Me comunico fácilmente con otras personas.",
            5: "Me gusta automatizar tareas.",
            6: "Tengo paciencia para encontrar errores.",
            7: "Me interesa la ciberseguridad.",
            8: "Prefiero trabajar de manera independiente.",
            9: "Trabajo bien bajo presión.",
            10: "Me interesa analizar datos.",
            11: "Disfruto investigar problemas difíciles.",
            12: "Me interesa liderar proyectos tecnológicos."
        }

    def realizar_test(self):

        print("=" * 50)
        print("        TEST DE ORIENTACIÓN VOCACIONAL")
        print("=" * 50)

        codigo = validar_codigo(
            input("Código del estudiante: ")
        )

        carrera = validar_texto(
            input("Carrera: ")
        )

        estudiante = EstudianteEvaluado(codigo, carrera)

        numero = 1

        while numero <= len(self.preguntas):

            print("\n-------------------------------------")
            print(f"Pregunta {numero} de {len(self.preguntas)}")
            print("-------------------------------------")

            print(self.preguntas[numero])

            print("""
1. Muy en desacuerdo
2. En desacuerdo
3. Neutral
4. De acuerdo
5. Muy de acuerdo

0. Regresar a la pregunta anterior
""")

            try:

                respuesta = validar_respuesta(
                        input("Respuesta: ")
                    )

                if respuesta == 0:

                    if numero > 1:
                        numero -= 1
                    else:
                        print("Ya estás en la primera pregunta.")

                    continue

                if respuesta < 1 or respuesta > 5:
                    print("Ingrese un valor entre 1 y 5.")
                    continue

                estudiante.agregar_respuesta(numero, respuesta)

                numero += 1

            except ValueError:

                print("Debe ingresar un número.")

        return estudiante