
import streamlit as st

from calcular_materiales import calcular_materiales
from elementos_concreto import calcular_losa, calcular_zapata, calcular_columna, calcular_trabe
from calcular_volumen import aplicar_desperdicio

st.title("🏗️ CivilQuant")
st.write("Calculadora de materiales de construcción")

st.subheader("Selecciona el elemento constructivo")

elemento = st.selectbox(
    "Tipo de elemento:",
    ["Losa", "Zapata", "Columna", "Trabe"]
)

st.subheader("Ingresa las dimensiones")

if elemento == "Losa":
    medida1 = st.number_input("Largo (m)", min_value=0.01, value=5.0)
    medida2 = st.number_input("Ancho (m)", min_value=0.01, value=4.0)
    medida3 = st.number_input("Espesor (m)", min_value=0.01, value=0.12)

elif elemento == "Zapata":
    medida1 = st.number_input("Largo (m)", min_value=0.01, value=1.5)
    medida2 = st.number_input("Ancho (m)", min_value=0.01, value=1.5)
    medida3 = st.number_input("Altura (m)", min_value=0.01, value=0.40)

elif elemento == "Columna":
    medida1 = st.number_input("Base (m)", min_value=0.01, value=0.30)
    medida2 = st.number_input("Profundidad (m)", min_value=0.01, value=0.30)
    medida3 = st.number_input("Altura (m)", min_value=0.01, value=3.0)

else:
    medida1 = st.number_input("Base (m)", min_value=0.01, value=0.25)
    medida2 = st.number_input("Peralte (m)", min_value=0.01, value=0.40)
    medida3 = st.number_input("Longitud (m)", min_value=0.01, value=5.0)

desperdicio = st.number_input(
    "Desperdicio (%)",
    min_value=0.0,
    value=5.0
)

cantidad = st.number_input(
    "Cantidad de elementos iguales",
    min_value=1,
    value=1,
    step=1
)

resistencia = st.selectbox(
    "Resistencia del concreto (kg/cm²)",
    [100, 150, 200, 250]
)


if st.button("Calcular volumen"):

    if elemento == "Losa":
        volumen = calcular_losa(medida1, medida2, medida3)

    elif elemento == "Zapata":
        volumen = calcular_zapata(medida1, medida2, medida3)

    elif elemento == "Columna":
        volumen = calcular_columna(medida1, medida2, medida3)

    else:
        volumen = calcular_trabe(medida1, medida2, medida3)

    volumen = volumen * cantidad
    volumen_total = aplicar_desperdicio(volumen, desperdicio)


    st.success("¡Cálculo realizado correctamente!")

    st.write("Elemento:", elemento)
    st.write("Volumen neto:", round(volumen, 3), "m³")
    st.write("Volumen con desperdicio:", round(volumen_total, 3), "m³")

    materiales = calcular_materiales(volumen_total, resistencia)

    if materiales is not None:
        st.subheader("Materiales estimados")

        st.write("Cemento:", round(materiales[0], 2), "kg")
        st.write("Cal hidratada:", round(materiales[1], 2), "kg")
        st.write("Arena:", round(materiales[2], 2), "kg")
        st.write("Grava:", round(materiales[3], 2), "kg")
        st.write("Agua:", round(materiales[4], 2), "litros")
        st.write("Sacos de cemento de 50 kg:", materiales[5])

        st.warning(
            "Dosificación didáctica no verificada. "
            "La inclusión de cal hidratada requiere revisión técnica. "
            "No utilizar estas cantidades para preparar concreto en obra."
        )

    else:
        st.error("No se encontró la dosificación seleccionada.")

