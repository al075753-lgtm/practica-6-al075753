# [CivilQuant modulo volumen]

def calcular_volumen(largo, ancho, espesor):

    volumen = largo * ancho * espesor

    return volumen


def aplicar_desperdicio(volumen, porcentaje):

    volumen_total = volumen * (1 + porcentaje / 100)

    return volumen_total


if __name__ == "__main__":

    volumen = calcular_volumen(4, 3, 0.12)

    volumen_total = aplicar_desperdicio(volumen, 5)

    print("Volumen:", volumen, "m3")
    print("Volumen con desperdicio:", volumen_total, "m3")
