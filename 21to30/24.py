from operator import itemgetter

permList = []

# prints all permutations of array
# n must be len(array)
def perm(n, array):
    if n == 1:
        temp = combine(array)
        permList.append(temp)

    else:
        for i in range(n-1):
            perm(n-1, array)
            if n%2 == 0:
                array[i] = array[i] ^ array[n-1]
                array[n-1] = array[i] ^ array[n-1]
                array[i] = array[i] ^ array[n-1]
            else:
                array[0] = array[0] ^ array[n-1]
                array[n-1] = array[0] ^ array[n-1]
                array[0] = array[0] ^ array[n-1]
        perm(n-1, array)

def combine(array):
    number = 0
    for i in range(len(array)):
        number += array[-(i+1)] * 10 ** (i)
    return number

array = [0,1,2,3,4,5,6,7,8,9]
n = len(array)
perm(n,array)
permList = sorted(permList)
print(permList[999999])


