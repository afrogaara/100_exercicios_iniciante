# maior e menor, são apenas 2 caminhos. Não existe mais possibilidades.
maior = 0
menor = 0
for c in range(0, 3):
    p = float(input('Digite seu peso: '))
    if c == 1:
        maior = p
        menor = p
    else: 
        if p > maior: 
            maior = p
        elif p < menor: 
            menor = p
print(f'O maior número é {maior} e o menor número é {menor}')

#Se você digitar pesos inteiros, o resultado dará errado. Isso pq está em float
