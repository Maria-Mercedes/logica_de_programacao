"""
notas = [10, 5, 9, 7, 8, 6, 10] 

pos_1 = int(input())
pos_2 = int(input())

variavel_aux = notas[pos_1]

notas[pos_1] = notas[pos_2]
notas[pos_2] = variavel_aux

print(notas)
"""






nomes = ['Maria', 'Weverton']

if 'Luana' in nomes:
    nomes.remove('Luana')
    print('Existe o nome Luana!')
else:
    print('Não existe Luana na lista')