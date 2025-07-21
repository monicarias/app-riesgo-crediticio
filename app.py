import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo previamente entrenado
model = joblib.load('modelo_credito.pkl')

# Título de la app
st.title("Predicción de Riesgo Crediticio")

# Inputs del usuario
st.header("Ingresa la información del cliente:")

age = st.number_input("Edad", min_value=18, max_value=100, value=30)
job = st.selectbox("Tipo de trabajo (job)", [0, 1, 2, 3])
credit_amount = st.number_input("Monto del crédito", min_value=0, value=1000)
duration = st.slider("Duración del crédito (meses)", 6, 60, 12)

sex_male = st.radio("Sexo", ["Femenino", "Masculino"]) == "Masculino"
housing_own = st.radio("Tipo de vivienda", ["Alquilada", "Propia"]) == "Propia"
purpose_car = st.checkbox("¿El propósito del crédito es comprar un carro?")

# Crear DataFrame con los datos ingresados
input_data = pd.DataFrame([{
    "age": age,
    "job": job,
    "credit_amount": credit_amount,
    "duration": duration,
    "sex_male": int(sex_male),
    "housing_own": int(housing_own),
    "purpose_car": int(purpose_car)
    # Agrega aquí cualquier otra variable dummy que tu modelo esté esperando
}])

# Mostrar entrada
st.subheader("Vista previa de los datos ingresados:")
st.write(input_data)

# Botón para predecir
if st.button("Predecir riesgo crediticio"):
    prediction = model.predict(input_data)[0]
    resultado = "RIESGO BAJO ✅" if prediction == 1 else "RIESGO ALTO ⚠️"
    st.subheader(f"Resultado del modelo: {resultado}")
