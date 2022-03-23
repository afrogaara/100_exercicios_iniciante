from random import choice

lista = ['pedra', 'papel', 'tesoura']

aleatorio = choice(lista)

print('1) pedra \n2) papel \n3) tesoura')

j = int(input('Escolha um número: '))

if j == 1 and aleatorio == 'papel':
    print(f'você perdeu.\nO computador escolheu {aleatorio}')
elif j == 2 and aleatorio == 'tesoura':
    print(f'você perdeu.\nO computador escolheu {aleatorio}')
elif j == 3 and aleatorio == 'pedra':
    print(f'você perdeu.\nO computador escolheu {aleatorio}')
elif j == aleatorio:
    print('EMPATE')
else:
    print(f'Você ganhou \nO computador escolheu {aleatorio} :)')