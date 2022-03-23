print('-------------------------')
print('Vamos jogar par ou impar?')
print('-------------------------')

from random import randint
s = 0 
#Escolha um número

while True:
    computador = randint(0, 10)
    num = int(input('Digite um número: '))
    p_i = str(input('Escolha P/I: ')).upper()[0]
    
    #soma
    s = num + computador
    
    #condicionais 
    if s % 2 == 0 and p_i == 'P':
        print(f'Você venceu \nComputador joga o número {computador}')
        print('--' * 30)
    elif s % 2 != 0 and p_i== 'I':
        print(f'Você venceu\nComputador joga o número {computador}')
        print('--' * 30)
    else:    
        print(f'Você perdeu \nO computador joga o número {computador}')
        print('--' * 30 )
        break
