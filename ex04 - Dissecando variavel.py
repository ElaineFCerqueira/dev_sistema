import os
from unicodedata import numeric

os.system ("clear || cls")



n = input ("Digite algo ")
print("O tipo primitivo desse valor é : ", type(n))
print("Só tem espaços? ", n.isspace())
print("É só um numero?", n.isnumeric())
print("É alfabetico?  ", n.isalpha())
print("É alfanumerico ?", n.isalnum ())
print("Está em maiuscula? ", n.isupper())
print("Está em minuscula? ", n.islower())
print("Está capitalizada? ", n.istitle ())

