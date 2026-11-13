"""
Solicite ao usuário um número inteiro 
e mostre a tabuada desse número de 1 a 10.

"""

numero = int(input())

contador = 0

while contador <= 10:
    print(numero*contador)
    
    contador += 1
    