def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Paras Saxena"
print ("The Original string is :",end="")
print(s)

print("The reversed string(using loops) is :", end="")
print(reverse(s))