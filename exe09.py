lista = list()
dicionario = dict()
gols = list()

dicionario['nome'] = str(input("Digite o nome do jogador: "))
dicionario['partidas'] = int(input("Quantas partidas jogadas?: "))

for c in range(1, dicionario['partidas']+1):
    print('Quantos gols foram feitos na partida: ?')
    gols.append(int(input(f'{c}: ')))


lista.append(dicionario.copy())


for valor in lista:
    for chave, valor in valor.items():
        print(f"{chave}: {valor}")
print(f'gols: {gols}')




