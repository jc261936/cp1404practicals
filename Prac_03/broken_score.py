"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """User input for their score and print the result"""
    # score = float(input("Enter score: "))
    # print(score)
    # print(check_score(score))
    """Generates a random score and prints the result"""
    score = random.randint(1, 101)
    print(score)
    print(check_score(score))


def check_score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
