lista = list()
pares = list()
impares = list()

for c in range(0, 7):
    num = int(input('Digite um número: '))

    if num % 2 == 0: 
        pares.append(num)
        
     
    if num % 2 == 1: 
        impares.append(num)
       
#salvando coisas nas listas 
lista.append(pares[:])
lista.append(impares[:])

print(f'os valores pares são:\n{sorted(lista[0])}')
print(f'os valores impares são:\n{sorted(lista[1])}')