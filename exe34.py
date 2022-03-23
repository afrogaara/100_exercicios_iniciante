s = float(input('Digite seu salário: '))
mau = s * (10 / 100) + s 
sau = s * (15 / 100) + s 
if s > 1250:
    print(f'seu novo aumento salarial é {mau}')
else:
    print(f'Seu novo aumento é {sau}')
