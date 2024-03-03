def findFactorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    return fact

def main():
    inputNumber = int(input("Enter a number: "))
    print(f"{inputNumber} factorial is: {findFactorial(inputNumber)}")

main()
