pontuacao = int(input("Informe a pontuação:"))
penalidade = int(input("Quantas penalidades o jogador teve?"))

if pontuacao >= 200:
    print("Classificado!")
elif pontuacao >= 100 and penalidade == 0:
    print("Classificado!")
else:
    print("Desclassificado.")
    
    