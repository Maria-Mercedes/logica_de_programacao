"""
Solicite o nome e a idade de uma pessoa. 
Exiba uma mensagem informando quantos anos ela terá no próximo ano.
"""

nome = input("Qual é o seu nome?\n")
idade = int(input("Quantos anos você tem?\n"))

idade += 1

print(f"{nome}, você terá {idade} anos no próximo ano")

