class PerfilProfesionalTI:
    """
    Representa un perfil profesional del área de Tecnología.
    Cada perfil posee un conjunto de pesos para evaluar la afinidad
    de un estudiante.
    """

    def __init__(
        self,
        nombre,
        peso_algoritmos,
        peso_matematicas,
        peso_diseno_visual,
        peso_comunicacion,
        peso_infraestructura,
        demanda_mercado,
        salario
    ):
        self.nombre = nombre
        self.peso_algoritmos = int(peso_algoritmos)
        self.peso_matematicas = int(peso_matematicas)
        self.peso_diseno_visual = int(peso_diseno_visual)
        self.peso_comunicacion = int(peso_comunicacion)
        self.peso_infraestructura = int(peso_infraestructura)
        self.demanda_mercado = int(demanda_mercado)
        self.salario = float(salario)

    def mostrar_perfil(self):
        print("\n==============================")
        print("PERFIL PROFESIONAL")
        print("==============================")
        print(f"Rol: {self.nombre}")
        print(f"Algoritmos: {self.peso_algoritmos}")
        print(f"Matemáticas: {self.peso_matematicas}")
        print(f"Diseño Visual: {self.peso_diseno_visual}")
        print(f"Comunicación: {self.peso_comunicacion}")
        print(f"Infraestructura: {self.peso_infraestructura}")
        print(f"Demanda: {self.demanda_mercado}%")
        print(f"Salario: S/. {self.salario:.2f}")