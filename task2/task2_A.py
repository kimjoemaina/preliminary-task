# Read and print names and age:
def searchName():
    infile = open("task2/names.txt", "r")
    for s in infile:
        s = s.strip()
        print(s)

searchName()
