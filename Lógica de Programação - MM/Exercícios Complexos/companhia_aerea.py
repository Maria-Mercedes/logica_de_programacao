#Destinos Fixos
passagem_RJ = 350
passagem_SAL = 650
passagem_REC = 800

#Informações Comprador
nome_passageiro = " "
destino_passageiro = 0
quant_passagens = 0
total_compra = 0
desconto = 0

while True:
    opcao_menu = int(input("""
          ---- Companhia Aérea ----
          1. Comprar passagem
          2. Encerrar
          """))
    
    if opcao_menu == 1:
        nome_passageiro = input("Informe o seu nome:\n")
        
        destino_passageiro = int(input("""
                                   ---- Selecione o destino: ----
                                   1. Rio de Janeiro - RJ: R$ 350,00
                                   2. Salvador - BA: R$ 650,00
                                   3. Recife - PE: R$ 800,00
                                   """))
        quant_passagens = int(input("Quantidade de Passagens:\n"))
        
        if quant_passagens <= 0:
            print("A quantidade não pode ser igual ou menor do que 0. Tente novamente.")
        else:
              
            if destino_passageiro == 1:
                total_compra += passagem_RJ * quant_passagens
                
                
            elif destino_passageiro == 2:
                total_compra += passagem_SAL * quant_passagens
                
                
            elif destino_passageiro == 3:
                total_compra += passagem_REC * quant_passagens
                
            else:
                print("Destino inválido. Tente novamente.")
                
                 
            if quant_passagens > 7:
                    desconto = total_compra * 0.15
            elif quant_passagens > 5:
                    desconto = total_compra * 0.1
            elif quant_passagens >= 3:
                    desconto = total_compra * 0.05
                    
            total_compra -= desconto

            print(f"""
                ---- Compra Realizada com Sucesso! ----
                Nome: {nome_passageiro}
                Destino: {destino_passageiro}
                Quantidade de Passagens: {quant_passagens}
                Desconto: R$ {desconto}
                Total: R$ {total_compra}
                """)
    
    elif opcao_menu == 2:
        print("Encerrando...")
        
        break
    
    else:
        print("Opção inválida. Tente novamente.")
        
