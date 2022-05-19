# Print only lines where the name starts with "A"
def searchName():
    infile = open("names.txt", "r")
    for s in infile:
        if s[:1] == "A":
            print(s)

searchName()