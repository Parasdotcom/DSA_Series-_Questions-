def sumarray(arr, N):
    if len(arr) == 1:
        return arr[0]

    else:
        return arr[0] + sumarray(arr[1:], N)

arr = []
arr = [1,2,3,4,5]

# Calculating length
N = len(arr)
ans = sumarray(arr,N)
print(ans)