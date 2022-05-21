# Numbers divisible by the sum of their digits:
for i in range(1, 101):
    number = i % 10
    divisor = i // 10
    sum = number + divisor
    if i % sum == 0:
        print(i)
