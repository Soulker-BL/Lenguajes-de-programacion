from functools import reduce


# ==========================================
# Función pura
# ==========================================

def normalizar(valor):
    """
    Convierte una respuesta de la escala 1-5
    a un porcentaje (0-100).
    """
    return (valor - 1) * 25


# ==========================================
# Función de orden superior
# ==========================================

def transformar(lista, funcion):
    """
    Aplica una función a todos los elementos
    de una lista.
    """
    return list(map(funcion, lista))


# ==========================================
# Cálculo de afinidad
# ==========================================

def calcular_afinidad(estudiante, perfil):

    # Respuestas del estudiante
    respuestas = list(estudiante.respuestas.values())

    # Uso de map()
    respuestas_normalizadas = transformar(
        respuestas,
        lambda x: normalizar(x)
    )

    # Pesos del perfil
    pesos = [
        perfil.peso_algoritmos,
        perfil.peso_matematicas,
        perfil.peso_diseno_visual,
        perfil.peso_comunicacion,
        perfil.peso_infraestructura
    ]

    # Solo tomamos las primeras 5 preguntas
    respuestas_principales = respuestas_normalizadas[:5]

    productos = list(
        map(
            lambda datos: datos[0] * datos[1],
            zip(respuestas_principales, pesos)
        )
    )

    suma = reduce(lambda a, b: a + b, productos)

    porcentaje = suma / sum(pesos)

    if porcentaje > 100:
        porcentaje = 100

    return round(porcentaje, 2)


# ==========================================
# Fortalezas
# ==========================================

def obtener_fortalezas(estudiante):

    respuestas = list(estudiante.respuestas.values())

    normalizadas = transformar(
        respuestas,
        lambda x: normalizar(x)
    )

    fuertes = list(
        filter(
            lambda x: x >= 75,
            normalizadas
        )
    )

    return fuertes