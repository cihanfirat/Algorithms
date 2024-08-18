def BinarySearch(A,l,r,key): #!!!!ARRAY MUST BE ORDERED TO IMPLEMENT BINARY SEARCH!!!!! l= left r=right key=key value that we want to search in array
    
    while (l<=r):
        mid=(l+r)//2
        
        if key==A[mid]: # if key is in the middle , return the mid index
            return mid
            
        elif key>A[mid]: # if key is greater than middle value then change your searching bound as right hand side of the array
            l=mid+1
            
        else:
            r=mid-1  # if key is smaller than the middle value then change your searching bound as left hand side of the array
            
    return 0 #return 0 if key is not found
    
if __name__ == "__main__":
    arr=[2,3,5,6,8,10,22,33,37,56]
    
    k=int(input("Enter key value: ")) # getting key from user (must be integer).
    
    res = BinarySearch(arr,0,len(arr)-1,k)
    
    
    if res > 0: # if key is found
        print("Key is found at index", res)
    else: # if returns 0
        print("Key is not found!")
