def findDivisible(n):
    for i in range(n + 1):
        if i % 5 == 0:
            print(f"{i} ", end="")


def main():

    n = int(input("Enter the value of n: "))
    print("Calculated Series: ")
    findDivisible(n)


main()
