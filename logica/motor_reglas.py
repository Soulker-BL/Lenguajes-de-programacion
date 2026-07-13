class MotorReglas:
    """
    Motor de inferencia encargado de analizar las respuestas
    del estudiante y deducir el rol profesional más adecuado.
    """

    def evaluar(self, respuestas):

        roles = []
        explicaciones = []


        if (
            respuestas[1] >= 4 and
            respuestas[8] >= 4 and
            respuestas[3] <= 2
        ):
            roles.append("Backend Developer")
            explicaciones.append(
                "Alta capacidad lógica, preferencia por algoritmos y trabajo individual."
            )

        if (
            respuestas[6] == 5 and
            respuestas[6] >= 4
        ):
            roles.append("QA Automation Engineer")
            explicaciones.append(
                "Gran atención al detalle y facilidad para detectar errores."
            )


        if (
            respuestas[4] >= 4 and
            respuestas[12] >= 4
        ):
            roles.append("IT Project Manager / Scrum Master")
            explicaciones.append(
                "Buenas habilidades de comunicación y liderazgo."
            )


        if (
            respuestas[2] >= 4 and
            respuestas[10] >= 4
        ):
            roles.append("Data Engineer / BI Analyst")
            explicaciones.append(
                "Afinidad por matemáticas y análisis de datos."
            )


        if (
            respuestas[3] >= 4 and
            respuestas[4] >= 5
        ):
            roles.append("UX/UI Product Designer")
            explicaciones.append(
                "Alta sensibilidad visual y orientación hacia el usuario."
            )


        if (
            respuestas[5] >= 4 and
            respuestas[9] >= 4
        ):
            roles.append("DevOps / Cloud Engineer")
            explicaciones.append(
                "Interés por la automatización y buen desempeño bajo presión."
            )

        if (
            respuestas[7] >= 4 and
            respuestas[11] >= 4
        ):
            roles.append("Cybersecurity Blue Team Analyst")
            explicaciones.append(
                "Interés por la investigación y la seguridad informática."
            )


        tecnicas = [
            respuestas[1],
            respuestas[2],
            respuestas[3],
            respuestas[5],
            respuestas[7],
            respuestas[10],
            respuestas[11]
        ]

        if all(valor <= 2 for valor in tecnicas):
            roles.append("Alerta Vocacional")
            explicaciones.append(
                "Se recomienda reforzar los fundamentos de computación."
            )

        if len(roles) == 0:
            roles.append("Perfil General TI")
            explicaciones.append(
                "No se encontró un perfil claramente dominante."
            )

        return roles, explicaciones