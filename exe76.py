tupla = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 
        'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120, 'Canetas', 22.30 )

for c in range(0, len(tupla)):
    
    def imprimir_menu():
        if c % 2 == 0:
            print(f'{tupla[c]} ----------------------- {tupla[c+1]}')

imprimir_menu()