#A Pilha deverá ser implementada utilizando uma estrutura homogênea com 20 posições, 
#e as seguintes funções deverão ser implementadas para a manipulação da pilha: 
# Adicionar um livro a lista
# Visualizar lista de livros
# Remover um livro da lista
# Sair do programa.

import os
os.system('cls||clear')

lista = []

while True:
    print('''
          \n Menu de Opções:
          1 - Adiconar nome
          2 - Visualizar lista
          3 - Remover lista
          4 - Mostrar elementos
          5 -
        ''')
    x = int(input('Digite a opção desejada: \n'))
    print('\n')

    match (x):
        case 1 : 
            y = str(input('Digite o nome desejado: '))
            lista.append(y)
            print('Nome adicionado com sucesso')

        
        case 2:
            if lista ==[]:
                print('A lista de nome está vazia')
            for i, nome in enumerate(lista):
                print(f'{i} - {nome}', end='')
        
        case 3:
            if lista == []:
                print('Lista está vazia')
            else:
                y = input(f'O nome {lista[0]} será removido. Confirmar(s/n)?')
                if y.lower() == 's':
                    removid = lista.pop(0)
                    print(f'O item {removid} foi removido da lista')
        case 4:
            contar = len(lista)
            print(f'A lista tem {contar} elementos')



            
