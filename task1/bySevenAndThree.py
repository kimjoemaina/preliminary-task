#numbers divisible by 7 and 3:
for i in range(1, 101):
    if i % 7 == 0:
        if i % 3 == 0:
            print(i)