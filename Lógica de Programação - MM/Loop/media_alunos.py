media_turma = 0
media = 0
contador = 1

while contador <= 5:
    notas = float(input(f"Informe a nota do Aluno {contador}:\n"))
    
    media += notas
    contador += 1
    
media_turma = media / 5

print("Média da turma: ", media_turma)

