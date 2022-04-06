#chaves armazenam informações chamadas de "valores" 
dados = {'titulo:': 'O contador de historias',
         'ano:': 2012,
         'diretor:': 'Luiz Vilaça',
         'ator:': 'Roberto Carlos Ramos',
         }
#print(dados.values())
#print(dados.keys())
#print(dados.items())

for p, c in dados.items(): # {p} chaves e {c} valores atribuidos 
    print(f'{p} {c} ')
