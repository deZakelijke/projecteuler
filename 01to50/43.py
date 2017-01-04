
def permutations(inputList):
    try:
        n = len(inputList)
    except TypeError:
       print('Input is not an iterable and does not have permutations.\n') 

    if n:
        allPermutations = permRecur(n, inputList)
    else:
        allPermutations = 0

    print(allPermutations)
    totalSum = 0
    while allPermutations:
        try:
            newNum = next(allPermutations)
            totalSum += check(newNum)
            print(totalSum)
        except:
            print(totalSum)
            break
        

def check(n):
    return n

def permRecur(n, inputList):
    if n==1:
        yield inputList
    else:
        for i in range(n-1):
            for hp in permRecur(n-1, inputList): yield hp
            j = 0 if (n % 2) == 0 else i
            inputList[j], inputList[n-1] = inputList[n-1], inputList[j]
        for hp in permRecur(n-1, inputList): yield hp             



permutations([1,2,3,4])
    
