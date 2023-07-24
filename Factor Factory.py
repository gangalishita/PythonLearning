number = int(input("Please choose a positive integer: "))

# Checks if the entered number is positive
while number < 0:
    print()
    print("The number you entered isn't positive.")
    number = int(input('Please enter a POSITIVE integer: '))
    print()
# Prints the factors of the number
else:
    print("These are the factors of", str(number), ":")
    factors = ""
    for n in range(1, (number + 1)):
        if number % n == 0:
            print(str(n))
