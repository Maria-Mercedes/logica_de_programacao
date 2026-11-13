saldo = 1000
valor_deposito = 0
valor_saque = 0

i = 0
while i != 4:
    opcao = int(input("""
          ------ Menu ------
          1. Consultar saldo
          2. Depositar
          3. Sacar
          4. Sair
          ------------------
          """))
    
    if opcao == 1:
        print("Seu saldo é de R$: ", saldo)
    elif opcao == 2:
        valor_deposito = int(input("Quanto deseja depositar?"))
        if valor_deposito <= 0:
            print("Não é possível depositar um valor negativo ou zerado. Tente novamente.")
        else:
            print("Seu saldo era de R$ ", saldo)
            
            saldo += valor_deposito  
            print("Valor do depósito: R$ ", valor_deposito)
            print("Saldo atual: R$ ", saldo)
            
    elif opcao == 3:
        valor_saque = int(input("Quanto deseja sacar?"))
        if valor_saque > saldo:
            print("Saldo insuficiente. Tente novamente")
        elif valor_saque <= 0:
            print("Não é possível sacar um valor negativo ou zerado.")
        else:
            print("Seu saldo era de R$ ", saldo)
            saldo -= valor_saque
            
            print("Valor do saque: R$ ", valor_saque)
            print("Saldo atual: R$ ", saldo)
    elif opcao == 4:
        print("Encerrando")
        break
    
    else:
        print("Opção inválida! Tente novamente.")