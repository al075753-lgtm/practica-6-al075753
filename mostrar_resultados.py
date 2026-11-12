# [CivilQuant]

def mostrar_resultados(resistencia, volumen, materiales):

    print("\nRESULTADOS CIVILQUANT")
    print("----------------------------")

    print("Resistencia:", resistencia, "kg/cm2")
    print("Volumen total:", round(volumen, 3), "m3")

    print("Cemento:", round(materiales[0], 2), "kg")
    print("Cal hidratada:", round(materiales[1], 2), "kg")
    print("Arena:", round(materiales[2], 2), "kg")
    print("Grava:", round(materiales[3], 2), "kg")
    print("Agua:", round(materiales[4], 2), "litros")

    print("Sacos de cemento de 50 kg:", materiales[5])

    print("----------------------------")
    print("Dosificacion aproximada de referencia.")
    print("No sustituye un diseno de mezcla verificado.")
