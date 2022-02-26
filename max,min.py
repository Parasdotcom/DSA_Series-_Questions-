# Maximum and Minimum occuring character in string.  

string = "my name is paras saxena"
freq = [None] * len(string)
minChar = string[0]
maxChar = string[0]

# Count each word in given string and store in arr freq
for i in range(0,len(string)):
    freq[i] = 1
    for j in range(i+1, len(string)):
        if(string[i] == string[j] and string[i] != '' and string [i] != '0'):
            freq[i] = freq[i] + 1

            # Set strings to 0 to avoid printing visited characters

            string = string[:j] + '0' + string[j+1:]

# Determine minimum and maximum occuring characters
min = max = freq[0]
for i in range(0, len(freq)):

    # if min is a greater than a frequency of a character
    # then, store frequency in min corresponding char in min char
    if(min > freq[i] and freq [i] != '0'):
        min = freq[i]
        minChar = string[i]
    if(max < freq[i]):
        max = freq[i]
        maxChar = string[i]

print("Minimum occuring character:" + minChar)
print("Maximum occuring character:" + maxChar)