dados = list()
lista = list()

while True:

    nome = str(input('Digite o nome do aluno: '))
    num1 = float(input('Digite a primeira nota: '))
    num2 = float(input('Digite a segunda nota: '))
    media = (num1 + num2) / 2
    parada = str.upper(input('Deseja adicionar mais alunos?\n[S/N]: '))


    dados.append(nome)
    dados.append(num1)
    dados.append(num2)
    dados.append(media)
    lista.append(dados[:])
    dados.clear() #voltar na parte do video em curso em video que fala sobre esse comando

    if parada == 'N':
        for c in lista:
            print(f'Nome do aluno: {c[0]} ------------ media :{c[3]}')
        break
while True:
    print('O que gostaria de fazer?'
          '1) ver a nota individual de cada aluno: '
          '2) ver apenas a media:')
    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        for nota in lista:
            print(f'nome do aluno: {nota[0]}\nprimeira: {nota[1]}\nsegunda nota: {nota[2]} ')

