s = 0
for c in range(0, 7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(f'A soma de todos os valores pares é igual a {s}')