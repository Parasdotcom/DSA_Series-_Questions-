# Student_dt = [[74,14,52,65,85], [47,56,12,45,20], [20,12,32,25,26], [10,20,30,40,50]]
# print(Student_dt)

# print all elements of index 1
# print(Student_dt[1])
# print all elements of index 4
# print(Student_dt[3])

# Traversing array in 2D (Two Dimensional)
# Student_dt = [[74,14,52,65,85], [47,56,12,45,20], [20,12,32,25,26], [10,20,30,40,50], [20,30,40,50,60]]

# Use for loop to print entire elements of two dimensionals array

# Outer loop
#for x in Student_dt:
    # inner loop
    #for i in x:
        #print(i, end = " ") # print the elements
        #print()


# Program to insert the element into the 2D.

from array import*

arr1 = [[1,2,3,4], [8,9,10,12]]
print("Before inserting the array elements: ")
print(arr1)

# first parameters defines the index no. and second parameter defines the element.  
arr1.insert(1,[5,6,7,8])
print("After inserting the elements\n")

for i in arr1:
    for j in i:
        print(j, end = " ")# print inserted elements
        print()