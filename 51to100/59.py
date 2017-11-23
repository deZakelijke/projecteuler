import sys
import copy
import numpy as np

def read():
    cypher = sys.stdin.readline().split(',')
    cypher = [int(i) for i in cypher]
    return cypher


# Doesn't do a xor shift
def shift_cypher(cy, p, q, r):
    cypher = copy.deepcopy(cy)
    for i in range(0, len(cypher)-3, 3):
        cypher[i] = cypher[i] ^ p
        cypher[i+1] = cypher[i+1] ^ q
        cypher[i+2] = cypher[i+2] ^ r
    m = len(cypher) % 3
    if m == 1:
        cypher[-1] = cypher[-1] ^ p
    if m == 2:
        cypher[-2] = cypher[-2] ^ p
        cypher[-1] = cypher[-1] ^ r
    return cypher

cypher = read()
for i in range(97, 123):
    print(chr(i))
    for j in range(97,123):
        for k in range(97, 123):
            shift = shift_cypher(cypher, i, j, k)
            string = ''.join([chr(l) for l in shift])
            flag = True
            for n in range(32):
                if chr(n) in string:
                    flag = False
                    break
            for n in range(35, 38):
                if chr(n) in string:
                    flag = False
                    break
            for n in range(60, 65):
                if chr(n) in string:
                    flag = False
                    break
            if '~' in string:
                flag = False

            if flag:
                print("\nNext example: ")
                print(string)
                val = 0
                for char in string:
                    val += ord(char)
                print("Sum of characters: %d" %val)
