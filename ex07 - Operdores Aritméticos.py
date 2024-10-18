import os
os.system("cls||clear")

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input("Digite a primeira nota "))
n2 = float(input("Digite a segunda nota "))
media = (n1+n2)/2

print("A primeira nota {}, e a segunda nota {}. A média do aluno foi {}" .format(n1,n2,media))
