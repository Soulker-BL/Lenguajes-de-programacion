from modelos.perfil_profesional import PerfilProfesionalTI


class PerfilHibrido(PerfilProfesionalTI):
    """
    Representa un perfil profesional híbrido que combina
    dos especialidades tecnológicas.
    """

    def __init__(
        self,
        nombre,
        especialidad1,
        especialidad2,
        peso_algoritmos,
        peso_matematicas,
        peso_diseno_visual,
        peso_comunicacion,
        peso_infraestructura,
        demanda_mercado,
        salario
    ):

        super().__init__(
            nombre,
            peso_algoritmos,
            peso_matematicas,
            peso_diseno_visual,
            peso_comunicacion,
            peso_infraestructura,
            demanda_mercado,
            salario
        )

        self.especialidad1 = especialidad1
        self.especialidad2 = especialidad2

    def mostrar_perfil(self):
        print("\n==============================")
        print("PERFIL HÍBRIDO")
        print("==============================")

        print(f"Rol: {self.nombre}")
        print(f"Especialidad 1: {self.especialidad1}")
        print(f"Especialidad 2: {self.especialidad2}")

        print(f"Algoritmos: {self.peso_algoritmos}")
        print(f"Matemáticas: {self.peso_matematicas}")
        print(f"Diseño Visual: {self.peso_diseno_visual}")
        print(f"Comunicación: {self.peso_comunicacion}")
        print(f"Infraestructura: {self.peso_infraestructura}")

        print(f"Demanda: {self.demanda_mercado}%")
        print(f"Salario estimado: S/. {self.salario:.2f}")