def findFactorial(rangeLen):
    term1 = 0
    term2 = 1
    nextTerm = term1 + term2

    print(term1)
    print(term2)

    for i in range(3, rangeLen + 1):
        print(nextTerm)
        term1 = term2
        term2 = nextTerm
        nextTerm = term1 + term2


def main():
    rangeLen = int(input("Enter a number: "))
    findFactorial(rangeLen)


main()
