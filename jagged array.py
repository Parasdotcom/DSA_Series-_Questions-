arr = [[10], [12, 3], [33, 22, 2], [2],...]
# Neither the size of 
# the each row is known nor the count of lists.
for value in arr:
    i = 0
    j = 0
    if isinstance(value, list):
        for other in value:
            print("a[%s][%s] = %s" % (i, j, other))

            i += 1
            j += 1
# Every new row start with indices [0][0]. 
# Value 12 should be [1][0].
