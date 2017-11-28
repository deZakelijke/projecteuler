import sys
import math


def check_digits(n,m):
    n= str(n)
    m = str(m)
    for digit in n:
        if not digit in m:
            return False
    for digit in m:
        if not digit in n:
            return False
    return True

number = 1
flag = False
while(not flag):
    flag = False
    number +=1
    for i in range(2,7):
        flag = check_digits(number,number*i)
        if not flag: break
    

print(number)

