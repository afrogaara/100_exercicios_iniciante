lista = list()
dicionario = dict()

while True:
    try:
        dicionario['nome'] = str(input('Digite o nome do aluno: '))
        dicionario['nota 1:'] = float(input('Digite a primeira nota do aluno: '))
        dicionario['nota 2:'] = float(input('Digite a segunda nota do aluno: '))
        #media
        dicionario['media:'] = (dicionario['nota 1:'] + dicionario['nota 2:']) / 2

        lista.append(dicionario.copy())
        if dicionario['media:'] < 5:
            print(f'Este aluno está reprovado com media {dicionario["media:"]}')
        elif dicionario['media:'] >= 5:
            print(f'Este aluno está aprovado com media {dicionario["media:"]}')

        print('Deseja adicionar mais algum aluno?\n[S/N]')
        opc = str.upper(input(': '))[0]
        if opc == 'S':
            continue
        if opc == 'N' or opc != 'SN':
            break

    except ValueError:
        print('Digite apenas números')
    except:
        print('Algum erro ocorreu')


for c in (lista):
    for chave, valor in c.items():
        print(f'{chave} {valor}', end='\n')
    print('--'*25)

