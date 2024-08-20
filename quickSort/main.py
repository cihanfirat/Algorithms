def QuickSort(arr, l, h): # array, low, high
    # If the starting index is less than the ending index, we need to sort
    if l < h:
        # Partition the array and get the pivot index
        j = Partition(arr, l, h)
        
        # Recursively apply QuickSort to the left subarray (elements before pivot)
        QuickSort(arr, l, j - 1) # arr, low, pivot-1
        
        # Recursively apply QuickSort to the right subarray (elements after pivot)
        QuickSort(arr, j + 1, h) # arr, pivot+1, high

def Partition(arr, l, h):
    # Set the pivot element as the first element of the current subarray
    pivot = arr[l]
    
    # Initialize two indices: i starting from l, j starting from h
    i = l
    j = h
    
    # Loop to move i and j towards each other and swap elements
    while i < j:
        # Move i to the right as long as elements are less than or equal to the pivot
        while arr[i] <= pivot:
            i += 1
        
        # Move j to the left as long as elements are greater than the pivot
        while arr[j] > pivot:
            j -= 1
        
        # If i is still less than j, swap the elements at i and j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at index j
    arr[l], arr[j] = arr[j], arr[l]
    
    # Return the index j, which is now the position of the pivot element
    return j

# Test the QuickSort algorithm
A = [1, 5, 8, 3, 2, 4]

# Apply QuickSort to the entire array
QuickSort(A, 0, len(A) - 1)

# Print the sorted array
print(A)
