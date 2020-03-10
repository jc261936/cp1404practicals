min_length = 3
password = input("Please enter a password with a minimum of 3 Characters- ")
while len(password) < min_length:
    password = input("Please enter a password with a minimum of 3 Characters- ")
stars = "*" * len(password)
print(stars)