"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a function receives the correct type but an inappropriate value. example;
example = int("James")
print(example)
ValueError: invalid literal for int() with base 10: 'James'
2. When will a ZeroDivisionError occur?
When the second argument in division was a zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if numerator and denominator != 0:
        fraction = numerator / denominator
    else:
        fraction = 0
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
