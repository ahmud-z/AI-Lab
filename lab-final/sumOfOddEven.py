def findSum(numbers):
    evenSum = 0
    oddSum = 0

    for i in numbers:
        if i % 2 == 0:
            evenSum += i
        else:
            oddSum += i

    print(f"Sum of even elements: {evenSum}\n")
    print(f"Sum of odd elements: {oddSum}")


def main():
    myList = [4, 5, 3, 2, 18]
    print(type(myList))


main()
