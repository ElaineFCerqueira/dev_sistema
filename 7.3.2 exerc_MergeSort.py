# Utilizando o algoritmo MergeSort, você e um colega deverão implementar uma função que receba por parâmetro uma estrutura homogênea desordenada, 
# Aplique o algoritmo de ordenação e retorne a estrutura homogênea ordenada de forma crescente. 
# Importante: para esta etapa, é obrigatória a utilização do conceito de recursividade.">

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [1,7,10,9,2,3,20,18,33,90,44,34,21,27,5,8,99,54,68]
    print("A Lista é : ", end="\n")
    print_list(arr)
    mergeSort(arr)
    print("MergeSort : ", end="\n")
    print_list(arr)
