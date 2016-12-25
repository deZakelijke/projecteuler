

def addTriangleNumber(triangleList):
    n = len(triangleList)+1
    newTriangle = n*n(n+1)/2
    triangleList.append(newTrinagle)
    return triangleList

def readFile():
    f = open('42.txt')
    words = f.readline()
    words = words.split(',')
    print(words)



readFile()
