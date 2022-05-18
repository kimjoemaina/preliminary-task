#numbers divisible by 7 and 3:
for i in range(1, 101):
    if i % 7 == 0:
        if i % 3 == 0:
            print(i)

# # numbers divisible by 7 but not 3:
for i in range(1, 101):
    if i % 7 == 0:
        if i % 3 != 0:
            print(i)

# Odd numbers divisibly by 7 but not 3:
for i in range(1, 101):
    if i % 2 != 0:
        if i % 7 == 0:
            if i % 3 != 0:
                print(i)

# Numbers divisibly by the sum of their digits:
for i in range(10, 101):
    number = str(i)
    divisor = int(number[0]) + int(number[1])
    if i % divisor == 0:
        print(i)

# Numbers equal to the square of the sum of its digits:
for i in range(10, 101):
    number = str(i)
    square = (int(number[0]) + int(number[1])) ** 2
    if i == square:
        print(i)