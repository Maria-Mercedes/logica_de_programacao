"""
Exiba um menu com as opções consultar saldo, depositar, sacar e sair. 
O programa deve continuar executando até que o usuário escolha sair. 
Não permita saques maiores que o saldo disponível nem depósitos negativos.
"""

saldo = 1000
valor_deposito = 0
valor_saque = 0
opcao = " "

contador = 0
while contador == 0:
    opcao = int(input("""
          ------- Menu-------
          1. Consultar saldo
          2. Depositar
          3. Sacar
          4. Sair
          --------------------
          """))
    
    if opcao == 1:
        print("Seu saldo é de: R$ ", saldo)
        
    elif opcao == 2:
        valor_deposito = int(input("Quanto deseja depositar?\n"))
        
        if valor_deposito <= 0:
            print("Não é possível depositar valores negativos ou zerados.")
            valor_deposito = 0
        else:
            print(f"""
                    Operação concluída com sucesso!
                    Saldo inicial: R$ {saldo}
                    Valor do depósito: R$ {valor_deposito}
                    """)
            
            saldo += valor_deposito
            print("Saldo final: R$ ", saldo)
        
    elif opcao == 3:
        valor_saque = int(input("Quanto deseja sacar?\n"))
        
        if valor_saque > saldo:
            print("Saldo insuficiente para saques nesse valor.")
            valor_saque = 0
            
        elif valor_saque <= 0:
            print("Não é possível sacar valores negativos ou zerados. Tente novamente.")
            valor_saque = 0
            
        else:
            print(f"""
                  Operação concluída com sucesso!
                  Saldo inicial: R$ {saldo}
                  Valor do saque: R$ {valor_saque}
                  """)
            
            saldo -= valor_saque
            
            print("Saldo final: R$ ", saldo)
        
    elif opcao == 4:
        print("Encerrando")
        contador += 1
        break
