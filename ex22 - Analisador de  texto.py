import os
os.system('cls||clear')

#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome... ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minuscula é {nome.lower()}')

#– Quantas letras ao todo (sem considerar espaços).

print(f'Seu nome tem ao todos {len(nome)-nome.count(' ')} letras') # conta somente as letras e retira o espaço


#– Quantas letras tem o primeiro nome.

print(f'Seu primeiro nome tem {nome.find(' ')} letras')

# - Separar os nomes
separa = nome.split()
print(separa)