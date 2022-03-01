import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%&*()*+'

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

password = ""
for _ in range(number_of_letters):
    password += random.choice(letters)
for _ in range(number_of_symbols):
    password += random.choice(symbols)
for _ in range(number_of_numbers):
    password += random.choice(numbers)

# generating Easy Password
easy_password = password
print(password)

# generating Hard Password
password = list(password)
random.shuffle(password)
generated_password = ""
for letter in password:
    generated_password += letter
print("Here is your password:", generated_password)
