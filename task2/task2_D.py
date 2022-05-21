# Printing where age = 5
def searchAge():
    infile = open("task2/names.txt", "r")
    for s in infile:
        s = s.strip()
        if s[-1] == "5":
            print(s)

searchAge()
