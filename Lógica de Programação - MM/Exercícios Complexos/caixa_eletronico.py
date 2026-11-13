#Declaração de variáveis de saldo e saque.
saldo_cliente = 1500
valor_saque = int(input("Qual valor deseja sacar?"))

notas_100 = valor_saque // 100
print("Qtd Notas R$100: ", notas_100)
valor_restante = valor_saque % 100 


notas_50 = valor_restante // 50
print("Qtd Notas R$50: ", notas_50)
valor_restante = valor_restante % 50


notas_20 = valor_restante // 20
print("Qtd Notas R$20: ", notas_20)
valor_restante = valor_restante % 20


notas_10 = valor_restante // 10
print("Qtd Notas R$10: ", notas_10)
valor_restante = valor_restante % 10


notas_5 = valor_restante // 5
print("Qtd Notas R$5: ", notas_5)
valor_restante = valor_restante % 5



notas_2 = valor_restante // 2
print("Qtd Notas R$2: ", notas_2)




