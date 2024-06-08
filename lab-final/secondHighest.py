def secondHighest(numbers):
    if len(numbers) == 1:
        return numbers[0]

    return bubbleSort(numbers)[1]


def bubbleSort(data):
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]

    return data


def main():
    numbers = [56, 2, 415, 54, 12, 4, 698, 70, 87]

    print(secondHighest(numbers))


main()
