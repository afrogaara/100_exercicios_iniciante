from random import choice
lista = list() 
while True:
    lista.clear() 
    numero_alunos = int(input("Quantos alunos? "))    
    for c in range(0, numero_alunos):
        nome = input('Digite o nome dos alunos?: ')
        lista.append(nome)
    escolhido = choice(lista)       
    print(f"O escolhido foi: {escolhido}")
        
