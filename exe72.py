n = ('zero um dois três quatro cinco seis sete oito nove dez').split()

while True:
    print('Digite um número negativo caso deseje sair do programa')
    print('---' * 50)
    num = int(input('Digite um número de 1 a 10: '))
    escolha = n[num]
    
    print(f'você escolheu o número: {escolha}')    
    
    if num > 10:
        print('Se desejar sair, digite um numero negativo')
        print('Número inválido, tente novamente')
    
    if num == -1:
        break


