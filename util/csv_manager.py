import csv
from modelos.perfil_profesional import PerfilProfesionalTI


class CSVManager:
    """
    Gestiona la lectura y escritura de archivos CSV
    del sistema.
    """

    # ==========================================
    # Cargar perfiles profesionales
    # ==========================================

    @staticmethod
    def cargar_perfiles(ruta):

        perfiles = []

        try:
            with open(ruta, mode="r", encoding="utf-8") as archivo:

                lector = csv.DictReader(archivo)

                for fila in lector:

                    perfil = PerfilProfesionalTI(
                        fila["Rol"],
                        fila["Peso_Algoritmos"],
                        fila["Peso_Matematicas"],
                        fila["Peso_Diseno_Visual"],
                        fila["Peso_Comunicacion"],
                        fila["Peso_Infraestructura"],
                        fila["Demanda_Mercado"],
                        fila["Salario"]
                    )

                    perfiles.append(perfil)

        except FileNotFoundError:

            print("No se encontró el archivo de perfiles.")

        return perfiles


    # ==========================================
    # Guardar evaluación
    # ==========================================

    @staticmethod
    def guardar_evaluacion(
        ruta,
        codigo,
        carrera,
        rol_principal,
        rol_secundario,
        porcentaje,
        fecha
    ):

        datos = [
            codigo,
            carrera,
            rol_principal,
            rol_secundario,
            porcentaje,
            fecha
        ]


        with open(
            ruta,
            mode="a",
            newline="",
            encoding="utf-8"
        ) as archivo:

            escritor = csv.writer(archivo)

            escritor.writerow(datos)