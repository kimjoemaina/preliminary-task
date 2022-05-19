# Printing where age = 5
def searchAge():
    infile = open("names.txt", "r")
    for s in infile:
        if s[-2] == "5":
            print(s)

searchAge()


