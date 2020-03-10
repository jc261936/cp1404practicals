def main():
    password = get_password()
    make_asterisks(password)


def make_asterisks(password):
    stars = "*" * len(password)
    print(stars)


def get_password():
    min_length = 3
    password = input("Please enter a password with a minimum of 3 Characters- ")
    while len(password) < min_length:
        password = input("Please enter a password with a minimum of 3 Characters- ")
    return password


main()