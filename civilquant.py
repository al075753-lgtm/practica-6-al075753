
# CIVILQUANT
# Calculadora de materiales de construccion
# Modulo de concreto

from validar_datos import validar_dato
from calcular_volumen import aplicar_desperdicio
from calcular_materiales import calcular_materiales
from mostrar_resultados import mostrar_resultados
from elementos_concreto import calcular_losa, calcular_zapata, calcular_columna, calcular_trabe


def seleccionar_elemento():
    print("\n¿QUE ELEMENTO DESEAS CALCULAR?")
    print("1. Losa de concreto")
    print("2. Zapata de concreto")
    print("3. Columna de concreto")
    print("4. Trabe de concreto")

    opcion = input("Selecciona una opcion: ")

    while opcion not in ("1", "2", "3", "4"):
        print("Opcion invalida.")
        opcion = input("Selecciona una opcion: ")

    return opcion


def seleccionar_resistencia():
    print("\nRESISTENCIA DEL CONCRETO")
    print("1. f'c = 100 kg/cm2")
    print("2. f'c = 150 kg/cm2")
    print("3. f'c = 200 kg/cm2")
    print("4. f'c = 250 kg/cm2")

    resistencias = {
        "1": 100,
        "2": 150,
        "3": 200,
        "4": 250
    }

    opcion = input("Selecciona una opcion: ")

    while opcion not in resistencias:
        print("Opcion invalida.")
        opcion = input("Selecciona una opcion: ")

    return resistencias[opcion]


def validar_cantidad():
    cantidad = 0

    while cantidad <= 0:
        try:
            cantidad = int(input("Cantidad de elementos iguales: "))
            if cantidad <= 0:
                print("Ingresa un numero entero mayor que cero.")
        except ValueError:
            print("Ingresa un numero entero valido.")

    return cantidad


def validar_desperdicio():
    desperdicio = -1

    while desperdicio < 0:
        try:
            desperdicio = float(input("Porcentaje de desperdicio (%): "))
            if desperdicio < 0:
                print("El porcentaje no puede ser negativo.")
        except ValueError:
            print("Ingresa un numero valido.")

    return desperdicio


def calcular_elemento(opcion):
    if opcion == "1":
        nombre = "Losa de concreto"
        largo = validar_dato("Largo (m): ")
        ancho = validar_dato("Ancho (m): ")
        espesor = validar_dato("Espesor (m): ")
        volumen = calcular_losa(largo, ancho, espesor)

    elif opcion == "2":
        nombre = "Zapata de concreto"
        largo = validar_dato("Largo (m): ")
        ancho = validar_dato("Ancho (m): ")
        altura = validar_dato("Altura (m): ")
        volumen = calcular_zapata(largo, ancho, altura)

    elif opcion == "3":
        nombre = "Columna de concreto"
        base = validar_dato("Base (m): ")
        profundidad = validar_dato("Profundidad (m): ")
        altura = validar_dato("Altura (m): ")
        volumen = calcular_columna(base, profundidad, altura)

    else:
        nombre = "Trabe de concreto"
        base = validar_dato("Base (m): ")
        peralte = validar_dato("Peralte (m): ")
        longitud = validar_dato("Longitud (m): ")
        volumen = calcular_trabe(base, peralte, longitud)

    return nombre, volumen


def iniciar_civilquant():
    print("================================")
    print("          CIVILQUANT")
    print(" Calculadora de materiales")
    print("================================")

    print("\nMODULO DE CONCRETO")

    opcion = seleccionar_elemento()
    nombre, volumen_unitario = calcular_elemento(opcion)
    cantidad = validar_cantidad()
    resistencia = seleccionar_resistencia()
    desperdicio = validar_desperdicio()

    volumen_neto = volumen_unitario * cantidad
    volumen_total = aplicar_desperdicio(volumen_neto, desperdicio)
    materiales = calcular_materiales(volumen_total, resistencia)

    print("\nELEMENTO:", nombre)
    print("Cantidad de elementos:", cantidad)
    print("Volumen neto:", round(volumen_neto, 3), "m3")
    print("Desperdicio aplicado:", desperdicio, "%")

    mostrar_resultados(resistencia, volumen_total, materiales)


if __name__ == "__main__":
    iniciar_civilquant()
