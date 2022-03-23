from datetime import date
data = date.today()
ano = data.year

dicionario = dict()
lista = list()
while True:
    dicionario['nome'] = str(input('Digite seu nome: '))
    dicionario['ano de nascimento'] = int(input('Digite APENAS o ano de nascimento: '))
    dicionario['idade'] = ano - dicionario['ano de nascimento']
    dicionario['carteira'] = int(input('Carteira de trabalho? (0 não etem): '))


    if dicionario['carteira'] != 0:
        dicionario['salario'] = int(input('Digite seu salário: '))
        dicionario['contratacao'] = int(input('Digite um ano de contratação: '))
        dicionario['aposentadoria'] = dicionario['contratacao'] + 35
    lista.append(dicionario.copy())
    parada = str.upper((input('Deseja sair?\n[S/N]: ')))


    if parada == 'S':
        break

for c in lista:
    for chave, valor in c.items():
        print(f'{chave}: {valor}')