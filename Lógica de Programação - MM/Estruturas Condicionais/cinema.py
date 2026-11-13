ingresso = 30
desconto = 0

idade = int(input("Quantos anos você tem?"))
estudante = input("É estudante? (s/n)")

#Pessoas com 60 anos ou mais recebem 50% de desconto.
if idade >= 60:
    desconto = ingresso * 0.5
#Estudantes com menos de 60 anos recebem 30% de desconto
elif idade < 60 and estudante == "s":
    desconto = ingresso * 0.3
else:
    desconto = 0
    
ingresso_final = ingresso - desconto
print("Valor ingresso: R$", ingresso)
print("Valor desconto: R$", desconto)
print("Valor final: R$", ingresso_final)
    

