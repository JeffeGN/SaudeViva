import streamlit as st

def calcular_bmi(peso, altura):
    """Calcula o BMI com base no peso (kg) e altura (m)."""
    return round(peso / (altura ** 2), 2)

def interpretar_bmi(bmi, sexo):
    """Retorna a interpretação do BMI baseada em tabelas médicas padrão."""
    if sexo.lower() == "male":
        if bmi < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            return "Peso normal"
        elif 25 <= bmi < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"
    else:  # Para sexo "female"
        if bmi < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            return "Peso normal"
        elif 25 <= bmi < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

# Interface no Streamlit
st.title("Calculadora de BMI (Índice de Massa Corporal)")

# Entrada do usuário
peso = st.number_input("Informe seu peso (kg):", min_value=30.0, max_value=200.0, step=0.1)
altura = st.number_input("Informe sua altura (m):", min_value=1.0, max_value=2.5, step=0.01)
sexo = st.selectbox("Selecione seu sexo:", ["male", "female"])

# Cálculo e exibição do BMI
if st.button("Calcular BMI"):
    bmi = calcular_bmi(peso, altura)
    interpretacao = interpretar_bmi(bmi, sexo)
    st.success(f"Seu BMI é {bmi}. Classificação: {interpretacao}.")
