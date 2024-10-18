import os
os.system("cls||clear")

print("Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.")

a = (float(input("Digite a altura da parede ")))
l = (float(input("Digite a largura da parede ")))
area = a*l
tinta = area/2

print("Para uma parede com area de {} metros, será necessário {} litros de tinta" .format(area,tinta))

