import os
os.system ("cls||clear")


#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Km = float(input("Quantos Km foram percorridos? "))
dia = int(input("Por quantos dias? "))

dias = dia * 60
novo = Km * 0.15

print("alugado por: ", dias)

print("alugado por: ", novo)

print(dias + novo)
