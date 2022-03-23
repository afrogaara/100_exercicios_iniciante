frase = str.lower((input('Digite sua frase: ')))
espaço = frase.replace(' ', '')

print('Esta frase é um polindromo?')

if frase == frase[::-1]:
    print('é um polindromo')
else:
    print('não é um polindromo')