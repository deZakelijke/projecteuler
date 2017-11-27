import math

def palindrome(n):
    return int(str(n)) == int(str(n)[::-1])

def lychrel(n):
    for i in range(50):
       n = n + int(str(n)[::-1]) 
       if palindrome(n):
           return False
    return True

val = 0
for n in range(10000):
    if lychrel(n):
        val += 1

print(val)

