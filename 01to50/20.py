import math

def main(n):
    number = math.factorial(n)
    s = 0
    while number:
        s +=number%10
        number //= 10
    print(s)

main(100)
