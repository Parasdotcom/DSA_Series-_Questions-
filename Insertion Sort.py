def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
arr = [10, 13, 12, 14, 8]
insertionSort(arr)
print("Sorted Array is : ")
for i in range(len(arr)):
    print("%d" %arr[i])