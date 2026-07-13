from logica.asesor_vocacional import AsesorVocacional
from logica.motor_reglas import MotorReglas
from logica.compatibilidad import calcular_afinidad

from util.csv_manager import CSVManager

from util.graficos_ascii import (
    mostrar_competencias,
    detectar_brechas
)

from reportes.estadisticas import EstadisticasVocacionales
from reportes.generador_reporte import GeneradorReporte

from datetime import datetime



class MenuPrincipal:


    def mostrar(self):

        while True:


            print("\n")
            print("=" * 55)
            print(" SISTEMA DE ORIENTACIÓN PROFESIONAL TI ")
            print("=" * 55)


            print("""
1. Realizar evaluación vocacional
2. Ver estadísticas generales
3. Ver perfiles profesionales
4. Salir
""")


            opcion = input(
                "Seleccione una opción: "
            )


            if opcion == "1":

                self.realizar_evaluacion()


            elif opcion == "2":

                self.mostrar_estadisticas()


            elif opcion == "3":

                self.mostrar_perfiles()


            elif opcion == "4":

                print(
                    "Sistema finalizado."
                )

                break


            else:

                print(
                    "Opción inválida."
                )



    def realizar_evaluacion(self):


        asesor = AsesorVocacional()


        estudiante = asesor.realizar_test()



        # Motor lógico

        motor = MotorReglas()


        roles_detectados, razones = motor.evaluar(
            estudiante.respuestas
        )



        print("\nRESULTADO DEL MOTOR LÓGICO")


        for rol, razon in zip(
            roles_detectados,
            razones
        ):

            print("\nRol:")
            print(rol)

            print("Motivo:")
            print(razon)




        # Cargar perfiles

        perfiles = CSVManager.cargar_perfiles(
            "datos/perfiles_roles_ti.csv"
        )



        resultados = []



        for perfil in perfiles:


            porcentaje = calcular_afinidad(
                estudiante,
                perfil
            )


            resultados.append(
                (
                    perfil.nombre,
                    porcentaje
                )
            )



        resultados.sort(
            key=lambda x:x[1],
            reverse=True
        )



        principal = resultados[0]

        secundario = resultados[1]



        print("\nRESULTADO FINAL")

        print(
            f"""
Rol principal:
{principal[0]}

Afinidad:
{principal[1]}%


Rol secundario:
{secundario[0]}

Afinidad:
{secundario[1]}%
"""
        )



        mostrar_competencias(
            estudiante.respuestas
        )


        brechas = detectar_brechas(
            estudiante.respuestas
        )



        # Guardar CSV

        fecha = datetime.now().strftime(
            "%d/%m/%Y"
        )


        CSVManager.guardar_evaluacion(
            "datos/evaluaciones_vocacionales.csv",
            estudiante.codigo,
            estudiante.carrera,
            principal[0],
            secundario[0],
            principal[1],
            fecha
        )



        # Crear reporte TXT

        GeneradorReporte.generar(
            estudiante,
            principal[0],
            principal[1],
            secundario[0],
            secundario[1],
            brechas,
            razones
        )



        print(
            "\nEvaluación completada."
        )




    def mostrar_estadisticas(self):


        estadistica = EstadisticasVocacionales(
            "datos/evaluaciones_vocacionales.csv",
            "datos/perfiles_roles_ti.csv"
        )


        estadistica.cargar_datos()


        estadistica.distribucion_roles()

        estadistica.promedio_afinidad()

        estadistica.demanda_vs_vocacion()

        estadistica.salarios_roles()




    def mostrar_perfiles(self):


        perfiles = CSVManager.cargar_perfiles(
            "datos/perfiles_roles_ti.csv"
        )


        print("\nPERFILES PROFESIONALES")


        for perfil in perfiles:


            print(
                f"""
----------------------------

Rol:
{perfil.nombre}

Demanda:
{perfil.demanda_mercado}%

Salario:
S/. {perfil.salario}

"""
            )