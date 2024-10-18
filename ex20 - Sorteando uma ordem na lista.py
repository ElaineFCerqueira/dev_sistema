#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a 
# ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Digite um nome: ')
n2 = input('Digite um nome: ')
n3 = input('Digite um nome: ')
n4 = input('Digite um nome: ')

lista = [n1,n2,n3,n4]

random.shuffle(lista) #embaralha a lista
print(lista)