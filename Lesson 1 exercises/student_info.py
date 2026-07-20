# This program must collect personal information from the user and displays it in a formatted profile card.
# Thses are declaration the beginning
from unicodedata import name


FirstName = input("Please enter you First name :")
Surname = input("Please enter your Surname :")
Age = int(input("Please enter your age :")) # this must be in INT
FavouriteNumber = float(input("Please enter your favourite number :")) # this should also be a float

# The beginning of the program the Display is the "PRINT"
print ( f"Greetings {FirstName} {Surname}, hope you are doing well"  )
print(f" Welcome, {FirstName} {Surname}")

# If you want to get the name from the user, you can do:
#print("Uppercase:", name.upper())
#print("Title Case:", name.title())


full_name = FirstName + " " + Surname
print(f"Uppercase: {full_name.upper()}")
print(f"Title Case: {full_name.title()}")

# Additional calculations and formatting 
age_in_months = Age * 12
rounded_fav = round(FavouriteNumber , 2)

#  Display data types 
print(" Data Types ")
print(f"Type of first_name: {type(FirstName)}")
print(f"Type of surname:    {type(Surname)}")
print(f"Type of age:        {type(Age)}")
print(f"Type of favourite_number: {type(FavouriteNumber)}")