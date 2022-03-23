maior = menor = c = 0
lista = []
c = 0
print('Caso deseje parar o programa, digite um número negativo')
while True:
    try:
        
        num = int(input('Digite um número: '))
        c += 1
        lista.append(num)            
        
        
        if c == 1:
            maior = num 
            menor = num 
        
        else:
            if num > maior:
                maior = num 
            if num < menor:
                menor = num 
            if num < 0:
                print(f'O maior número é: {maior} \nO menor número é: {menor}')
                print('--' * 20) 
                for pos, numb in enumerate(lista):
                    print(f'o número: {numb} está na posição: {pos} ')
                break
        
    except ValueError:
        print('Digite número, não letra.')



