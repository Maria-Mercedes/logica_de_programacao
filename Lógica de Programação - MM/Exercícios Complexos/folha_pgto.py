salario_bruto = float(input("Informe o salário:\n"))
horas_trabalhadas = int(input("Informe as horas trabalhadas: \n"))
fez_horas_extras = input("Fez horas extras?: (s/n)")
vale_transporte = input("Utiliza VT?: (s/n)")

salario_liquido = 0
desconto_inss = 0
desconto_VT = 0
valor_hora_extra = 0

if salario_bruto > 0 and horas_trabalhadas > 0:
    #Desconto INSS
    if salario_bruto <= 1500:
        desconto_inss = salario_bruto * 0.08
        
    elif salario_bruto > 3000:
        desconto_inss = salario_bruto * 0.09
    else:
        desconto_inss = salario_bruto * 0.11
        
    if vale_transporte == "s":
        desconto_VT = salario_bruto * 0.06
        
    if fez_horas_extras == "s":
        quant_horas_extras = int(input("Quantas horas extras? \n"))
        valor_hora_trabalhada = salario_bruto/horas_trabalhadas
        valor_hora_extra = valor_hora_trabalhada + (valor_hora_trabalhada * 0.5)
        valor_hora_extra = valor_hora_extra * quant_horas_extras
        
    salario_liquido = salario_bruto - desconto_VT - desconto_inss + valor_hora_extra
    
    print("Salário bruto R$ ", salario_bruto)
    print("Desconto INSS R$ ", desconto_inss)
    print("Desconto VT R$ ", desconto_VT)
    print("Valor das horas extras R$ ", valor_hora_extra)

    
else:
    print("Valores inválidos!")