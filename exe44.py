p = float(input('Digite o preço do produto: '))

print('As formas de pagamento são: \n1) dinheiro/cheque: 10% desconto')
print('2) A vista no cartão: 5% de desconto \n3) 3x ou mais no cartão: 20% de desconto')

e_1 =  p - (p * (10/100)) 
e_2 =  p - (p * (5/100))  
e_3 =  p - (p * (20/100)) 

opção = int(input('Digite a opção escolhida: '))

if opção == 1:
    print(f'Você paragará com o desconto um total de {e_1}')
elif opção == 2:
    print(f'Você pagará com o desconto um total de {e_2}')
elif opção == 3:
    print(f'Você pagará com o desconto um total de {e_3}')

