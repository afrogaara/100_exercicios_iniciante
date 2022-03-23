from random import randint

tupla = ()
maior = menor = []
contagem = 0

while True:
    aleatorio = randint(0, 5)
    tupla = (aleatorio)
    contagem += 1
    
    print(f'Os números gerados foram {tupla}', end='\n') 
    
    if contagem == 1:
        maior = tupla
        menor = tupla
    else: 
        if tupla > maior:
            maior = tupla
        if tupla < menor:
            menor = tupla
    
    if contagem == 5:
        
        print(f'o maior número foi {maior}')
        print(f'o menor número gerado foi o {menor}')
        break



