#não se pode usar o choice diretamente na lista, tem que criar uma outra variavel e usar o choice 
# errado > ale = choice[aa, ab, ac, ad] 
# certo > ale = [aa, ab, ac, ad]\nescolhido = choice(ale)
from random import choice
aa = str(input('nome do aluno: '))
ab = str(input('nome do aluno: '))
ac = str(input('nome do aluno: '))
ad = str(input('nome do aluno: '))
ale = [aa, ab, ac, ad]
escolhido = choice(ale)
print(f'O escolhido foi {escolhido}')
