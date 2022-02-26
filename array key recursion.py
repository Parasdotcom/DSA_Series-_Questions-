def recSearch(arr, l, r, key):
    if r < l:
        return -1
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    return recSearch(arr, l+1, r-1, key)

arr = [3, 5, 1, 2, 6]
n = len(arr)
key = 2
index = recSearch(arr, 0, n-1, key)
if index != -1:
    print("Element", key, "is present at index %d" %(index))

else:
    print("Element is not present %d" %(key))
