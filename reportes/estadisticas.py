import pandas as pd


class EstadisticasVocacionales:
    """
    Genera análisis estadísticos utilizando Pandas
    sobre las evaluaciones realizadas.
    """


    def __init__(self, archivo_evaluaciones, archivo_perfiles):

        self.archivo_evaluaciones = archivo_evaluaciones
        self.archivo_perfiles = archivo_perfiles


        self.evaluaciones = None
        self.perfiles = None


    # ======================================
    # Cargar archivos CSV
    # ======================================

    def cargar_datos(self):

        self.evaluaciones = pd.read_csv(
            self.archivo_evaluaciones
        )


        self.perfiles = pd.read_csv(
            self.archivo_perfiles
        )


        # Limpieza básica

        self.evaluaciones.dropna(
            inplace=True
        )


    # ======================================
    # Distribución vocacional
    # ======================================

    def distribucion_roles(self):

        print("\n===== DISTRIBUCIÓN VOCACIONAL =====")


        resultado = (
            self.evaluaciones
            .groupby("Rol_Principal")
            .size()
            .sort_values(
                ascending=False
            )
        )


        print(resultado)



    # ======================================
    # Promedio de afinidad
    # ======================================

    def promedio_afinidad(self):

        print("\n===== PROMEDIO DE AFINIDAD =====")


        promedio = (
            self.evaluaciones["Porcentaje"]
            .mean()
        )


        print(
            f"Promedio general: {promedio:.2f}%"
        )



    # ======================================
    # Comparación demanda laboral
    # ======================================

    def demanda_vs_vocacion(self):

        print("\n===== DEMANDA VS VOCACIÓN =====")


        vocacion = (
            self.evaluaciones
            .groupby("Rol_Principal")
            .size()
            .reset_index(
                name="Cantidad_Estudiantes"
            )
        )


        comparacion = vocacion.merge(
            self.perfiles,
            left_on="Rol_Principal",
            right_on="Rol"
        )


        resultado = comparacion[
            [
                "Rol",
                "Cantidad_Estudiantes",
                "Demanda_Mercado"
            ]
        ]


        print(resultado)



    # ======================================
    # Salarios
    # ======================================

    def salarios_roles(self):

        print("\n===== SALARIOS PROMEDIO =====")


        tabla = self.perfiles[
            [
                "Rol",
                "Salario"
            ]
        ]


        print(tabla)