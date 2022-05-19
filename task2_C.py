# Reads a letter from user then prints only the lines where names start with the letter:
def searchName():
    userInput = input("Enter a letter to check names: \n").upper()
    infile = open("names.txt", "r")
    for s in infile:
        if s[:1] == userInput:
            print(s)

searchName()