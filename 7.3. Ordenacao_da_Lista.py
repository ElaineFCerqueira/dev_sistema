
import os
os.system('cls||clear')


#BubbleSort (ou ordenação por flutuação)
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





a = [5,3,2,4,1,6]
bubble(a)

for v in a:
    print(v)

# MergeSort (ou ordenação por mistura) 

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
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    print_list(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)

# HeapSort (ou ordenação por heap), 
# InsertionSort (ou ordenação por inserção), 
 
