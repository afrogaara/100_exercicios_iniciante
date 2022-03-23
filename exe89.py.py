dados = []
media = []
lista = list()
while True:
    
    n = input('Digite seu nome: ')
    num1 = int(input('Digite a sua primeira nota aluno: '))
    num2 = int(input('Digite a segunda nota dod aluno: '))
    parada = str(input('Deseja adicionar mais algum aluno?\n[S/N] ')).upper()
    calculo = (num1 + num2) / 2 
    
    #guardando informações nas listas
    dados.append(n)
    dados.append(num1)
    dados.append(num2)
    dados.append(calculo)
    
    
    if parada == 'N':
        break

while True:
    print('O que deseja fazer?')
    print('DIGITTE 1 para ver notas e as medias de cada aluno')
    print('DIGITE 2 para ver apenas as notas')
    print('DIGITE 3 para ver apenas as medias')
            
    opc = input('Digite a opção escolhida: ')
    
    if opc == 1:
        print(f'{c} ------------- primeira nota: {c+1} segunda nota: {c+2} media: {c+3}')
    elif opc == 2:
        print(f'{c} ------------------ primeira nota: {c+1} segunda nota: {c+2}')
    elif opc == 3:
        print(f'{c+3}')
    
    