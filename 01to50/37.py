# Made by Micha de Groot

import math

def prime(num):
    if num == 1:
        return False
    limit = int(math.sqrt(num))
    for i in range(2, limit+1):
        if num % i == 0:
            return False
    return True


def truncatable(num):
    num_2 = num
    while(num):
        if not prime(num):
            return False
        num = num // 10

    l = len(str(num_2))
    while(l > 1):
        num_2 = num_2 - ((num_2 // (10**(l-1))) * (10**(l-1)))
        if not prime(num_2):
            return False
        l = len(str(num_2))
    return True

truncs = []
num = 9
while len(truncs) < 11:
    if prime(num):
        if truncatable(num):
            print(num)
            truncs.append(num)
    num += 1

print(truncs)
print("Result: %d" %sum(truncs))

