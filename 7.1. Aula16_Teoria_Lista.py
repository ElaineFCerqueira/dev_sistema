import os

os.system('cls||clear')


num = [2,5,9,1]
num [2] = 3
print(num)

num.append(7) #acrescenta numero a lista
print(num)

num.sort() #coloca em ordem crescente
print(num)

num.sort(reverse=True) #coloca em ordem decrescente
print(num)

len(num) #conta quantos elementos tem
print(num)


num.insert(2,0) #adiciona valores numa posição especifica
print(num)

num.pop() #remove o ultimo item da lista
print(num)

num.pop(2) #remove o penultino item adicionado a lista
print(num)

num.remove(5) #remove o numero corresponde na lista
print(num)


if 5 in num:
    num.remove(5)
else:
    print('Não achei na lista')    


#começar uma lista vazia pode ser assim:
valores = [] 

#ou assim
valores = list()

valores.append(5)
valores.append(9)

for v in valores:
    print(f'{v}...', end='') # end=''se quiser a lista na mesma linha

#se quiser mostrar o indice
for c,v in enumerate(valores): 
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')    

#ler valores pelo teclado e colocar na lista
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

#criar uma cópia da lista
a = [1,2,3,4]
b = a[:]

#duplicar uma lista
a = [1,2,3,4]
b = a
