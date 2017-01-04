import matplotlib.pyplot as plt

def newPentagonal(pentagonalList):
    n = len(pentagonalList)
    newNumber = n*(3*n-1)//2
    pentagonalList.append(newNumber)
    return pentagonalList


pentagonalList = [0]
size = 10000
for i in range(size):
    pentagonalList = newPentagonal(pentagonalList)

plt.plot(range(size+1),pentagonalList)
plt.show()
