#aprimorar depois 
from time import sleep
from random import randint, random
import numpy as np

lista = sorteio = list()



while True:
    
    print('Digite a quantidade de jogos que você gostaria fazer')
    print('=-'*25)
            
    num = int(input(': '))
    stop = str(input('Você gostaria de parar?\nS/N: ')).upper()
    sorteados = np.random.randint(0, 60, (num,6))

    #guardando valores em uma lista
    sorteio.append(sorteados[:])
    lista.append(sorteio[:])
    print(sorteados)
    
    if stop == 'N':
        for cada in lista:
            print(cada)
        continue
    elif stop != 'S' and stop != 'N':
        print('inválido')
    elif stop == 'S':
        break


            