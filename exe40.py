nota_1 = float(input('Digite a nota da primeira prova: '))
nota_2 = float(input('Digite a nota da segunda prova: '))

m = (nota_1 + nota_2) / 2 

if m <= 5:
    print('REPROVADO')
elif m > 5 and m <= 6.9:
    print('RECUPERAÇÃO')
elif m >= 7:
    print('APROVADO')