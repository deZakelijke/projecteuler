import math

def factor(number):
    # This code should return two prime factors of 'number'
    a = math.ceil(number ** 0.5)
    b2 = a**2 - number
    b = b2 ** 0.5
    while not b.is_integer():
        a += 1
        b2 = a**2 - number
        b = b2 ** 0.5
    # returns first the smalles, then the biggest
    return ((a-b),(a+b))

def main():
    # Returns the smalles and biggest prime factor of number
    number = 600851475143
    factors = []
    temp = []
    a,b = factor(number)
    temp.append(a) 
    temp.append(b)
    while len(temp) > 0:
        fact1, fact2 = factor(temp[0])
        del temp[0]
        if fact1 == 1:
            factors.append(fact2)
        else:
            temp.append(fact1)
            temp.append(fact2)
    factors = sorted(factors)
    print factors[-1]

main()
