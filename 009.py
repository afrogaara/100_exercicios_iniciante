from time import sleep
from random import randint
from operator import itemgetter
lista = list()


dicionario = {'jogador 1': randint(0, 6),
              'jogador 2': randint(0, 6),
              'jogador 3': randint(0, 6),
              'jogador 4': randint(0, 6)}
lista.append(dicionario.copy())

for c in lista:
    for chave, valor in c.items():
        print(f'{chave} -- {valor}')
        sleep(0.8)
#colocar dicionário na ordem
ordem = list()
ordem = sorted(dicionario.items(), key=itemgetter(1), reverse=True) #0 é chave. 1 é o valor #sorted ele tá ordenando os valores
                                                               # do menor para o maior
for pos, numero in enumerate(ordem):
    print(f'posição: {pos} {numero[0]}--{numero[0+1]}')
