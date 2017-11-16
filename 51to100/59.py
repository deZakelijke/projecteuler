import sys
import copy

def read():
    cypher = sys.stdin.readline().split(',')
    cypher = [int(i) for i in cypher]
    return cypher


def shift_cypher(cy, p, q, r):
    cypher = copy.deepcopy(cy)
    for i in range(0, len(cypher)-3, 3):
        cypher[i] += p
        cypher[i+1] += q
        cypher[i+2] += r
    m = len(cypher) % 3
    if m == 1:
        cypher[-1] += p
    if m == 2:
        cypher[-2] += p
        cypher[-1] += r
    return cypher

cypher = read()
for i in range(1,26):
    print(i)
    for j in range(1,26):
        for k in range(1,26):
            shift = shift_cypher(cypher, i, j, k)
            string = ''.join([chr(l) for l in shift])
            flag = True
            for n in range(30):
                if chr(n) in string:
                    flag = False
                    break
            if flag:
                print("\nNext example: ")
                print(string)
