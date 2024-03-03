def findFibonacci(n):
    term1 = 0
    term2 = 1

    print(term1)
    print(term2)

    while True:
        nextTerm = term1 + term2
        if nextTerm <= n:
            print(nextTerm)
            term1 = term2
            term2 = nextTerm
        else:
            break


findFibonacci(55)
