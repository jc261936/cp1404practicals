"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    salary = []
    number_of_months = int(input("How many months? "))

    report_income(number_of_months, salary)

    print_report(number_of_months, salary)


def print_report(number_of_months, salary):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = salary[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def report_income(number_of_months, salary):
    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        salary.append(income)


main()