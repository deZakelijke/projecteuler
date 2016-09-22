import math

# Reads the names from the file and makes it a str list
def readFile():
    f = open('22.txt')
    f = f.read()
    rawNames = f.split('"')
    names = []
    for i in range(len(rawNames)):
        if i%2 == 1:
            names.append(rawNames[i])
    return names

# TODO make sort function
# Could do this myself but sort() works fine for now
def sort(names):
    return sortedNames

# TODO make function to calculate values
def calcVal(names):
    value = 0
    for i in range(len(names)):
        wordValue = 0
        for l in names[i]:
            wordValue += ord(l)-64
        value += wordValue * (i+1)
    return value

def main():
    names = readFile()
    names.sort()
    value = calcVal(names)
    print(value)


main()
