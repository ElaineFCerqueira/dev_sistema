#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

#a = float(input("Digite o angulo :"))

#seno = math.sin(math.radians(a))
#print('O angulo de {} tem o SENO de {:.2f}' .format(a,seno))

#cosseno = math.cos(math.radians(a))
#print('O angulo de {} tem o COSSENO de {:.2f}' .format(a,cosseno))

#tangente = math.tan(math.radians(a))
#print('O angulo de {}, tem a TANGENTE de {:.2f}'.format(a,tangente))

#outro metodo

from math import radians, sin, cos,tan

a = float(input("Digite o angulo :"))

seno = sin(radians(a))
print('O angulo de {} tem o SENO de {:.2f}' .format(a,seno))

cosseno = cos(radians(a))
print('O angulo de {} tem o COSSENO de {:.2f}' .format(a,cosseno))

tangente = tan(radians(a))
print('O angulo de {}, tem a TANGENTE de {:.2f}'.format(a,tangente))
