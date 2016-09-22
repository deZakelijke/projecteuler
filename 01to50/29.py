

# make powers
def powers(a,b):
    powers = []
    for i in range(2,a+1):
        for j in range(2,b+1):
            powers.append(i**j)
    return powers

def quickSort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x[2] < pivot[2]:
                less.append(x)
            if x[2] == pivot[2]:
                equal.append(x)
            if x[2] > pivot[2]:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


def main():
    powerList = powers(100,100)
    newSet = set(powerList)
    #sortedSet = quicksort(newSet)
    print(len(newSet))


main()

