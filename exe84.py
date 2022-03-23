lista = list()
dados = list() 
maior = menor = c = 0
maior_peso = menor_peso = []

while True:
   
  
        nome = str(input('Digite seu nome: '))
        idade = int(input('Digite sua idade: '))
        peso = float(input('Digite seu peso: '))
            
        dados.append(nome)
        dados.append(idade)
        dados.append(peso)
        lista.append(dados[:])
        c += 1 # contagem de pessoas

        if c == 1: 
            maior = peso 
            menor = peso

        else: 
            if peso > maior:
                maior = peso 
                maior_peso.append(nome)
            if peso < menor: 
                menor = peso
                menor_peso.append(nome)
        
        for c in lista:
            print(f'Fora cadastradas: {c} pessoas')
            print(f'as pessoas mais pesadas registradas:\n{maior_peso} com {maior} kg')
            print(f'as pessoas mais leves registrada é:\n{menor_peso} com {menor} kg')
    
    
    
    