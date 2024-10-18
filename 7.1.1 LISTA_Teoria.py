import os
os.system('cls||clear')

import random

#Declaração de lista

idade = [] # lista vazia

idade = [27,19,18,63,5] # lista com elementos pré defindos

#ex:
dados = ["Carol",0,1.70,True]
print(f'Nome:{dados[0]}')
print(f'Filhos: {dados[1]}')
print(f'Altura: {dados[2]}')
if dados[3] == True:
    print('Sim, tenho Instagram')
else:
    print('Não tenho instagram')


#Incluindo Elementos
atrizes = ['Paola']

while True:
    nome = input('Digite o novo nome: ')
    atrizes.append(nome)
    resp = input(f'Deseja continuar? (S/N)')
    if resp.upper() == 'N':
       break 
print(atrizes)

atrizes = ['Paola', 'Júlia']
atrizes.insert(0,'Mariana')
print(atrizes)

#ORDENANDO ELEMENTOS

atrizes = ['Paola', 'Nara', 'Julia', 'Mara', 'Galia']
random.shuffle(atrizes) # embaralha os elementos
print(atrizes)

atrizes.sort() # na ordem crescente
print(atrizes)

atrizes.sort(reverse=True)
print(atrizes) # na ordem decrescente

#REMOVENDO ELEMENTOS

atrizes = ['Paola', 'Nara', 'Mara', 'Julia', 'Galia']
atrizes.remove('Nara')
print(atrizes)

atrizes = ['Paola', 'Nara', 'Mara', 'Julia', 'Galia']
atrizes.pop()
print(atrizes)

atrizes = ['Paola', 'Nara', 'Mara', 'Julia', 'Galia']
del atrizes