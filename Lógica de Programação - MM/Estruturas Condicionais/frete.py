"""
Uma loja virtual calcula o frete de acordo com o valor da compra 
e a região de entrega.
Para compras abaixo de R$ 200, o frete custa R$ 10 para a região Sudeste 
e R$ 20 para as demais regiões. 

Calcule e exiba o valor do frete e o total da compra.
"""

valor_compra = float(input("Valor da compra:"))
regiao_entrega = input("Região de Entrega:")

if valor_compra >= 200:
    print("Parabéns! Frete grátis!")
else:
    if regiao_entrega == "Sudeste":
        print("Frete: R$10,00")
        
    else:
        print("Frete: R$20,00")
        


    
    