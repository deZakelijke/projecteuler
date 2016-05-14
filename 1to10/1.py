def main():
    threeList = range(0,1000,3)
    fiveList = range(0,1000,5)
    fifteenList = range(0,1000,15)
    total = sum(threeList)+sum(fiveList)-sum(fifteenList)
    print total
    return total

main()
