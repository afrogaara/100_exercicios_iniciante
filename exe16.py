#modulos
#import x ( importará tudo da biblioteca )
#from (biblioteca) import ( item da biblioteca )
#random.random // random.randint
from math import trunc
num = float(input('Digite um número: '))
r = trunc(num)
print(f'A porção inteira do número {num} é: {r}')