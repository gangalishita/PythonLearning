# Welcome message
print("Welcome to the Personalized Message Generator!")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
age = input("Enter your age: ")
integer = input("Enter your integer: ")
favorite_color = input("Enter your favorite color: ")
# Future Age
future_age = int(age) + int(integer)
# Name Length
name_length = len(first_name) + len(last_name)
# Personalized message
print("Hello " + first_name + " " + last_name + "!")
print("Your name is " + str(name_length) + " characters long.")
print("In " + str(integer) + " years, you will be " + str(future_age) + " years old.")
print("Your favorite color is " + favorite_color.upper() + "!")
