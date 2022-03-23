agenda = {                              #dicionário 
    'Roberto':{                         #criar um dicionario pra chave roberto? oras, pra adicionar mais info
    'telefone': '7999115100',
    'email': 'robertocoliver@protonmail.com',
    'endereço': 'rua 7, número 231. Marcos Freire II',
    }, 
    'Clecia': '79999115100'   #'clecia' é uma chave. e o número é o valor  
} 

#for c in agenda.values(): #
print(agenda['Roberto'])   #você pode acessar a chave e qualquer valor dentro dela 
#print(agenda['Roberto]['telefone']) exemplo de filtragem
#agenda.pop('Roberto') remover roberto