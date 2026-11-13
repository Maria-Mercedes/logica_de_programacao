"""
Para 5 alunos, peça 2 notas, calcule a média e 
Mostre “Aprovado” (>= 6) ou “Reprovado”
Ao final, mostre quantos foram aprovados.
"""

nota1 = 0
nota2 = 0
media_aluno = 0
quant_aprovados = 0

for contador in range(1,6):
    print("------- Média dos Alunos -------")
    
    nota1 = float(input(f"Informe a 1° Nota do Aluno {contador} :\n"))
    nota2 = float(input(f"Informe a 2° Nota do Aluno {contador}\n"))
    
    media = (nota1 + nota2) / 2
    
    if media >= 6:
        print("Aprovado!")
        quant_aprovados += 1
        
    else:
        print("Reprovado.")
        
print(quant_aprovados, "foram Aprovados!")
