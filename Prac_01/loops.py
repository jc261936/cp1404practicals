for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star = int(input("How many Stars?: "))
for i in range(star):
    print('*', end=' ')
print()

for i in range(1, star + 1):
    print('*' * i)
print()
