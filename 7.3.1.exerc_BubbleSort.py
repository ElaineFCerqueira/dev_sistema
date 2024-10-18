#Utilizando o algoritmo BubbleSort, que receba por parâmetro uma estrutura homogênea desordenada
#Aplique o algoritmo de ordenação e retorne a estrutura homogênea ordenada de forma crescente

def bubble(A):
    if len(A) <= 1:
        sA = A
    else:
        for j in range(0,len(A)):
            for i in range(0,len(A)-1):
                if A[i]>A[i+1]:
                    Aux = A[i+1]
                    A[i+1] = A[i]
                    A[i] = Aux
        sA = A
    print(sA)


a = [1,7,10,9,2,3,20,18,33,90,44,34,21,27,5,8,99,54,68]
bubble(a)

for v in a:
    print(v)











