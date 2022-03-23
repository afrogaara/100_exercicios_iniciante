#tento encontrar depois uma resolução pra isso
lista = [] 

maior = menor = c = 0 

while True: 
    num = int(input('Digite um número: '))
    c += 1 

    if c == 1:
        maior = num
        menor = num
    
    else: 
        
            if num > maior:
                maior = num
                lista.append(maior[-1])
           
            if num < menor:
                menor = num
                lista.append(menor[0])

         