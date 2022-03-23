#com o shuffle você embaralhará a ordem
from random import shuffle
aa = str(input('nome do aluno: '))
ab = str(input('nome do aluno: '))
ac = str(input('nome do aluno: '))
ad = str(input('nome do aluno: '))
list = [aa, ab, ac, ad]
ordem = shuffle(list)
print(list)