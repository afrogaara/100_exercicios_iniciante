lista = list()
linha1 = list()
linha2 = list()
linha3 = list()
pares = [] 
c = 0 

for p in range(0, 9):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        pares.append(num)
    c += 1 
    
    if c <= 3:
        linha1.append(num)
    elif c > 3 and c <= 6:
        linha2.append(num)
    elif c > 6 and c <= 9:
        linha3.append(num)

#salvando na lista
lista.append(linha1[:])
lista.append(linha2[:])
lista.append(linha3[:])

print(f'a soma de todos os valores pares digitados é {sum(pares)}')
print(f'{lista[0]}')
print(f'{lista[1]}, o maior valor dessa coluna é {max(lista[1])}')
print(f'{lista[2]}, a soma desses valores é {sum(lista[2])}')