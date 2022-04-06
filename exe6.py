def calculo(a):
    d = a * 2
    t = a * 3 
    r = a ** (1/2) 
    return d, t, r

lista = list() 
while True:
    lista.clear()
    num = int(input('Digite um número: '))
    lista.append(calculo(num))
    
    for c in lista: 
        print(f"Dobro: {c[0]}\nTriplo: {c[1]}\nraiz: {c[2]}")
   
