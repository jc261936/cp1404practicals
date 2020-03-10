"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def convert_fahrenheit():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)


def convert_celsius():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32


def main():
    main_menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(main_menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            convert_celsius()
            print("Result: {:.2f} F".format(convert_celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            convert_fahrenheit()
            print("Result: {:.2f} C".format(convert_fahrenheit))
        else:
            print("Invalid option")
        print(main_menu)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
