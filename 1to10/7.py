# Is a brute force method, do not use for anything else
def main(n):
    primes = [2,3]
    # We start at five, because sqrt(5) > 2
    integer  = 5
    while len(primes) < n:
        root = integer ** 0.5
        for i in range(len(primes)):
            # Only search untill the root of the integer
            if primes[i] <= root:
                if integer%primes[i] == 0:
                    break
        else:
            primes.append(integer)
        integer += 2
    print len(primes)
    print primes[-1]

main(10001) 
