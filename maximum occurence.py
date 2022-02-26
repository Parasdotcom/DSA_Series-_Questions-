def getMaxOccuringChar(str):

    # freq used in hash table 
    freq = [0 for i in range(100)]

    # To store maximum frequency
    max = -1

    # To store the maximum occuring
    # character length of 'str'
    len__ = len(str)

    # get frequency of each character of 'str'
    for i in range(0, len__, 1):
        freq[ord(str[i]) - ord('a')] +=1

    # for each character, where character
    # is obtained by ('i + a') check whether
    # it is the maximum character so for and
    # accordingly update 'result'
    for i in range(26):
        if (max < freq[i]):
            max = freq[i]
            result = chr(ord('a') + i)
        # maximum occuring character
    return result

if __name__ == '__main__':
    str = "sample program"
    print ("Maximum occuring character =", getMaxOccuringChar(str))                