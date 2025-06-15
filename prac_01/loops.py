# a. count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. count down from 20 to 1
for p in range(20, 0, -1):
    print(p, end=' ')
print()

# c/d. print n stars and print n lines of increasing stars
number = int(input("Number of Stars: "))

temp = number
while temp >= 1:
    print("*", end='')
    temp -= 1
print()

for i in range(1, number + 1):
    print("*" * i)
