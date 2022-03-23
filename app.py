#salvar pra aperfeiçoar depois 
print('Quando você nasceu?')
dia = int(input('digite o dia: '))
m = int(input('digite o mês: '))
ano = int(input('digite o ano: '))
if dia > 31: 
    int(input('por favor, digite o dia válido de nascimento: '))
if m > 12: 
    int(input('por favor digite um mês de nascimento válido: '))
print('você nasceu no dia', dia)
print('do mês', m)
print('do ano', ano)
    

