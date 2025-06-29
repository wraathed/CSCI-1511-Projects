import string

def printWds(data):

    for x in sorted(data.keys()):
        print(f"{x} :: {data[x]}")
    return

def wordFreq(fptr):

    freq = {}
    line = fptr.readline()
    punctChars = tuple(string.punctuation)

    while line:
        for c in punctChars:
            line = line.replace(c, "")
        
        words = line.split()

        for word in words:
            tmp = word.lower()
            freq[tmp] = freq.get(tmp, 0) + 1

        line = fptr.readline()
    return freq