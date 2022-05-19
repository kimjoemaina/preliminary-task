# Print only lines where the name starts with "A"
def searchName():
    infile = open("names.txt", "r")
    for s in infile:
        s= s.strip()
        if s[0] == "A":
            print(s)

searchName()