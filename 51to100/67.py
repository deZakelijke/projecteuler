import sys
import numpy as np
import pprint

def read():
    pyramid = [] 
    input_file = sys.stdin.read().split('\n')
    for line in input_file:
        try:
            pyramid.append(list(map(int, line.split(' '))))
        except ValueError:
            continue
    return pyramid


pyramid = read()
print(pyramid)


for i in range(len(pyramid)-1, 0, -1):
    #print(pyramid[i-1])
    for j in range(len(pyramid[i-1])):
        max_val = max(pyramid[i][j], pyramid[i][j+1])
        pyramid[i-1][j] += max_val
    print(pyramid[i-1])

#print(pyramid[-1])
print(pyramid[0][0])

