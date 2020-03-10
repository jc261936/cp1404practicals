out_file = open("name.txt", 'w')
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is", name)
in_file.close()

in_file = open("numbers.txt", "r")
first = int(in_file.readline())
second = int(in_file.readline())
total = first + second
print(total)
in_file.close()

in_file = open("numbers.txt", "r")
total = 0
for number in in_file:
    numbers = int(number)
    sum += numbers
print(total)
in_file.close()
