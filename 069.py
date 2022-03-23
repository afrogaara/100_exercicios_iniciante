#lendo sexo e idade
lista_idade = []
lista_sexo = []
lista_mulheres = [] 

while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo M/F: ')).upper()[0]
        
    p = str(input('Quer parar? S/N: ')).upper()[0] 
    
    # Quantos homens foram cadastrados ?
    if sexo == 'M': 
        lista_sexo.append(sexo)
        

    # Quantas pessoas tem mais de 18 anos ? 
    if idade > 18:
       lista_idade.append(idade)
       
     
    # Mulheres com menos de 20 anos ?
    if sexo == 'F' and idade < 20:
        lista_mulheres.append(idade)
      
    #condição de parada
    if p == 'S':
        print('======= FIM DO PROGRAMA ========')
        break    

print(f'foram registrados: {len(lista_sexo)} Homens')

print(f'{len(lista_idade)} pessoas tem mais de 18 anos')

print(f'{len(lista_mulheres)} tem menos de 20 anos de idade')