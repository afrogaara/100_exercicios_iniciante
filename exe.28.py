from random import randint
n = randint(0, 5)
p = int(input('Tente adivinhar um número escolhido por mim entre 0 e 5: '))
if p == n:
    print('Parabéns, você acertou :)')
else:
    print('Errou jovem')