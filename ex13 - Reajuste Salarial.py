import os

os.system ("cls||clear")

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Qual o seu salario? "))
novo = salario + (salario*15/100)

print("Você recebeu um aumento. O salario de R$ {} ,passou para R$ {:.4}" .format(salario,novo))
