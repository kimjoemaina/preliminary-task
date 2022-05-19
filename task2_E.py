# Printing where age is user input
def searchAge():
    infile = open("names.txt", "r")
    age_search = input("Enter age to search:\n")
    for s in infile:
        s = s.strip()
        if s[-1:] == age_search or s[-2:] == age_search:
            print(s)


    
