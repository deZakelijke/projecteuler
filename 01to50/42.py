

def addTriangleNumber(triangleList):
    n = len(triangleList)
    newTriangle = n*(n+1)//2
    triangleList.append(newTriangle)
    return triangleList

def readFile():
    f = open('42.txt')
    words = f.readline()
    words = words.split(',')
    for i in range(len(words)):
        words[i] = words[i].rstrip('"').lstrip('"')
    words[-1] = words[-1].rstrip('\n')
    return words

def sumOfWord(word, anchor):
    wordSum = 0
    for char in word:
        wordSum += (ord(char) - anchor + 1)
    return wordSum

def main():
    words = readFile()
    triangleList = [0]
    triangleWordCount = 0
    anchor = ord(words[0])
    for word in words:
        wordSum = sumOfWord(word,anchor)
        while triangleList[-1] < wordSum:
            triangleList = addTriangleNumber(triangleList)
        if wordSum in triangleList:
            triangleWordCount += 1
    print(triangleWordCount)

main()
