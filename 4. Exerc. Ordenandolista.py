
#mês de maior valor?

import os
os.system('cls||clear')

mes = ['janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro e dezembro']
valor = [100,210,75,180,4000,53,500,123,576,800,320,760]

for i in range (len(valor)):
    for j in range(len(valor)):
        if valor[i]<= valor[j]:
            var = valor[i]
            var1=mes[i]
            valor[i] = valor[j]
            mes[i]=mes[j]
            valor[j] = var
            mes[j]=var1
               
print(f'O maior valor do mês foi: {var} reais ; ', end='')
print(f'Os valores na ordem será: {valor}')
