#gosto desse jeito de fazer
lista = list()
dados = list()


while True:

    nome = str(input('Digite um nome: '))
    idade = int(input('Digite sua idade: '))

    dados.append(nome)
    dados.append(idade)
    lista.append(dados[:])
    dados.clear() #você faz uma copia dos dados pra lista e depois exclui o conteudo de dados
                  #para não ser repetido

    for c in lista:
        print(f'nome: {c[0]}\nidade: {c[1]}')
        print('--'*30)