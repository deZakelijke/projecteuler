def oneToNine(n):
    numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    return len(numbers[n])

def tens(n):
    tens = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
    return len(tens[n])

def tenAndMore(n):
    tens = {1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
    return len(tens[n])

def main(n):
    # will print the number of letters in all ints between 1 and n combined
    # Will probably not work for n > 1000
    sumOfLetters = 0
    for i in range(1,n+1):
        stringI = str(i)
        # add the letters of the 4th digit and if necessary 'and'
        if len(stringI) == 4:
            sumOfLetters += oneToNine(int(stringI[0]))
            sumOfLetters += len('thousand')
            # chop the 4th digit and remove 3rd digit if it is 0
            stringI = str(int(stringI[1:]))
            if int(stringI) != 0:
                sumOfLetters += len('and')
        if len(stringI) == 3:
            sumOfLetters += oneToNine(int(stringI[0]))
            sumOfLetters += len('hundred')
            # chop the 3rd digit and remove 2nd digit if it is 0
            stringI = str(int(stringI[1:]))
            if int(stringI) != 0:
                sumOfLetters += len('and')
        if len(stringI) == 2:
            # check for the special case between 10 and 20 
            if int(stringI[0]) == 1 and int(stringI[1]) !=0:
                sumOfLetters += tenAndMore(int(stringI[1]))
                stringI = []
            else:
                sumOfLetters += tens(int(stringI[0]))
                stringI = stringI[1]
        if len(stringI) == 1 and int(stringI) != 0:
            sumOfLetters += oneToNine(int(stringI[0]))
        print(i)
    print(sumOfLetters)

main(1000)
             
