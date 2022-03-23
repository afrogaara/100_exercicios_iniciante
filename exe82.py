lista = [] 
pares = [] 
impares = [] 

while True: 
    num = int(input('Digite um número: '))
    parada = str(input('Deseja continuar adicionando valores?\nS/N: ')).upper()

    if num:
        lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    if num % 2 == 1:
        impares.append(num)
    if parada == 'N':
        print('--' * 25)
        print(f'todos: {lista} \npares: {pares} \nimpares: {impares} ')
        break
    