media = []
hsexo = []
midade = []
maior = 0 

for c in range(0, 4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str((input('H ou F: ')))
    
    #média de idade do grupo 
    media.append(idade)
    soma = sum(media)
    c =  soma / 4
    
    #qual é o nome do homem mais velho
    if c == 1:
        maior = idade

    else: 
        if idade > maior: 
            maior = idade
            hsexo = nome 
        
    #quantas mulheres tem menos de 20 anos 
    if 'fF' in sexo and sexo < 20: 
        midade.append(idade)
        
print(f'A media da idade do grupo é {c}')
print(f'{len(midade)} mulheres tem menos de 20 anos')
print(f'O homem mais velho é {hsexo} e tem {maior} de idade')







