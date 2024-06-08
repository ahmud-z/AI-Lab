def findSmallest(numbers):
    smallest = numbers[0]
    for i in numbers:
        if smallest > i:
            smallest = i

    return smallest


def main():
    number = [54, 1, 64, 5, 7, 14]
    print(f"Smallest number is {findSmallest(number)}")


main()
