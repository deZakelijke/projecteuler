def main():
    f = open('13.txt')
    totalSum = 0
    for line in f:
        totalSum += int(line[0:-1])
    print totalSum

main()
