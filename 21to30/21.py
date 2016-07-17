# Takes an int and returns all divisors of int as a list
import math

def divisors(num):
    divSum = 0
    root = math.sqrt(num)
    for i in range(1, int(root)+1):
        if num%i == 0:
            divSum += i 
            divSum += num//i
    if root == int(root):
        divSum -= int(root)
    divSum -= num
    return divSum

def main(number):
    sumList = []
    amicable = []
    for i in range(number):
        divSum = divisors(i)
        sumList.append(divSum)
        if divSum < i:
            if sumList[divSum] == i:
                amicable.append(i)
                amicable.append(divSum)
    print(sum(amicable))



main(10000)
