import os

os.system("cls||clear")

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input("Qual o valor do produto? R$ "))
desc = (prod - (prod*5)/100)


print("O produto de R$ {}, com desconte fica R$ {:2}" .format(prod,desc))
