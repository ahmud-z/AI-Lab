# Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and
# not divisible by 5.

def main():
    sum = 0
    for i in range(50, 100 + 1):
        if i % 3 == 0 and i % 5 != 0:
            sum += i
    print("Result: " + str(sum))

main()
