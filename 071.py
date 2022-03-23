total = caros = nome_barato = [] # armazenando o total das compras, mais caro, e o nome do mais barato 
barato = contagem = 0 #armazenando o menor valor dos produtos digitados e a contagem 

while True:
    
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    contagem  += 1
    parada = str(input('Deseja continuar? S/N: ')).upper()[0]

    #armazenar preco
    total.append(preco)
    soma = sum(total)

    #menor 
    primeiro = preco 
    
    
    #condicionais 
    if preco > 1000:
        caros.append(preco)

    if contagem == 1:
        barato = preco 

    if  preco < barato:
        barato = preco
        nome_barato.append(nome)
    
    if parada == 'N':
        break

print(f'O total de gasto na compra é {soma} ')
print(f'São {len(caros)} os produtos que custam mais de 1000$')
print(f'O produto mais barato é a {nome_barato} e custa: {barato}')
