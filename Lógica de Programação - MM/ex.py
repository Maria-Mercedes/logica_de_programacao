"""
Crie uma lista com seis notas. 
Percorra a lista e conte quantos alunos foram aprovados,
considerando a média mínima 7.
"""

notas = [10, 5, 7, 6, 4.5]
aprovados = 0
reprovados = 0

for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
        
print(f"{aprovados} alunos foram aprovados!")
print(f"{reprovados} alunos foram reprovados")