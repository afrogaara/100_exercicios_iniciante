#LEMBRAR DE MELHORAR ESSE CÓDIGO. FUNCIONA ? FUNCIONA. Muita gambiarra. 
tuplas = ()
contagem = 0 
n_pares = []
nove = [] 
add =  []

while True:
    
    num = int(input('Digite um número: '))
    add.append(num)
    contagem += 1
    tuplas = (add)
    
    if num < 0:
        print('número inválido, digite novamente: ')

    if num % 2 == 0:
        n_pares.append(num)
    
    if num == 9:
        nove.append(num)
    
    if contagem == 4: 
        print(f'os números pares são: {n_pares}')
        print(f'Você digitou os valores {tuplas}')
        print(f'O número 9 aparece {len(nove)} vezes')
        if 3 not in tuplas: 
            print('o número 3 não foi digitado')
        else:  
            print(f'O número 3 aparece na posição {tuplas.index(3)}')
        break 

  