def minIndex(a, i, j):
    if i == j:
        return i
    # Find minimum of remaining elements
    k = minIndex(a, i + 1, j)

    # Return minimum of current
    # and remaining
    return (i if a[i] < a[k] else k)

def recuSelectionSort(a, n, index = 0):

    # Return when starting and size are same
    if index == n:
        return -1
    # calling minimum index function
    # for minimum index
    k = minIndex(a, index, n-1)
    
    if k != index:
        a[k], a[index] = a[index], a[k]

arr = [3, 1, 5, 2, 7, 0]
n = len(arr)

# Calling function
recuSelectionSort(arr, n)

# printed sorted list
for i in arr:
    print(i, end = ' ')