from datetime import date

data = date.today()
data = data.year

maiores = 0
menores = 0 
maior = 0 

for c in range(0, 7+1):
    ano = int(input('Digite seu ano de nascimento: '))
    if data - ano > 18:
        maiores += 1
    elif data - ano < 18:
        menores += 1
    elif data - ano == 18:
        maior += 1

print(f'{maiores} são maiores de idade \n{menores} são menores de idade \n{maior} fizeram 18 recentemente')

   