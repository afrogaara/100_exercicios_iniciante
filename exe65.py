# parada = False ( condição de parada não usando o while True)
from decimal import DivisionByZero

contagem = 0 
soma = 0
maior = 0 
menor = 0

while True:

    print('--' * 30 )
    try:
        num = int(input('Digite um número: '))
        print('Digite 999 caso queira encerrar o programa: ')
    
        
        if num == 999:
            print(f'O maior número é {maior}') 
            print(f'O menor número é {menor}')
            print(f'a media entre todos os números digitados é: {media}\nA soma entre todos os números é: {soma}')
            print(f'Você digitou {contagem} valores')
            break
        #soma
        soma += num
        #contagem
        contagem += 1 
        #media
        media = soma / contagem
        #maior e o menor
    
        if contagem == 1: 
            maior = num 
            menor = num
        else:
            if num > maior:
                maior = num
             
            if num < menor: 
                menor = num
            
            if maior == menor:
                print('Ambos são iguais')
    except ValueError: # acontece quando você digita letras ao inves de números 
        print('Digite um número, não letra.')
  