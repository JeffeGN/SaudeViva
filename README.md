<<<<<<< HEAD
# SaudeViva
Aplicação em Python e Streamlit para prever custos de planos de saúde com base em fatores individuais.
=======
# 📌 Case de Previsão de Custo Anual – SaúdeViva

Saúde acessível e previsível é essencial para um planejamento financeiro eficiente. Pensando nisso, o plano de saúde **SaúdeViva** busca oferecer **previsões precisas** para seus clientes, garantindo **transparência** no cálculo de custos com base em características individuais.

## 🏥 **Contexto do Negócio**
O setor de saúde suplementar enfrenta desafios na precificação de planos, pois fatores como **idade, IMC, hábitos como tabagismo, quantidade de filhos e região de residência** impactam diretamente os custos anuais de um beneficiário. No caso do **SaúdeViva**, a empresa opera em quatro regiões: **Norte, Nordeste, Sul e Sudeste**.  

Os cálculos são ajustados conforme as condições individuais dos clientes, garantindo preços mais justos e **reduzindo riscos para a empresa e consumidores**.

### 📌 **Ajuste de Regiões no Modelo**
Os dados utilizados neste projeto categorizam as regiões como **Northeast, Southeast, Northwest e Southwest**. No entanto, no Brasil, a divisão oficial inclui **Norte e Sul** em vez de Northwest e Southwest.  
Por isso, para alinhar o modelo à realidade nacional:  
✅ **Northwest foi tratado como Norte**  
✅ **Southwest foi tratado como Sul**  
Esse ajuste garante que as previsões fiquem coerentes com a segmentação geográfica oficial.

## 🎯 **Objetivo do Projeto**
Criamos um modelo de **Machine Learning** capaz de **prever o custo mensal e anual** do plano de saúde, permitindo à empresa estimar com **precisão** os valores cobrados. Isso otimiza o processo de cotação e melhora a experiência do usuário, garantindo que cada cliente receba uma oferta personalizada.

## 🚀 **Impacto no Mercado**
- 💰 **Redução de custos operacionais**: Automatizando a precificação, eliminamos processos manuais.
- 🏥 **Decisões mais assertivas**: A empresa pode ajustar preços de acordo com padrões de consumo e perfil de risco.
- 🤝 **Maior transparência**: Clientes entendem como suas características influenciam o custo do plano.

---

# 📊 **Análise da Importância das Variáveis na Previsão de Custos**

A precificação de planos de saúde é fortemente influenciada por diversos fatores individuais. Nosso modelo considera algumas variáveis fundamentais que impactam diretamente os custos anuais dos beneficiários.  

### **1️⃣ Idade** 📈  
A idade tem uma relação **direta e crescente** com o custo do plano de saúde. À medida que envelhecemos, estamos mais propensos a desenvolver **doenças crônicas** e demandar mais atendimentos médicos.  
➡ **Padrão observado:** Quanto maior a idade, maior o custo anual.  
➡ **Explicação:** O envelhecimento aumenta os custos com exames, consultas, tratamentos e internações.  

### **2️⃣ Tabagismo** 🚬  
Ser fumante **aumenta consideravelmente os custos**, pois está associado a doenças pulmonares, cardiovasculares e maior necessidade de acompanhamento médico.  
➡ **Impacto:** O custo médio dos fumantes é significativamente mais alto do que dos não fumantes.  
➡ **Explicação:** Além de problemas respiratórios, fumantes podem desenvolver câncer e outras condições graves, elevando os custos de tratamento.  

### **3️⃣ Índice de Massa Corporal (BMI)** ⚖  
O IMC elevado pode indicar sobrepeso ou obesidade, condições que aumentam os riscos de hipertensão, diabetes e problemas cardíacos.  
➡ **Padrão observado:** Pessoas com IMC maior tendem a ter custos mais altos.  
➡ **Explicação:** O excesso de peso está ligado a **comorbidades**, aumentando a frequência de exames e consultas médicas.  

### **4️⃣ Região de residência** 🌍  
O local onde o beneficiário mora impacta os custos do plano, pois diferentes regiões possuem **níveis de atendimento e custos operacionais distintos**.  
➡ **Padrão observado:** Diferenças significativas entre regiões, sendo algumas mais caras que outras.  
➡ **Explicação:** Infraestrutura hospitalar, custo de vida e demanda médica variam de acordo com a localização.  

### **5️⃣ Quantidade de filhos** 👶  
O número de filhos pode impactar diretamente os custos do plano de saúde, pois famílias maiores costumam demandar mais atendimentos médicos.  
➡ **Padrão observado:** Beneficiários com mais filhos tendem a ter custos médios mais altos.  
➡ **Explicação:** Crianças necessitam de **consultas pediátricas regulares**, vacinas, exames e tratamentos específicos, o que pode elevar os custos gerais do plano.

---

## 📌 **Conclusão**
Este projeto apresenta um **case realista**, simulando como um plano de saúde pode prever os custos anuais de seus beneficiários. Com a implementação de **Machine Learning**, o modelo permite que a empresa tome **decisões estratégicas**, melhore sua precificação e aumente a transparência para os clientes.  
>>>>>>> 3932e24 (Primeiro commit: adicionando arquivos iniciais)
