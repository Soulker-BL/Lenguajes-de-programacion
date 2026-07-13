class EstudianteEvaluado:
    """
    Representa a un estudiante que realiza el test vocacional.
    Sus respuestas se almacenan de forma encapsulada.
    """

    def __init__(self, codigo: str, carrera: str):
        self.__codigo = codigo
        self.__carrera = carrera
        self.__respuestas = {}

    # ======================
    # Código
    # ======================

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    # ======================
    # Carrera
    # ======================

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, valor):
        self.__carrera = valor

    # ======================
    # Respuestas
    # ======================

    @property
    def respuestas(self):
        return self.__respuestas

    def agregar_respuesta(self, pregunta, respuesta):
        self.__respuestas[pregunta] = respuesta

    def obtener_respuesta(self, pregunta):
        return self.__respuestas.get(pregunta)

    def limpiar_respuestas(self):
        self.__respuestas.clear()

    # ======================
    # Mostrar información
    # ======================

    def mostrar_datos(self):
        print("\n===== DATOS DEL ESTUDIANTE =====")
        print(f"Código   : {self.codigo}")
        print(f"Carrera  : {self.carrera}")
        print("Respuestas:")
        for pregunta, respuesta in self.__respuestas.items():
            print(f"Pregunta {pregunta}: {respuesta}")