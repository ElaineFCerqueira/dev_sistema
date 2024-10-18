import os
os.system ("cls||clear")

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero"))

soma = n1 + n2
sub = n1 - n2
mult = n1*n2
div = n1/n2
pont = n1**n2
resto = n1%n2
divisao_inteira = n1//n2
print(soma)
print(sub)
print(mult)
print(div)
print(pont)
print(resto)
print(divisao_inteira)

print("A soma é {} , a subtração {}, a multiplicação é {}, a divisão é {}, a potenciação {}  " .format(soma,sub,mult,div,pont))