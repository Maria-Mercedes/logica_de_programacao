"""
Solicite uma nota entre 0 e 10 e exiba:
Nota fora do intervalo de 0 a 10: "Nota inválida".
Nota maior ou igual a 7: "Aprovado".
Nota maior ou igual a 5 e menor que 7: "Recuperação".
Nota menor que 5: "Reprovado".
"""

nota = float(input("Nota: \n"))

if nota>=0 and nota <= 10:
    if nota >= 7:
        print("Aprovado!")
    elif nota >= 5:
        print("Recuperação.")
    else:
        print("Reprovado.")    
else:
    print("Nota inválida. Informe entre 0 e 10.")
    
    