import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#primeiro você define o tipo de conexão
try:
    port = int(input('Digite a porta para se conectar: '))
    cliente.connect(('192.168.100.77', port)) #depois você se conecta definindo o host e a porta
    cliente.send(b'GET / HTTP/ 1.1\nHost: www.google.com.br\n\n\n') #padrão http
#depois você envia requisições seguindo a norma do protocolo que a porta exige
#você está enviando string e o servidor só aceita binarios
    recebidos = cliente.recv(1000024).decode()#resposta é em bytes, precisamos dela em string
except:
    print('algum erro ocorreu')
print(recebidos)



