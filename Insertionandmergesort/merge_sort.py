import math

def merge_sort(A,p,r):
    if  p < r:
        q = math.floor((p+r)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


def merge(A, p, q, r):
   
    L = A[p:q+1]
    R = A[q+1:r+1]
 
    # for i in range(0, n1):
    #     L[i] = A[p + i-1]
 
    # for j in range(0, n2):
    #     R[j] = A[q + j]
 
    i = 0    
    j = 0         
    for k in range(p,r+1):
        if  i<len(L) and  j<len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i<len(L):
           A[k] = L[i]
           i  +=  1
        else:
            A[k]=R[j]
            j += 1
           
    