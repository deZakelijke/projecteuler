import math

# Returns True if n is prime, False oif otherwise
def prime(n):
    border = math.ceil(math.sqrt(n))
    for i in range(2, border+1):
        if n%i==0:
            return False
    return True

# Returns a list of all prime numbers between 1 and n
def sieve(n):
    numberList = list(range(1,n+1))
    i = 2
    while i < n:
        for j in range(2*i, n+1, i):
            try:
                numberList.remove(j)
            except ValueError:
                continue
        i += 1
    return numberList

# Returns the lenght of the sequence of cnsecutive prime numbers
# from the formula n^2 +a*n + b, starting at n=0
def primeSequence(a, b):
    sequenceLength = 0
    n = 0
    nextValue = n **2 + a*n + b
    while prime(nextValue):
        sequenceLength +=1
        n += 1
        nextValue = n **2 + a*n + b
    return sequenceLength


def main():
    aRange = 1000
    bList = sieve(1000)

    sequenceLengths = []

    for i in range(1, aRange+1):
        sequenceLengths.append([])
        for j in range(len(bList)):
            primeRange = primeSequence(i, bList[j]) 
            sequenceLengths[i-1].append(primeRange)

    maxA = 0
    maxAIndex = 0
    maxB = 0
    maxBIndex = 0
    for i in range(len(sequenceLengths)):
        continue

main()
