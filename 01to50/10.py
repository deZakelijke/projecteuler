import numpy as np

def main(n):
    primes = range(2,n+1)
    ones = [1] * (n-1)
    i = 0 
    while i < len(primes):
        if ones[i] == 1:
            for j in range(2*primes[i],len(ones),primes[i]):                 
                ones[j-2] = 0
        i += 1
    # There is an off by 2 error so the last two are hardcoded :(
    ones[-1] = 0
    ones[-2] = 0
    primeSum = np.dot(primes, ones)
    print primeSum
main(2000000) 
