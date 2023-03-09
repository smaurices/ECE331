#Write a program to run Quicksort (pseudocode on p. 171) on 1,000 random permutations of the array A = < 1, 2, 3, ..., 20 >.  For each permutation i=1, 2, ..., 1000, find the number of comparisons C_i , the number of swaps S_i and the number of times PARTITION is called, P_i, when running Quicksort. Output the sample means
#C = 1/1000 Sum_i C_i,    S = 1/1000 Sum_i S_i,   P = 1/1000 Sum_i P_i.

Pseudocode = """
QuickSort(a,p,r)
  if p < range  
      #partition the subarray around the pivot, which ends up in A[q]
      q = Partition(A,p,r)
      QuickSort(A,p,q-1) #sort the low side
      QuickSort(A,q+1,r) #sort the high side
"""
import random

def Quicksort(A, p, r):
  #Needed global variables in order to access in main
  global Part_, Comp_

  #print(A)
  if p < r:
    q = Partition(A, p, r)
    Part_ += 1
    Quicksort(A, p, q - 1)  #low side
    Quicksort(A, q + 1, r)  #high side
  #print(A)
  return

def Partition(A, p, r):
  global count_
  global Part_, Comp_
  pivot = A[r]  #the pivot
  #print(pivot)
  i = p - 1  #highest index low side
  #j = p
  for j in range(p, r):
    Comp_ +=1
    if A[j] <= pivot:
      i += 1
      #exchange
      (A[i], A[j]) = swaps(A[i], A[j])
      if (A[i] != A[j]):
        count_ += 1
  #exchange
  (A[i + 1], A[r]) = swaps(A[i + 1], A[r])
  if (A[i + 1] != A[r]):
    count_ += 1
  return i + 1

#exchange with
def swaps(i, j):
  #Needed global variables in order to access in main
  dummy_var = i
  i = j
  j = dummy_var
  return i, j

if __name__ == "__main__":
  A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  # Testing array: A = [2, 8, 7, 1, 3, 5, 6, 4]
  #Globa variable set to 0
  Comp_, count_,Part_ = 0,0,0
  cVal, sVal, pVal, = [], [], []

  """ For testing functions: 
        print("Given array:", A)
        #Part_, count_S = 0, 0,
        l = Quicksort(A, 0, len(A) - 1)
        print("Sorted array:", A)
        ci.append(Part_)
        si.append(count_)
  """
  
  #For loop functions like a permutation
  n = 1000
  for i in range(n):
    random.shuffle(A)
    #print(A)
    Part_, count_ = 0, 0
    Quicksort(A, 0, len(A) - 1)
    sVal.append(count_)
    pVal.append(Part_)
    
  #comparisons
  cVal.append(Comp_)
  
  #find the means
  Pmean = sum(pVal) / 1000
  Smean = sum(sVal) / 1000
  Cmean = sum(cVal) / 1000
  
  #Output the sample means C = 1/1000 Sum_i C_i,    S = 1/1000 Sum_i S_i,   P = 1/1000 Sum_i P_i.
  print("Number of comparisons:", Cmean)
  print("Number of swaps:", Smean)
  print("Number of times Partition called:", Pmean)
