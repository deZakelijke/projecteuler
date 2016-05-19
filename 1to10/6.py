def sumOfSquares(n):
    sum = 0
    for i in range(0,n+1):
        sum += i**2
    return sum

def squareOfSum(n):
    square = sum(range(0 ,n+1)) ** 2
    return square

def main():
    n = 100
    diff = abs(squareOfSum(n)-sumOfSquares(n))
    print diff

main()  
