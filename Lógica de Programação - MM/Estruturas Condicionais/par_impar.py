"""
Solicite um número inteiro e verifique se ele é par ou ímpar. 
Se for divisível por 2, exiba "O número é par". 
Caso contrário, exiba "O número é ímpar".
"""

num_inteiro = int(input("Informe um n° inteiro:"))

#Se for divisível, o resto tem que ser 0
if num_inteiro % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

