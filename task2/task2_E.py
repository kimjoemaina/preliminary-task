# Printing where age is user input
def searchAge():
    infile = open("task2/names.txt", "r")
    age_search = input("Enter age to search:\n")
    for s in infile:
        s = s.strip()
        if s[-1:] == age_search:
            print(s)
        elif s[-2:] == age_search:
            print(s)

if __name__ == "__main__":
    searchAge()

# split 