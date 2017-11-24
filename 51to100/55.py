import math

def palindrome(n):
    return str(n) == str(n)[::-1]

def lychrel(n):
    for i in range(50):
       if palindrome(n):
           print(n, i)
           return True
       n = n + int(str(n)[::-1]) 
    return False

val = 0
for n in range(1, 10000):
    if lychrel(n):
        val += 1

print(val)

