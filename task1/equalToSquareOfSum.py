# Numbers equal to the square of the sum of its digits:
for i in range(10, 101):
    number = str(i)
    square = (int(number[0]) + int(number[1])) ** 2
    if i == square:
        print(i)