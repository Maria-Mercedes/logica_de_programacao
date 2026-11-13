senha = 1234

digitado = int(input())

while digitado != senha:
    print("Acesso negado. Tente novamente!")
    
    digitado = int(input())
    
print("Acesso permitido!")


contador = 0

while contador == 0:
    senha_digitada = input()
    
    if senha_digitada == "maria123":
        print("Acesso permitido!")
        
        contador = 1
        break
    