# [CivilQuant - Calculo de elementos de concreto]

def calcular_losa(largo, ancho, espesor):
    volumen = largo * ancho * espesor
    return volumen


def calcular_zapata(largo, ancho, altura):
    volumen = largo * ancho * altura
    return volumen


def calcular_columna(base, profundidad, altura):
    volumen = base * profundidad * altura
    return volumen


def calcular_trabe(base, peralte, longitud):
    volumen = base * peralte * longitud
    return volumen


def validar_dimension(valor):
    if valor > 0:
        return True
    else:
        return False


if __name__ == "__main__":

    # Prueba 1: Losa
    volumen = calcular_losa(5, 4, 0.12)
    print("Volumen de losa:", volumen, "m3")

    # Prueba 2: Zapata
    volumen = calcular_zapata(1.5, 1.5, 0.40)
    print("Volumen de zapata:", volumen, "m3")

    # Prueba 3: Columna
    volumen = calcular_columna(0.30, 0.30, 3)
    print("Volumen de columna:", volumen, "m3")

    # Prueba 4: Trabe
    volumen = calcular_trabe(0.25, 0.40, 5)
    print("Volumen de trabe:", volumen, "m3")

    # Prueba 5: Validacion
    print("Dimension valida:", validar_dimension(5))
    print("Dimension invalida:", validar_dimension(-2))
