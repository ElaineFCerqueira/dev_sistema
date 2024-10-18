import os
os.system("cls||clear")

#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Qual a temperatura °C ? "))
Farent = (celsius*1.8) + 32

print("De {} °C, está {} Fahrenheit" .format(celsius, Farent))