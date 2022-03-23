r = False

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite outro número: '))

s = (num_1 + num_2)
m = num_1 * num_2

print('O que você deseja fazer com esses números?')
print('\n1)SOMAR\n2)MULTIPLICAR\n3)MAIOR\n4)NOVOS NÚMEROS\n5)SAIR DO PROGRAMA')


while not r: # gostei muito desse método. 
    
    n = int(input('Opção escolhida é: '))
    
    if n == 1: 
        print(f'A soma é igual a {s}')
        
    elif n == 2:
        print(f'A multiplicação é igual a {m}')
    
    elif n == 3:
        if num_1 > num_2:
            print(f'{num_1} é o maior')
        if num_1 < num_2:
            print(f'{num_2} é o maior')
        if num_1 == num_2:
            print('São iguais')
    
    elif n == 4: 
        num_1 = int(input('Digite o numero novamente: '))
        num_2 = int(int(input('Digite outro número novamente: ')))
    
    if n == 5:
        print('Finalizando...')
        r = True

    