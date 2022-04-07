from math import tan, sin, cos, radians
angulo = int(input('Digite o valor do angulo: '))
sen = sin(radians(angulo))
coseno = cos(radians(angulo))
tang = tan(radians(angulo))
print(f'O seno do angulo {angulo} é {sen}\nO cosseno do angulo {angulo} é {coseno}\nA tangente do angulo{angulo} é {tang}')
