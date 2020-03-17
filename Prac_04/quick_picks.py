import random

AMOUNT = 6
MAX = 45
MIN = 1


def main():
    quick_pick_amount = int(input("How many picks?"))
    # Error check for lower than 0
    while quick_pick_amount < 0:
        print("Incorrect Amount of Picks")
        quick_pick_amount = int(input("How many picks?"))
    number_pick(quick_pick_amount)


def number_pick(quick_pick_amount):
    for i in range(quick_pick_amount):
        quickie = []
        for a in range(AMOUNT):
            pick_range = random.randint(MIN, MAX)
            while pick_range in quickie:
                pick_range = random.randint(MIN, MAX)
            quickie.append(pick_range)
        # Sort Lowest to Highest
        quickie.sort()
        print(quickie)


main()
