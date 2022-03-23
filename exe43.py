from math import pow

peso = float(input('Digite o peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / pow(altura, 2) 

if imc < 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')