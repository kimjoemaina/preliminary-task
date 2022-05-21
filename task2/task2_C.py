# Reads a letter from user then prints only the lines where names start with the letter:
def searchName():
    userInput = input("Enter a letter to check names: \n").upper()
    infile = open("task2/names.txt", "r")
    for s in infile:
        s = s.strip()
        if s[0] == userInput:
            print(s)

if __name__ == "__main__":
    searchName()