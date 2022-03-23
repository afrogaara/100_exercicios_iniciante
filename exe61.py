#ele quer que mostre os 10 primeiros termos 
# n = 10 

parada = False

while not parada:
    
    primeiro = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a razão da PA: '))
    
    c = primeiro + (10 - 1) * razao
    print(c)
    sn = str(input('Deseja continuar? S/N: ')).upper()
    
    if sn == 'N':
        parada = True
        print('Volte sempre')
    