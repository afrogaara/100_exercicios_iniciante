lista = []
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    lista.append(peso)
    maior = max(lista)
    menor = min(lista)
print(f'O maior número é {maior} \ne o menor número é {menor}')