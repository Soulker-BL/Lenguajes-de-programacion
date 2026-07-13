def generar_barra(valor, longitud=20):
    """
    Genera una barra gráfica ASCII según un porcentaje.
    """

    cantidad = int((valor / 100) * longitud)

    return "█" * cantidad + "-" * (longitud - cantidad)



def mostrar_competencias(respuestas):
    """
    Muestra las competencias del estudiante
    mediante barras ASCII.
    """

    nombres = [
        "Algoritmos",
        "Matematicas",
        "Diseño Visual",
        "Comunicacion",
        "Automatizacion",
        "Atencion Detalle",
        "Ciberseguridad",
        "Trabajo Independiente",
        "Trabajo Presion",
        "Analisis Datos",
        "Investigacion",
        "Liderazgo"
    ]


    print("\n========== COMPETENCIAS ==========")


    for numero, respuesta in respuestas.items():

        porcentaje = (respuesta - 1) * 25

        barra = generar_barra(
            porcentaje
        )


        print(
            f"{nombres[numero-1]:25} {barra} {porcentaje}%"
        )



def detectar_brechas(respuestas):
    """
    Identifica habilidades que necesitan mejora.
    """

    nombres = {
        1:"Algoritmos",
        2:"Matemáticas",
        3:"Diseño Visual",
        4:"Comunicación",
        5:"Automatización",
        6:"Atención al detalle",
        7:"Ciberseguridad",
        8:"Trabajo independiente",
        9:"Trabajo bajo presión",
        10:"Análisis de datos",
        11:"Investigación",
        12:"Liderazgo"
    }


    brechas = []


    for clave, valor in respuestas.items():

        if valor <= 2:

            brechas.append(
                nombres[clave]
            )


    print("\n========== HABILIDADES A FORTALECER ==========")


    if len(brechas) == 0:

        print(
            "No se detectaron brechas importantes."
        )

    else:

        for habilidad in brechas:

            print(
                "- Mejorar " + habilidad
            )


    return brechas