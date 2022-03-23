times = ('Palmeira Corinthians São-Paulo Santos Fluminense Internacional Ceará Flamengo').split()


for c in range(0, len(times)):
     
     print(f'lista de time do brasileirão: {times[c]}', end='\n')
     if c > 6:
        print(f'os 5 primeiros times são {times[:5]}', end='\n')
        print(f'os 4 ultimos times são {times[4:]}', end='\n')
        print(f'o internacional está na posição {times[5]}', end='\n')    
        print(f'os times na ordem alfabética são: {sorted(times)}')
      


   