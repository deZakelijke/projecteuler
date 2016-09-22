# use the fact that there is a correlation between the number of possibilities and the pyramid of pascal
import numpy as np


def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return line

def main(n):
    pascalRow = np.array(pascal(n))
    possibilities = sum(pascalRow*pascalRow)
    print(possibilities)

main(20)
