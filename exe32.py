d = int(input('Digite um ano qualquer: '))
c = d % 4 
if c == 0:
    print(f'{d} é um ano bissexto') 
else:
    print(f'{d} não é um ano bissexto') 
