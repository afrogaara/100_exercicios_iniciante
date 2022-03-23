v = int(input('Digite a distancia da viagem em km: '))
p_u = int(v * 0.50)
p_d = int(v * 0.45)
if v <= 200:
    print(f'O valor a ser pago é {p_u}')
else:
    print(f'O valor a ser pago é {p_d}')
