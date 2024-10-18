import os

os.system("cls|| clear")

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input("Digite um numero "))
c = n*100
mi = n*1000

print("{} metros, equivale a {} centimetros e {} milimetros" .format(n,c,mi))
