from random import randint

contagem = 0
c = randint(0, 2)

p = int(input('Adivinhe o número: '))
contagem += 1 
while p != c:
    
    p = int(input('Tente novamente: '))    
    contagem += 1 

print(f'O computador escolheu {c}. total de tentativas {contagem}')