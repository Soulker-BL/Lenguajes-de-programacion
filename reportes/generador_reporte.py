from datetime import datetime


class GeneradorReporte:
    """
    Genera un reporte resumen exportable
    del resultado vocacional.
    """

    @staticmethod
    def generar(
        estudiante,
        rol_principal,
        porcentaje_principal,
        rol_secundario,
        porcentaje_secundario,
        brechas,
        razones
    ):

        archivo_reporte = (
            f"reportes/reporte_{estudiante.codigo}.txt"
        )


        with open(
            archivo_reporte,
            "w",
            encoding="utf-8"
        ) as archivo:


            archivo.write(
                "=" * 55 + "\n"
            )

            archivo.write(
                "        REPORTE VOCACIONAL TI\n"
            )

            archivo.write(
                "=" * 55 + "\n\n"
            )


            archivo.write(
                "DATOS DEL ESTUDIANTE\n"
            )

            archivo.write(
                f"Código: {estudiante.codigo}\n"
            )

            archivo.write(
                f"Carrera: {estudiante.carrera}\n\n"
            )


            archivo.write(
                "ROL PROFESIONAL RECOMENDADO\n"
            )

            archivo.write(
                f"{rol_principal}\n"
            )

            archivo.write(
                f"Afinidad: {porcentaje_principal}%\n\n"
            )


            archivo.write(
                "ROL SECUNDARIO\n"
            )

            archivo.write(
                f"{rol_secundario}\n"
            )

            archivo.write(
                f"Afinidad: {porcentaje_secundario}%\n\n"
            )


            archivo.write(
                "MOTIVOS DE RECOMENDACIÓN\n"
            )


            for razon in razones:

                archivo.write(
                    f"- {razon}\n"
                )


            archivo.write(
                "\nHABILIDADES A FORTALECER\n"
            )


            if brechas:

                for habilidad in brechas:

                    archivo.write(
                        f"- Mejorar {habilidad}\n"
                    )

            else:

                archivo.write(
                    "No se encontraron brechas críticas.\n"
                )


            archivo.write(
                "\nFecha: "
            )

            archivo.write(
                datetime.now().strftime(
                    "%d/%m/%Y"
                )
            )


        print(
            "\nReporte generado correctamente:"
        )

        print(
            archivo_reporte
        )