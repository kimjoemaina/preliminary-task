# Odd numbers divisible by 7 but not 3:
for i in range(1, 101):
    if i % 2 != 0:
        if i % 7 == 0:
            if i % 3 != 0:
                print(i)
