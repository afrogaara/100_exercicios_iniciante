dados = dict()

dados['nome'] = 'dhsauh'
dados['idade'] = 21
dados['sexo'] = 'M'

'''del dados['idade']'''

#print(f"O {dados['nome']} tem {dados['idade']} anos ")
for chave, valores in dados.items():
    print(f'{chave} ------ {valores}')
