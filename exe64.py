parada = False
soma = 0


while not parada: 
    num = int(input('Digite um número: '))
    soma += num
    parar = str(input('Digite 999 pra parar ou S pra continuar ')).upper()

    if parar == '999':
        parada = True
        print(soma)