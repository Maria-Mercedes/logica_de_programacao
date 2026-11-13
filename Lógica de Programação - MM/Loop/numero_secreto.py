""" 
Enquanto errar, informe se o palpite foi maior ou menor que o número secreto. 
Ao acertar, exiba uma mensagem de parabéns e a quantidade de tentativas.

"""

numero_secreto = 1234
tentativas = 0

palpite = int(input("Tente adivinhar:"))

while palpite != numero_secreto:
    if palpite > numero_secreto:
        print("Seu palpite foi maior do que o número secreto. Tente novamente!")
    else:
        print("Seu palpite foi menor do que o número secreto. Tente novamente!")
        
    tentativas += 1
    
    palpite = int(input("Tente adivinhar:"))

tentativas += 1    
print("Parabéns! Você acertou o número secreto!!!")
print("Sua quantidade de tentativas foi de: ", tentativas)


