def main():
    # Create fibbonachi sequence
    first = 1
    second = 1
    sumOfEvens = 0
    temp = 0
    count = 2
    # Loop till' four million
    while second < 4000000:
        count += 1
        temp = first + second 
        first = second
        second = temp
        # Every third fibbonachi number is even
        if count%3 ==0:
            sumOfEvens +=second
    print sumOfEvens

main()
