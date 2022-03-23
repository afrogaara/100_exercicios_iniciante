lista = []


while True:
    try:
        num = int(input('Digite um número: '))
        lista.append(num)
        
        parada = str(input('Deseja adicionar mais números?\nS/N: ')).upper()
        lista.sort(reverse=True)
        
        if parada == 'S':
            continue
        
        if parada == 'N':
            print(f'você digitou {len(lista)} números ')
            print(f'o número 5 aparece {lista.count(5)} vezes')
            print(f'os números na ordem decrescente são {lista}')
        
    except ValueError:
        print('Digite apenas números')
    except:
        print('Algum erro ocorreu')