def calcular_salario_bruto(valor_hora, horas_trabalhadas):
    return valor_hora * horas_trabalhadas

def calcular_horas_extras(salario_bruto, horas_trabalhadas, horas_extras):
    valor_hora_extra = (salario_bruto / horas_trabalhadas) * 1.5
    return horas_extras * valor_hora_extra

def calcular_inss(salario_bruto):
    if salario_bruto <= 1302:
        return salario_bruto * 0.075
    elif salario_bruto <= 2571.29:
        return salario_bruto * 0.09
    elif salario_bruto <= 3856.94:
        return salario_bruto * 0.12
    elif salario_bruto <= 7500:
        return salario_bruto * 0.14
    else:
        return 7500 * 0.14

def calcular_irrf(salario_bruto):
    if salario_bruto <= 1903.98:
        return 0
    elif salario_bruto <= 2826.65:
        return salario_bruto * 0.075 - 142.80
    elif salario_bruto <= 3751.05:
        return salario_bruto * 0.15 - 354.80
    elif salario_bruto <= 4664.68:
        return salario_bruto * 0.225 - 636.13
    else:
        return salario_bruto * 0.275 - 869.36

def calcular_férias_proporcionais(salario_bruto, meses_trabalhados):
    return salario_bruto / 12 * meses_trabalhados

def calcular_13_salario(salario_bruto, meses_trabalhados):
    return salario_bruto / 12 * meses_trabalhados

def calcular_fgts(salario_bruto):
    return salario_bruto * 0.08

def calcular_rescisao(salario_bruto, dias_trabalhados):
    saldo_salario = (salario_bruto / 30) * dias_trabalhados
    return saldo_salario
