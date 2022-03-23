from time import sleep
lista = list()
dados = list()
maior = menor = c = 0 
maior_p = menor_p = [] 


while True:
    #dados
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    sleep(0.5)
    #quantas pessoas foram registradas
    
    #guardando informações 
    dados.append(nome)
    dados.append(idade)
    dados.append(peso)
    dados.append(lista[:])
    c += 1
    print('infomações guardadas com sucesso')
    #condição de parada
    if c == 1: 
        maior = peso 
        menor = peso 
    
    else: 
        if peso > maior: 
            maior = peso 
            maior_p.append(nome)       
        if peso < menor: 
            menor = peso 
            menor_p.append(nome)


    p = str(input('Deseja continuar salvando?\nS/N: ')).upper()
    if p == 'N':
        break
        
print(f'foram registradas: {c}')
print(f'A pessoa mais pesada é:\n{maior_p} com {maior} kg')
print(f'A pessoa mais leve é:\n{menor_p} com {menor} kg')
    
        
        
    
 