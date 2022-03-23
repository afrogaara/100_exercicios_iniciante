#[-1] ultima e [-2] penultima e assim por diante em uma lista 
n = str(input('Digite seu nome completo: '))
p = n.split()
pp = p[0] #primeiro nome 
u = p[-1] #ultimo nome 
print(f'Seu primeiro nome é {pp} \nseu ultimo nome {u}')
 