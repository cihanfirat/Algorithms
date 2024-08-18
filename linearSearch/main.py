def linearSeach(l,target):
    n = len(l)
    for i in range(0,n): #search along the array
        if l[i] == target: #if target is found return index
            return i

if __name__ == "__main__":
    array = [2,3,4,10,40]
    x = 4
    result = linearSeach(array, x)
    if(result == -1):
        print("Element is not in array")
    else:
        print("Element is in array at index : " , result)