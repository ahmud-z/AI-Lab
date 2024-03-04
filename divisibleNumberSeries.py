def findDivisible(n, divisibleNumber):
    for i in range(n + 1):
        if i % divisibleNumber == 0:
            print(f"{i} ", end="")

def main():

    n = int(input("Enter the value of n: "))
    divNumber = int(input("Enter a number to divide: "))

    print("Calculated Series: ")
    findDivisible(n, divNumber)

main()
