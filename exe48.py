contagem = 0
s = 0
for c in range(0, 500, 1):
    calculo = c % 3
    if calculo == 0:
        s += c
        contagem += 1
print(f'Existem {contagem} números multiplos de 3 \nA soma entre todos esses multiplos é {s}')
