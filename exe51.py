#ele quer que mostre os 10 primeiros termos 
# n = 10 

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

c = primeiro + (10 - 1) * razao

for c in range(0, c, razao): #c é um número 
    print(c)