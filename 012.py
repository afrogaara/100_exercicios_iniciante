def pag(a=0, b=0):
    
    a = p * (d/100)
    b = p - a     
    
    return a, b 

lista= list()
while True:
    d = int(input('Digite o desconto do cupom em %: '))
    p = float(input('Digite o valor do produto comprado: '))
    
    lista.append(pag(d, p))
    for c in lista: 
        print(f"O valor do desconto é: {c[0]} $$\nPreço corrigido: {c[1]}", end="\n")
