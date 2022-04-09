#calculando meia vida pela grama inicial e grama final ( sem tempo )
def meia_vida(num=0, b=0):
    svd = list()
    cont = 0 
    pos = num 
    for c in range(num, 0, -1):
        pos /= 2 
        print(end=" ")
        f = pos
        cont += 1 
        segundos = 50 * cont 
        if f >= 0.050:
            svd.append(f)  
            print(svd, end="\n")
        else: 
            if f < 0.05:
                print(f"Foram necessários {segundos} segundos para decompor em 0.05 gramas")
                break         

x = int(input("Digite a grama do objeto: "))
g = float(input("Digite a grama final do objeto: "))
meia_vida(x, g)
