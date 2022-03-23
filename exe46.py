from time import sleep
print(f'Contagem dos fogos vai começar')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('BUM')
