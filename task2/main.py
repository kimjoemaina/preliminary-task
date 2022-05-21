from task2_C import *
from task2_E import *

print('''
1 - Search with name (First letter)
2 - Search with age
''')

user_selection = input("Please select a value:")

if __name__ == "__main__":
    if user_selection == "1":
        searchName()
    elif user_selection == "2":
        searchAge()
    else:
        print("You have entered an invalid value!")
