# Read and print names and age:
def searchName():
    infile = open("names.txt", "r")
    for s in infile:
        print(s)

searchName()
