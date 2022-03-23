from datetime import date 

data = date.today()
data = data.year

ano = int(input('ano de nascimento: '))

idade = data - ano
passou = idade - 18 
falta = 18 - idade

if idade < 17:
    print(f'Você ainda irá se alistar no exercito, falta {falta}') 
elif idade == 18:
    print(f'Já está na hora de você se alistar!')
elif idade > 18:
    print(f'Já passou do tempo de alistamento a {passou} anos')
