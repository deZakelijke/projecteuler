def main():
    palindromeMax = 0
    for i in range(1000, 0,-1):
        for j in range(1000,0,-1):
            palindrome = i*j
            if str(palindrome) == str(palindrome)[::-1] and palindrome > palindromeMax:
                palindromeMax = palindrome
    print palindromeMax

main()
