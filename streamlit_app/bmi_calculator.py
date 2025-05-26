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