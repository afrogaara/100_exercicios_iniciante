contagemm = contagemf = 0 
guarda = []

lista = ['M', 'F' ]
sexo = str.upper((input('M/F? '))).strip()[0]

while sexo != lista[0] or sexo != lista[1]:
    sexo = str.upper((input('digite, um sexo válido. M/F: '))).strip()[0]
    
    if sexo  == lista[0] or sexo == lista[1]:
        guarda.append(sexo)
        print(f'{guarda} registrado com sucesso ')
    