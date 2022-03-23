c = str(input('Digite o nome da sua cidade: '))
palavra = 'SANTOS' 
f = c.upper() 
s = f.split()
p = s[0]
if palavra in p:
    print(f'Sua cidade começa com a palavra {palavra}')
else:
    print(f'Sua cidade não começa com {palavra}')
    