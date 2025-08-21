# Projeto SaúdeViva: Previsão de Custos de Planos de Saúde

## Contextualização
- [IBGE: População brasileira chega a 212,6 milhões](https://www.gov.br/secom/pt-br/assuntos/noticias/2024/08/populacao-do-brasil-chega-a-212-6-milhoes-de-habitantes-aponta-ibge)
- [ANS: Benefciários de plano de saúde chega a 216,6 milhões](https://www.gov.br/ans/pt-br/assuntos/noticias/numeros-do-setor/setor-de-planos-de-saude-fecha-2024-com-numeros-recordes-de-beneficiarios)
- Segundo os dados do IBGE e da ANS, apenas 24% da população brasileira possui plano de saúde.

## Notebook e Dashboard do Projeto  
- [**Notebook no GitHub**](https://github.com/JeffeGN/SaudeViva/blob/main/Plano%20de%20Sa%C3%BAde.ipynb)  
- [**Aplicação via Streamlit Cloud**](https://saudeviva-mj29yxjmdhwgsxx7we2xtb.streamlit.app/)

## Visão Geral do Projeto

Este projeto desenvolve uma solução completa de ciência de dados para o setor de saúde, transformando um problema de transparência na precificação de planos em uma aplicação web funcional. Considerando que apenas 24% da população brasileira possui plano de saúde, a solução permite que usuários compreendam como fatores individuais impactam no custo final de seus planos.

## Arquitetura e Metodologia

### **Estrutura de Dados e Pipeline**
O projeto implementa um pipeline de dados estruturado com módulos organizados (`src/`, `dados/`, `modelos/`, `streamlit_app/`), garantindo reprodutibilidade e manutenibilidade. A extração utiliza função personalizada `carregar_dados()` para padronização, enquanto o tratamento inclui critérios específicos para remoção seletiva de duplicatas sem comprometer a integridade dos dados.

### **Análise Estatística e Transformações**
A análise exploratória revela distribuições assimétricas que requerem tratamento estatístico. Implementei:
- **Teste de Kolmogorov-Smirnov** para validação de normalidade das distribuições
- **PowerTransformer (Yeo-Johnson)** para correção de assimetria nas variáveis numéricas
- **Análise de skewness** para identificação de variáveis que necessitam transformação
- **Feature Engineering** com criação de variável categórica `bmi_category` baseada em faixas clínicas

### **Modelagem Preditiva**
O desenvolvimento seguiu metodologia científica rigorosa:

**Baseline e Comparação**: Regressão Linear como modelo de referência para medir eficácia de algoritmos mais complexos (Ridge, Lasso, XGBoost, LightGBM, Random Forest).

**Otimização**: Aplicação de Bayesian Search nos modelos mais promissores (Random Forest e LightGBM) para ajuste fino de hiperparâmetros.

**Validação Robusta**: 
- Cross-validation (K-Fold) para garantir generalização
- Curvas de aprendizado para detecção de overfitting/underfitting
- Métricas múltiplas (MAE, RMSE, R²) para avaliação completa

**Modelo Final**: LightGBM selecionado após análise comparativa por apresentar performance superior com menor consumo computacional, ideal para deploy em produção.

## Soluções Técnicas Implementadas

### **Desafios de Dados**
- **Representatividade geográfica**: Dataset original sem regiões Sul/Norte adaptado usando Noroeste/Sudoeste como referência para manter cobertura nacional
- **Qualidade de dados**: Implementação de critérios específicos para tratamento de duplicatas preservando informações relevantes

### **Deploy e Compatibilidade**
- **Streamlit Cloud**: Resolução de incompatibilidades de dependências através de ajuste do `requirements.txt` para versões compatíveis
- **Formatação localizada**: Desenvolvimento de função lambda customizada para padrão monetário brasileiro
- **Interface responsiva**: Dashboard intuitivo com entrada de dados em tempo real

## Stack Tecnológico

### **Análise e Modelagem**
- **Python**: Pandas, NumPy para manipulação de dados
- **Machine Learning**: Scikit-learn, XGBoost, LightGBM
- **Estatística**: SciPy para testes de normalidade e transformações
- **Visualização**: Matplotlib, Seaborn para análise exploratória

### **Deploy e Produto**
- **Web Framework**: Streamlit para interface interativa
- **Cloud**: Streamlit Cloud para hospedagem
- **Versionamento**: GitHub com estrutura profissional de repositório
- **Serialização**: Pickle para persistência de modelo

## Lógica de Negócio

O sistema implementa estrutura de cálculo transparente baseada em fatores de risco:

| Fator | Impacto Mensal |
|-------|----------------|
| **Base anual** | R$ 4.000 |
| **Idade** | +R$ 8,33 por ano |
| **IMC** | +R$ 4,16 por ponto |
| **Tabagismo** | +R$ 208,33 se fumante |
| **Filhos** | +R$ 41,66 por filho |

## Resultados e Impacto

### **Solução Técnica**
- **Aplicação web funcional** com previsões em tempo real
- **Modelo otimizado** com validação estatística rigorosa
- **Pipeline reproduzível** com código documentado e versionado
- **Deploy automatizado** em ambiente de produção

### **Valor para o Setor**
- **Transparência na precificação** permitindo compreensão dos fatores de custo
- **Otimização de estratégias** para identificação de perfis de risco
- **Base para expansão** com potencial para inclusão de novos fatores preditivos

## Pré-requisitos  
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

## Como Executar Localmente  

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

- **Repositório**: Código fonte completo e documentação técnica
- **Aplicação**: Interface web acessível via Streamlit Cloud
- **Notebook**: Análise exploratória e desenvolvimento de modelos disponíveis

A solução demonstra capacidade técnica completa em ciência de dados, desde a concepção do problema até a entrega de produto funcional, seguindo boas práticas de engenharia de software e metodologia científica.