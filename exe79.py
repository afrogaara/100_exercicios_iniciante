#existem alguns erros nesse código. Corrigir depois 
from time import sleep

lista = []

while True:
    try:
        num = int(input('Digite um número: '))
        parada = str(input('Deseja parar? S/N: ')).upper()
        
        
        #adicionar número a lista
        if num not in lista:
            print('adicionando número...')
            lista.append(num)
            sleep(1)
        
        
        #removendo número da lista
        else:
            print('removendo número da lista')
            lista.remove(num)
            sleep(1)
           
        #condição de parada
        
        if parada == 'S':
            print('Volte sempre')
            break
        
        for pos, c in enumerate(lista):
            print(f'o número {c} está na posição {pos}')

    except ValueError:
        print('Digite apenas números!')

print(f'Todos os números digitados foram {sorted(lista)}')
