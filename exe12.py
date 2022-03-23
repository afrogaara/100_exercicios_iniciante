d = int(input('Digite o desconto do cupom em %: '))
p = float(input('Digite o valor do produto comprado: '))
c = p * (d/100)
v = p - c 
print(f'Seu desconto em $Reais é {c}, você pagará {v}Reais')