def numberOfBits(number):
    zeros = 0
    ones = 0

    while number > 0:
        if number & 1 == 1:
            ones += 1
        else:
            zeros += 1
        number = number >> 1

    print("Ones", ones)
    print("Zeros", zeros)


number = int(input("Enter the number: "))
print("Binary representation:", bin(number))
numberOfBits(number)
