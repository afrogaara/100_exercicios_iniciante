lista = list()
dicionario = dict()
gols = list()

dicionario['nome'] = str(input("Digite o nome do jogador: "))
dicionario['partidas'] = int(input("Quantas partidas jogadas?: "))

for c in range(1, dicionario['partidas']+1):
    gols.append(int(input(f'Gols na partida: {c}: ')))


lista.append(dicionario.copy())


for valor in lista:
    for chave, valor in valor.items():
        print(f"{chave}: {valor}")
for pos, n in enumerate(gols): 
    print(f"foram feitos {n} gols na partida {pos+1}")


