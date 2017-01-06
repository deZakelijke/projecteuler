# Does not give the right answer. Problem not yet indentified

import math

# Checks to see if a number is an abundant number
# en.wikipedia.org/wiki/Abundant_number 
def abundant(n):
    border = math.ceil(math.sqrt(n))
    divisors = []
    for i in range(1, border+1):
        if n % i ==0:
            divisors.append(i)
            divisors.append(n//i)
    divisors = list(set(divisors))
    divisors.remove(n)
    if sum(divisors) > n:
        return True
    else:
        return False

# Checks to see if n can be made from a sum of two integers in numberList
# numberList[0] is the even numbers, numberList[1] the uneven numbers.
# This seperation is made to speed up the search process
def findSum(n, numberList):
    if n%2==0:
        for i in range(len(numberList[0])):
            if numberList[0][i] >n:
                break
            for j in range(i, len(numberList[0])):
                if numberList[0][j] > n:
                    break
                if numberList[0][i] + numberList[0][j] == n:
                    return False
        for i in range(len(numberList[1])):
            if numberList[0][i] >n:
                break
            for j in range(i, len(numberList[1])):
                if numberList[0][j] > n:
                    break
                if numberList[1][i] + numberList[1][j] == n:
                    return False

    else:
        for i in range(len(numberList[0])):
            if numberList[0][i] >n:
                break
            for j in range(len(numberList[1])):
                if numberList[1][j] > n:
                    break
                if numberList[0][i] + numberList[1][j] == n:
                    return False
    return True

def main():
    maxNumber = 28123
    totalSum = 0
    abundantNumbers = [[],[]]
    for i in range(1,maxNumber+1):
        if abundant(i):
            if i%2==0:
                abundantNumbers[0].append(i)
            else:
                abundantNumbers[1].append(i)

    print('List complete')


    for i in range(maxNumber+1):
        if findSum(i, abundantNumbers):
            totalSum += i
        if i%1000 ==0:
            print(i)
    print(totalSum)


main()


