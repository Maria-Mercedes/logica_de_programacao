# Valores Destinos
passagem_RJ = 350
passagem_SAL = 650
passagem_REC = 800

# Informações de Compra
nome_passageiro = " "
destino_desejado = " "
quant_passagens = 0

# Compra
total_compra = 0
desconto = 0

#Início do Loop
while True:
    opcao_menu = int(input("""
                           ---- Companhia Aérea ----
                           1. Comprar passagens
                           2. Encerrar
                           """))
    
    #Se escolher Comprar passagens:
    if opcao_menu == 1:
        nome_passageiro = input("Informe o seu nome:\n")
        
        destino_desejado = int(input("""
                                     ---- Destinos Disponíveis ----
                                     1. Rio de Janeiro - RJ: R$ 350,00
                                     2. Salvador - BA: R$ 650,00
                                     3. Recife - PE: R$ 800,00
                                     """))
        
        quant_passagens = int(input("Quantidade de Passagens:\n"))
        
        #Verificação para não haver passagens 0 ou negativas
        if quant_passagens <= 0:
            print("Você precisa comprar pelo menos 1 passagem. Tente novamente.")
        #Caso ele informe uma quantidade válida:
        else:
            #Se escolher RJ
            if destino_desejado == 1:
                total_compra += passagem_RJ * quant_passagens
            #Se escolher Salvador
            elif destino_desejado == 2:
                total_compra += passagem_SAL * quant_passagens
            #Se escolher Recife
            elif destino_desejado == 3:
                total_compra += passagem_REC * quant_passagens
            #Se informar um valor errado
            else:
                print("Destino inválido. Tente novamente.")
        
        #Cálculo Desconto
        if quant_passagens > 7:
            desconto = total_compra * 0.15
        elif quant_passagens >= 5:
            desconto = total_compra * 0.1
        elif quant_passagens >= 3:
            desconto = total_compra * 0.05
            
        #Total da compra - desconto já calculado
        total_compra -= desconto
        
        #Encerramos a compra
        print(f"""
              ---- Resumo da Compra ----
              Nome: {nome_passageiro}
              Destino: {destino_desejado}
              Quantidade de Passagens: {quant_passagens}
              Desconto: R$ {desconto}
              Total: R$ {total_compra}
              """)
        
        #Para realizar uma nova compra, setamos como 0 para não somar o valor de uma compra em outra.
        #Opcional
        total_compra = 0
        
    #Caso o usuário escolha encerrar:
    elif opcao_menu == 2:
        print("Encerrando...")
        break
    #Caso o usuário informe uma opção inexistente no menu 
    else:
        print("Opção incorreta. Tente novamente")
