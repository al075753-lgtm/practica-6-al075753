# [CivilQuant - Modulo de resistencia]

def obtener_dosificacion(resistencia):

    dosificaciones = {
        100: [239, 24, 780, 812, 205],
        150: [263, 26, 749, 825, 205],
        200: [323, 16, 705, 812, 210],
        250: [370, 19, 654, 786, 210]
    }

    if resistencia in dosificaciones:
        return dosificaciones[resistencia]
    else:
        return None


if __name__ == "__main__":

    resistencia = 200

    resultado = obtener_dosificacion(resistencia)

    print("Resistencia:", resistencia, "kg/cm2")
    print("Dosificacion:", resultado)
