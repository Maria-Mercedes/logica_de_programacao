saldo_cliente = 1500
valor_saque = int(input("Qual valor deseja sacar?"))

if valor_saque <= 0:
    print("Valor inválido!")
elif valor_saque > saldo_cliente:
    print("Saldo insuficiente!") 
else:
    notas_100 = valor_saque // 100
    valor_restante = valor_saque % 100
    print("Valor saque: ", valor_restante)

    notas_50 = valor_restante // 50
    valor_restante = valor_restante % 50
    print("Valor saque: ", valor_restante)

    notas_20 = valor_restante // 20
    valor_restante = valor_restante % 20
    print("Valor saque: ", valor_restante)

    notas_10 = valor_restante // 10
    valor_restante = valor_restante % 10
    print("Valor saque: ", valor_restante)

    notas_5 = valor_restante // 5
    valor_restante = valor_restante % 5
    print("Valor saque: ", valor_restante)

    notas_2 = valor_restante // 2
    valor_restante = valor_restante % 2
    print("Valor saque: ", valor_restante)

    print("Notas R$100: ", notas_100)
    print("Notas R$50: ", notas_50)
    print("Notas R$20: ", notas_20)
    print("Notas R$10: ", notas_10)
    print("Notas R$5: ", notas_5)
    print("Notas R$2: ", notas_2)
    
        



