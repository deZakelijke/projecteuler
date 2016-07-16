# Takes an int and returns all divisors of int as a list
import math

def divisors(num):
    div = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num%i == 0:
            div += 2
    return div

def main():
    triangleSum = 0
    div = 0
    i = 1
    while div < 501:
        triangleSum += i
        div = divisors(triangleSum)
        if div > 500:
            print(triangleSum)
        i +=1

main()
