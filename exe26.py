#Não conseguir installar a porra do pygame 
#print(nome[0:]) # interessante saber 
#.count() quantas x coisas existem naquela frase 
#.upper().count() jogar tudo pro maisculo e contar quantas x palavras maisculas existem naquela frase 
#len(frase.strip()) saber o comprimento de uma palavra/frase ( quantas letras tem )
#frase.replace('x', 'y') ====== "troca a palavra", mas não salva. Você precisa fazer uma nova atribuição
    #nome = frase.replace('x','y')
#replace é mt importante pois ele remove todos os espaços vazios n.replace(' ', '')
#.capitalize().find() encontrar uma palavra e mostrar sua posição 
#n = frase.split() você consegue transformar uma frase em uma lista ( separar palavras ) print(n)
#.lower
#.strip ( tirar os espaços ) iniciais e finais 
frase = str.upper((input('Digite uma frase que você gosta: ')))
semspace = frase.replace(' ', '')
e = frase.count('A')
p = frase.find('A')
r = frase.rfind('A')
palavra = 'A'
if palavra in frase:
    print(f'A letra {palavra} aparece {e} vezes')
    print(f'A letra {palavra} aparece pela primeira vez na posição {p}')
    print(f'A letra {palavra} aparece pela ultima vez na posição {r}')


