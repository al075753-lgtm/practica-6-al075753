# [CivilQuant modulo materiales]

from dosificaciones import obtener_dosificacion

def calcular_materiales(volumen, resistencia):

    dosificacion = obtener_dosificacion(resistencia)

    if dosificacion is None:
        return None

    cemento = volumen * dosificacion[0]
    cal = volumen * dosificacion[1]
    arena = volumen * dosificacion[2]
    grava = volumen * dosificacion[3]
    agua = volumen * dosificacion[4]

    sacos = int(cemento / 50)

    if cemento % 50 > 0:
        sacos += 1

    return [cemento, cal, arena, grava, agua, sacos]


if __name__ == "__main__":

    materiales = calcular_materiales(1.512, 200)

    print("Materiales calculados:", materiales)
