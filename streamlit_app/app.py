import streamlit as st
from bmi_calculator import calcular_bmi, interpretar_bmi

# Título da aplicação
st.title("Previsão de Custo do Plano de Saúde – SaúdeViva")

# Entradas do usuário
peso = st.number_input("Informe seu peso (kg):", min_value=30.0, max_value=600.0, step=0.1, key="peso_input")
altura = st.number_input("Informe sua altura (m):", min_value=1.0, max_value=3.0, step=0.01, key="altura_input")
sexo = st.selectbox("Selecione seu sexo:", ["Masculino", "Feminino"], key="sexo_input")
idade = st.number_input("Informe sua idade:", min_value=18, max_value=150, step=1, key="idade_input")
tabagismo = st.selectbox("Você é fumante?", ["Sim", "Não"], key="tabagismo_input")
children = st.number_input("Quantos filhos você tem?", min_value=0, max_value=20, step=1, key="children_input")

# Botão para previsão de custo
if st.button("Prever Custo do Plano de Saúde"):
    # Calculando BMI com os dados informados pelo usuário
    bmi = calcular_bmi(peso, altura)
    interpretacao_bmi = interpretar_bmi(bmi, sexo)

    # Simulação de previsão de custo
    custo_base = 4000  # Valor inicial estimado
    adicional_idade = idade * 100
    adicional_tabagismo = 2500 if tabagismo == "Sim" else 0
    adicional_filhos = children * 500
    adicional_bmi = bmi * 50

    # Somando todos os fatores
    custo_anual = custo_base + adicional_idade + adicional_tabagismo + adicional_filhos + adicional_bmi
    custo_mensal = custo_anual / 12

    # Ajuste da moeda para o formato brasileiro
    ajuste = lambda valor: f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    # Exibição das estimativas
    st.success(f"💰 Estimativa de **custo mensal** do plano de saúde: **R$ {ajuste(custo_mensal)}**")
    st.success(f"📅 Estimativa de **custo anual** do plano de saúde: **R$ {ajuste(custo_anual)}**")

    # Exibição dos custos individuais
    st.subheader("Como este valor é calculado:")
    st.write(f"📌 Custo Base: **R$ {ajuste(custo_base / 12)}** / mês")
    st.write(f"👴 Acréscimo pela idade: **R$ {ajuste(adicional_idade / 12)}** / mês")
    st.write(f"🚬 Acréscimo pelo tabagismo: **R$ {ajuste(adicional_tabagismo / 12)}** / mês")
    st.write(f"👶 Acréscimo pelo número de filhos: **R$ {ajuste(adicional_filhos / 12)}** / mês")
    st.write(f"⚖️ Acréscimo pelo IMC: **R$ {ajuste(adicional_bmi / 12)}** / mês")
