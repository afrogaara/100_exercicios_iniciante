# tudo dentro do dicionário é um valor atribuido a ele
#chaves são titulo, ano, diretor e ator. que vão receber valores ( é como se fossem posições )
#keys mostrará apenas aos valores dados as chaves
#items ele vai mostrar a chave ( é muito importante )
#values() mostrará tudo que foi atribuido ao dicionário

dados = {'titulo:': 'O contador de historias',
         'ano:': 2012,
         'diretor:': 'Luiz Vilaça',
         'ator:': 'Roberto Carlos Ramos',
         }
'''print(dados.values())
print(dados.keys())
print(dados.items())'''

for p, c in dados.items(): # items mostrará tanto a chave quanto o valro atribuido a ela
    print(f'{p} {c} ')
