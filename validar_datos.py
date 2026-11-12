# [CivilQuant modulo de validacion]

def validar_dato(mensaje):

    numero = None

    while numero is None:

        try:
            valor = float(input(mensaje))

            if valor > 0:
                numero = valor
            else:
                print("El valor debe ser mayor que cero")

        except ValueError:
            print("Ingresa un numero valido")

    return numero


if __name__ == "__main__":

    largo = validar_dato("Ingresa el largo: ")

    print("Largo ingresado:", largo)
