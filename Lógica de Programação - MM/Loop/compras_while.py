total_compra = 0
valor_feijao = 10.5
valor_arroz = 17
valor_macarrao = 2

produto = input("Qual é o produto?")

while produto != "Encerrar":
    if produto == "Feijão":
        total_compra += valor_feijao
    elif produto == "Arroz":
        total_compra += valor_arroz
    elif produto == "Macarrão":
        total_compra += valor_macarrao
        
    produto = input("Qual é o produto?")
    
print("Total: R$", total_compra)

