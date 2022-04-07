def corrigido(a=0, b=0, c=0):
    lin = len(c)
    print("=" * lin)
    aumento = a * (b / 100) 
    saida = a + aumento  
    return saida 

msg = str("Correção salarial")

while True:
    a = float(input('Digite o seu salário: '))
    b = int(input(f"Quanto em % "))
    print(f"{corrigido(a, b, msg)}")
