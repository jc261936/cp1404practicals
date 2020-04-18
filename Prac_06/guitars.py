from Prac_06.guitar import Guitar


def main():
    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    exit = "Q"
    name = input("Enter Name of guitar or Enter 'Q' to quit: ")
    while name != exit:
        year = int(input("Year: "))
        price = float(input("Cost: $"))
        add_guitar = Guitar(name, year, price)
        guitars.append(add_guitar)
        print(add_guitar, "added.")
        name = input("Enter Name of guitar or Enter 'Q' to quit: ")

    if guitars:
        guitars.sort()
        for g, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(vintage)"
            print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}{2}".format(g + 1, guitar, vintage))
    else:
        print("Ukulele doesn't count!")


main()