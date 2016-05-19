import sys

def listProduct(l):
    p = 1
    for i in range(0,len(l)):
        p *= int(l[i])
    return p 

def main(num):
    numString = str(num)
    maxProduct = 0
    productlength = 13
    # Iterate through the string of numbers and calc the product
    for i in range(0,len(numString)-productlength):
        product = listProduct(numString[i:i+productlength])
        if maxProduct < product:
            maxProduct = product
    print maxProduct 

main(sys.argv[1])
