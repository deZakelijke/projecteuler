
def main():
    diagSum = 1
    increment = 2
    lastNumber = 1
    while increment < 1001:
        for i in range(4):
            lastNumber += increment
            diagSum += lastNumber
        increment += 2
    print(diagSum)


main()
