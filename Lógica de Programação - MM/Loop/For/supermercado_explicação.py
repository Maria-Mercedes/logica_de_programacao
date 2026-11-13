"""
 Peça o valor pago e calcule o troco, 
 avisando se o valor for insuficiente.
"""


quant_produtos = int(input("QTD Produtos:\n"))

total_compra = 0
desconto = 0
pgto = 0
troco = 0

#Calcular o total da compra
for contador in range(quant_produtos):
    preco_produto = float(input("Preço produto:\n"))
    quant_comprada = int(input("Quantidade:\n"))
    
    total_produto = preco_produto*quant_comprada
    
    total_compra += total_produto
    
#Calculando desconto
if total_compra > 500:
    desconto = total_compra * 0.1
    print("Valor desconto: R$", desconto)
elif total_compra > 200:
    desconto = total_compra * 0.05
    print("Valor desconto: R$", desconto)
    
total_compra -= desconto

print("Total: R$", total_compra)

#Pagamento   
while True:
    pgto = float(input("Valor Pgto:"))
    
    if pgto < total_compra:
        print("Valor insuficiente. Tente novamente.")
    else: 
        troco = pgto - total_compra
        
        if troco <= 0:
            print("Pagamento realizado com sucesso. Não há troco para essa compra.")
        else:
            print("Pagamento realizado com sucesso.\n Valor do troco: R$", troco)

        break