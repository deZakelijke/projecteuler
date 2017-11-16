# Made by Micha de Groot

import math

def pow_sum(number):
    pow_sum = 0
    while(number):
        number, dec = divmod(number, 1)
        number /= 10
        dec = round(dec*10)
        pow_sum += dec ** 5
    return pow_sum


correct = []

for i in range(2,200000):
    if i == pow_sum(i):
        print(i)
        correct.append(i)

print("Result: %d" %sum(correct))
