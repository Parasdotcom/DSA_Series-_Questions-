# String Reverse using Recursion 
def reverse(string):
    # Base case
    if len(string) == 0:
        return
    temp = string[0]
    reverse(string[1:])
    print(temp, end="")
string = "paras saxena"
reverse(string)    

