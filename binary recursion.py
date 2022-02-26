def binarySearch(arr, low, high, x):
    # base case
    if high >= low:
        mid = (high + low)//2

        # If element present is middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then 
        # It can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid - 1, x)
        # Else the element can only be present in right sub array.
        else:
            return binarySearch(arr, mid + 1, high, x)

    else:
            # Element is not present in the array.
            return -1

arr = [2, 3, 4, 5, 10, 11]
x = 12
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")    
