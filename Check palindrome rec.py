def isPalRec(st, s, e):
    # Base case
    if (s == e):
        return True
    # If first and last character does not match
    if (st[s] != st[e]):
        return False
    # If there are more than 
    # two characters, check if
    # middle substring is also
    # palindrome or not.
    if (s < e + 1):
        return isPalRec(st, s + 1, e - 1)
    return True

def isPalindrome(st):
    n = len(st)
    if (n == 0):
        return True
    return isPalRec(st, 0, n - 1)

st = "abbccbba"
if (isPalindrome(st)):
    print("It's a palindrome")
else:
    print("It's not a palindrome")            