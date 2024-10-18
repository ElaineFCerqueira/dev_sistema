# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import os
os.system ('cls||clear')
from random import choice


n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1,n2,n3,n4]

escolhido = choice(lista) #escolha dentro da lista
print =(f'O aluno escolhido foi {escolhido}')


