from random import shuffle # embaralha a lista de forma "aleatoria" 
lista = [] 

while True: 
    aluno = input("Nome do aluno: ")
    lista.append(aluno)
    print(lista)
    while True:
        parada = str.upper((input("Deseja parar? [S/N]: ")))[0]
        if parada in "SN":
            break
        print("Digite uma opção válida") 
    if parada == "S":
        break
    else:
        continue 
shuffle(lista) #shuffle é utilizado sozinho.
print(lista)
