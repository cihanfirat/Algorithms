def insertionSort(A):
    n=len(A) #get lenght of array
    for j in range (1,n): # loop until the end of the array
        key = A[j] 
        i=j-1
        while i>=0 and A[i]>key: #comparison
            A[i+1] = A[i] # exchanging
            i=i-1
        A[i+1] = key

arr=[1,5,2,8,11,3,9]
insertionSort(arr)
print(arr)

