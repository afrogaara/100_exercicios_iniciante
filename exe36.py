emprestimo = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
divida = int(input('Quantos anos pretende pagar a casa ? '))

c = emprestimo / (divida * 12) 
t = (c * 100) / salario 

if t > 30:
    print(f'emprestimo negado, a prestação excede seu salário em {int(t)}%')
else:
    print(f'Você pode pagar comprar a casa :). prestação mensal {int(c)}')

