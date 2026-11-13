#Caixa de supermercado: 
# Peça a quantidade de produtos e, para cada um, 
# o preço e a quantidade comprada.

quant_produtos = int(input("QTD Produtos:\n"))

total_compra = 0
desconto = 0

for contador in range(quant_produtos):
    preco_produto = float(input("Preço produto:\n"))
    quant_comprada = int(input("Quantidade:\n"))
    
    total_produto = preco_produto * quant_produtos
    
    total_compra += total_produto
    
if total_compra > 500:
    desconto = total_compra * 0.1
    print("Valor desconto: R$", desconto)
elif total_compra > 200:
    desconto = total_compra *0.05
    print("Valor desconto: R$", desconto)

total_compra -= desconto
print("Total: R$", total_compra)

while True:
    pgto = float(input("Quanto será pago?\n"))
    
    if pgto < total_compra:
        print("Pagamento insuficiente.")
    else:
        troco = pgto - total_compra
        
        if troco > 0:
            print("Pagamento realizado com sucesso!\nValor troco: R$", troco)
            break
        else:
            print("Pagamento realizado com sucesso!\nNão há troco para essa compra.")
            break
    
    
    


