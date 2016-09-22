def main():
    for a in range(0, 1000):
        for b in range(0, 1000):
            c = 1000 - a - b
            if c ** 2 == a ** 2 + b ** 2:
                print 'a: ', a, 'b: ', b, 'c: ', c
                print a*b*c
    
main()
