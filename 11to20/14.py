def collatz(n):
    # Returns the length of the collatz sequence of n
    counter = 0
    while n!=1:
        counter += 1
        if n%2 == 0:
            n = n/2
        else:
            n = n*3+1
    return counter 

def main(n):
    # Prints the length of the longest collatz sequence between 0 and n
    maxSequence = 0
    maxN = 0
    for i in range(1,n+1):
        sequence = collatz(i)
        if sequence > maxSequence:
            maxSequence = sequence
            maxN = i
    print maxSequence
    print maxN

main(1000000)
