from task2_C import *
from task2_E import *

user_selection = (input('''
Please select a value:
1 - Search with name (First letter)
2 - Search with age
'''))

if user_selection == "1":
    searchName()
elif user_selection == "2":
    searchAge()
else:
    print("You have entered an invalid value!")