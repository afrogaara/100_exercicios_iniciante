v = int(input('Qual a velocidade do carro? '))
if v > 80:
    m = (v - 80) * 7 
    print(f'Você vai ser multado!! \nCada km excedido custa $7Reais \nTotal a ser pago é: {m}')
else:
    print('Continue tendo cuidado no transito!')