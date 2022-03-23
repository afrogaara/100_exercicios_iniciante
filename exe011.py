import socket
lista = list()
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#primeiro você define o tipo de conexão
try:
    while True:
        msn = str.lower(input("Digite uma mensagem: ")) + '\n'
        cliente.sendto(msn.encode(), ('192.168.100.77', 10000))
        response, ip_port = cliente.recvfrom(1024) #response é a resposta do servidor que estará em binário
        print(f'{ip_port[0]}: {ip_port[1]}\ndiz: {response.decode()}') #decode transforma o binário em string

        if msn == 'sair' or response == 'sair':
            break
except Exception as error:
    print('algum erro ocorreu')
    print(error)
