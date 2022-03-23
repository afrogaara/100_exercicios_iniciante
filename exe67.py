while True:
    
    num = int(input('Digite um valor para ver a tabuada: '))
    
    #condição parada 
    if num < 0:
        print('Programa encerrado')
        break
    
    
    #tabuada 
    for c in range(0, 10+1):
        r = c * num
        print(f'{c} x {num} == {r} ')