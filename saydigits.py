num = int(input("Enter a number: "))
result = 0
alphabet = 0
string = 0
while num > 0:
    digit = num % 10
    result = result * string
    string = ["One", "Two", "Three", "Four", 
    "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    result = result + alphabet
    num = num//10
    print("alphabet is:", string, result)    