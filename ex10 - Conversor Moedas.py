import os

os.system("clear||cls")

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

c=float(input("Quanto dinheiro você tem na carteira? R$ "))
d=c/5.47

print("Com R$ {} reais, você pode comprar $ {:.3} dolares ".format(c,d))

