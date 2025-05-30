# 📊 SaúdeViva – Previsão de Custos de Planos de Saúde  

## 🚀 Visão Geral  

- [IBGE: População brasileira chega a 52.1 milhões](https://www.gov.br/secom/pt-br/assuntos/noticias/2024/08/populacao-do-brasil-chega-a-212-6-milhoes-de-habitantes-aponta-ibge)
- [ANS: Benefciários de plano de saúde chega a 216.6 milhões](https://www.gov.br/ans/pt-br/assuntos/noticias/numeros-do-setor/setor-de-planos-de-saude-fecha-2024-com-numeros-recordes-de-beneficiarios)
- Segundo os dados do IBGE e da ANS, apenas 24% da população brasileira possui plano de saúde, um número bem baixo.

O **SaúdeViva** é uma aplicação desenvolvida em **Python** e **Streamlit**, projetada para estimar os custos de planos de saúde com base em fatores individuais. O objetivo é oferecer **transparência na precificação**, permitindo que os usuários visualizem como **idade, IMC, tabagismo e número de filhos** impactam no valor final.

Esse projeto foi criado para demonstrar **habilidades em Ciência de Dados**, abrangendo **análise exploratória**, **tratamento de dados**, **Machine Learning**, **validação de modelos** e **deploy de aplicações interativas**.

---

## 📑 Notebook e Dashboard do Projeto  

🔗 **[Notebook no GitHub](https://github.com/JeffeGN/SaudeViva/blob/main/Plano%20de%20Sa%C3%BAde.ipynb)**  
🔗 **[Aplicação via Streamlit Cloud](https://saudeviva-mj29yxjmdhwgsxx7we2xtb.streamlit.app/)**

---

## 📈 Impacto do Projeto  

### 🔹 **Benefícios para Consumidores**  
✔️ **Transparência na precificação** – Permite que usuários compreendam como fatores individuais afetam o custo do plano de saúde.  
✔️ **Escolha informada** – Os clientes podem simular diferentes cenários antes de contratar um plano, evitando gastos inesperados.  
✔️ **Comparação inteligente** – Potencial para ajudar consumidores a comparar opções de planos de diferentes operadoras.  

### 🔹 **Benefícios para Empresas e Seguradoras**  
✔️ **Otimização da precificação** – Empresas podem ajustar políticas de preços de forma mais eficiente, considerando riscos individuais.  
✔️ **Melhoria na retenção de clientes** – Oferecendo transparência, seguradoras podem fortalecer a relação de confiança com consumidores.  
✔️ **Análise de risco aprimorada** – Modelos como LightGBM podem ajudar na identificação de perfis de maior risco, ajustando estratégias de precificação.  

### 🔹 **Possibilidades de Expansão do Projeto**  
✅ **Inclusão de novos fatores** como histórico médico, cidade e estado, para previsões ainda mais precisas.  
✅ **Aplicação comercial** – Modelo pode ser adaptado para que seguradoras utilizem previsões em seus sistemas internos.  
✅ **Treinamento contínuo** – Implementação de aprendizado incremental com IA para que o modelo se ajuste a novas tendências do mercado.  

---

## 🎯 Habilidades Demonstradas  
✔️ Manipulação de dados com pandas e numpy, garantindo organização e limpeza dos registros.  
✔️ Análise exploratória de dados (EDA) utilizando histogramas, boxplots e matriz de correlação.  
✔️ Engenharia de features, realizando transformação de variáveis categóricas e normalização de dados.  
✔️ Testes de diferentes algoritmos de Machine Learning para avaliar precisão e desempenho.  
✔️ Uso de um modelo baseline para comparar o desempenho das abordagens preditivas.  
✔️ Validação de modelos utilizando métricas como MAE, RMSE, R² e Cross-validation.  
✔️ Teste de generalização para identificar overfitting e underfitting usando curvas de aprendizado.  
✔️ Otimização de hiperparâmetros com Bayesian Search para os modelos mais promissores.  
✔️ Criação de um dashboard interativo utilizando **Streamlit**.  
✔️ Deploy do projeto no **GitHub** e **Streamlit Cloud**, tornando a aplicação acessível diretamente online.  
✔️ Tratamento de duplicatas com a implementação de critérios para remoção seletiva de duplicatas sem ID, garantindo a qualidade dos dados.  
✔️ Análise estatística de distribuição através da avaliação do skewness para identificar variáveis que precisavam de transformação.  
✔️ Interpretação de estatísticas com cálculo e análise do impacto da transformação nos dados, verificando a redução da assimetria.  
✔️ Transformação de dados aplicando transformação Yeo-Johnson para normalizar distribuições assimétricas.  
✔️ Teste de normalidade dos dados utilizando Kolmogorov-Smirnov, verificando a aderência das distribuições às premissas estatísticas.  
✔️ Identificação de variáveis que necessitam de transformação para melhorar a qualidade dos dados e otimizar a modelagem preditiva.

---

## 📌 Aprendizados e Desafios  

Durante o desenvolvimento do projeto, foram enfrentados desafios relacionados à manipulação e modelagem dos dados, bem como à implementação e deploy da aplicação.  

✔️ **Tratamento de dados geográficos** – O dataset original não continha as regiões Sul e Norte do Brasil. Para garantir representatividade, as regiões Noroeste e Sudoeste foram utilizadas como referência.  
✔️ **Escolha do modelo final** – Random Forest e LightGBM apresentaram resultados promissores e semelhantes. No entanto, após a otimização dos hiperparâmetros, o LightGBM demonstrou desempenho significativamente superior, sendo adotado como modelo final.  
✔️ **Ajuste de formato monetário** – Após o deploy com **Streamlit**, identificou-se que os valores monetários não estavam no padrão brasileiro. Para correção, foi desenvolvida uma função utilizando `lambda`, garantindo a correta formatação dos preços.  
✔️ **Deploy na nuvem e compatibilidade de dependências** – O arquivo `requirements.txt` apresentou incompatibilidades com o **Streamlit Community Cloud**, exigindo ajustes para versões compatíveis e atualizadas das bibliotecas utilizadas, permitindo a execução correta do deploy.  

A resolução desses desafios contribuiu para o aprimoramento de habilidades essenciais em Ciência de Dados, como engenharia de features, otimização de modelos, padronização de dados e implementação de soluções web interativas.  

---

## 🛠 Tecnologias Utilizadas  

### 📊 Manipulação e Visualização de Dados  
✔️ pandas → Estruturação, limpeza e análise de datasets.  
✔️ numpy → Cálculos matemáticos para tratamento de variáveis numéricas.  
✔️ matplotlib / seaborn → Criação de gráficos exploratórios e análise estatística.  

### 🤖 Modelagem Preditiva e Machine Learning  
✔️ scikit-learn → Implementação de algoritmos para previsão de custos.  
✔️ learning_curve → Utilizado para análise da curva de aprendizado e avaliação de generalização do modelo.  
✔️ xgboost → Modelo testado por sua robustez e alta performance.  
✔️ lightgbm → Escolhido como modelo final por seu consumo otimizado de recursos.  
✔️ random forest → Avaliado por sua precisão e interpretabilidade.  
✔️ pickle → Serialização do modelo para integração no dashboard.  
✔️ Aplicação do Teste de Kolmogorov-Smirnov para avaliar a normalidade das distribuições antes da transformação das variáveis.  
✔️ Uso de técnicas de transformação como Yeo-Johnson, ajustando a distribuição dos dados para melhorar a performance dos modelos.  
✔️ Implementação de LightGBM e Random Forest, avaliando trade-offs entre desempenho e escalabilidade.  


### 🖥️ Desenvolvimento Web e Deploy  
✔️ **Streamlit → Interface interativa para visualização das previsões, também disponível via Streamlit Cloud.**  
✔️ **GitHub → Hospedagem do código-fonte e documentação profissional, integrando a aplicação ao ambiente online.**  

---

## 📊 Etapas do Projeto  

### **1️⃣ Baseline para Avaliação de Modelos**  
- A **Regressão Linear** foi usada como **baseline** para medir a eficácia dos algoritmos preditivos.  
- Comparação de **múltiplos modelos**, garantindo uma análise robusta antes da escolha do modelo final.  

### **2️⃣ Modelos Testados**  
Os seguintes algoritmos foram treinados e avaliados:  
✔️ **Regressão Linear** → Modelo inicial para comparação de desempenho.  
✔️ **Regressão Ridge** → Testado para redução de multicolinearidade.  
✔️ **Regressão Lasso** → Aplicado para seleção de features relevantes.  
✔️ **XGBoost Regressor** → Avaliado por sua capacidade de generalização.  
✔️ **LightGBM Regressor** → Destacado por seu baixo consumo computacional e rapidez.  
✔️ **Random Forest Regressor** → Obteve desempenho próximo ao LightGBM.  

### **3️⃣ Otimização de Modelos com Bayesian Search**  
Os modelos **Random Forest** e **LightGBM** apresentaram resultados similares, então ambos foram **otimizados com Bayesian Search** para ajuste fino dos hiperparâmetros.  

✔️ O **LightGBM** foi escolhido como modelo final por **ser mais rápido e consumir menos recursos**, tornando-se ideal para deploy com **Streamlit**.  

### **4️⃣ Validação de Modelos**  
✔️ **Mean Absolute Error (MAE)** → Avaliação do erro absoluto médio entre previsões e valores reais.  
✔️ **Root Mean Squared Error (RMSE)** → Interpretação do erro considerando unidades originais.  
✔️ **R² Score** → Medida da capacidade do modelo em explicar a variabilidade dos custos.  
✔️ **Cross-validation (K-Fold)** → Aplicação para garantir **generalização** do modelo.  

### **5️⃣ Construção do Dashboard Interativo com Streamlit**  
✔️ Interface intuitiva para entrada de dados do usuário.  
✔️ Exibição do custo mensal e anual com detalhamento dos fatores que impactam na precificação.  
✔️ Geração dinâmica de previsões conforme os inputs do usuário.  

---

## 💰 Estrutura do Cálculo  

O custo do plano de saúde é ajustado com um valor base **anual** de **R$ 4.000**, adicionando incrementos conforme os seguintes fatores:

| Fator | Acréscimo Mensal |
|-------|----------------|
| **Idade** | + R$ 8,33 por ano |
| **IMC** | + R$ 4,16 por ponto de IMC |
| **Tabagismo** | + R$ 208,33 se fumante |
| **Número de Filhos** | + R$ 41,66 por filho |

O valor total é calculado e exibido na interface do **Streamlit**, permitindo ao usuário visualizar tanto o custo **mensal** quanto **anual**.

---

## 🔧 Pré-requisitos  

Antes de iniciar, verifique se o **Python 3.9 ou superior** está instalado no seu sistema.  

1️⃣ **Verifique se o Python está instalado**  
```bash
python --version
```
Se o comando não retornar uma versão do Python, instale-o [aqui](https://www.python.org/downloads/).

2️⃣ Verifique se o Git está instalado
```bash
git --version
```

Se o comando não retornar uma versão do Git, instale-o [aqui](https://git-scm.com/downloads).

---

## 🎮 Como Executar Localmente  

1️⃣ **Clone o repositório**  
```bash
git clone https://github.com/JeffeGN/SaudeViva.git
```

2️⃣ Acesse o diretório do projeto
```bash
cd SaudeViva
```
3️⃣ Instale as dependências listadas em requirements.txt
```bash
pip install -r requirements.txt
```
4️⃣ Acesse o diretório da aplicação Streamlit
```bash
cd streamlit_app
```
5️⃣ Execute a aplicação Streamlit
```bash
streamlit run app.py
```
6️⃣ Insira seus dados na interface e veja sua estimativa de custo  

![image](https://github.com/user-attachments/assets/279f2e76-7965-4fbf-a80e-97f48900b042)

