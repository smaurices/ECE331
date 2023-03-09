import random

def swap(a, b):
    s=0
    temp = a
    a = b
    b = temp
    s += 1
    return a, b

def partition(arr, low, high):
    global C, P
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = swap(arr[i], arr[j])
            C += 1
    arr[i+1], arr[high] = swap(arr[i+1], arr[high])
    P += 1
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

A = [i for i in range(1, 21)]
n = len(A)
Ci, Si, Pi = [], [], []

random.seed()
for i in range(1000):
    B = A.copy()
    for j in range(n):
        k = random.randint(0, j)
        B[j], B[k] = swap(B[j], B[k])
    C, S, P = 0, 0, 0
    quicksort(B, 0, n-1)
    Ci.append(C)
    Si.append(S)
    Pi.append(P)

Cmean = sum(Ci) // 1000
Smean = sum(Si) // 1000
Pmean = sum(Pi) // 1000
print(f"Sample means:\nC = {Cmean}\nS = {Smean}\nP = {Pmean}")
