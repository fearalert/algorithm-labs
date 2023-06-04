import math
import random

def merge_sort(A,p,r):
    if p<r:
        q = math.floor((p+r)//2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
        
def merge(A,p,q,r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    
    i = 0
    j = 0
    
    for k in range(p, r+1):
        if i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i < len(L):
           A[k] = L[i]
           i  +=  1
        else:
            A[k]=R[j]
            j += 1
            
# Generate a list of 100 random numbers between 1 and 100
random_numbers = random.sample(range(1, 101), 10)

print("Before sorting:", random_numbers)

# Call the insertion sort function
merge_sort(random_numbers, 0, len(random_numbers)-1)

print("After sorting:", random_numbers)