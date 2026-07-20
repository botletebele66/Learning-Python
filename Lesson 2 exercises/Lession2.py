    # In this LU we are going to learn. How to change a string casting, clean up messy inputs and pull out letters in a string by on its position ( yes it is Arrays) 
    #  1. Basicaly arrays = Tracking individual letters in a string.

name = "BotshelO" # this is a string

print (name [0])
print (name [-1])
print (name [2])

    # If an array is a Negetive the pc will state counting form the left (Botshel O) the O is the array index {-1}.
    # The if Postive it states form the right.

    # ------------------------------------#

    # 2. Using String methods

town = "Welkom"
 
print(town.upper())
print(town.strip())

    # print(town.upper())
    # town.upper() is calling a string method called .upper() on the town variable.
    # What it does: It creates a new string where every letter is converted to UPPERCASE.
    # Important: It does not change the original town variable (strings are "immutable" in Python). It just produces a new result.
    # print() then takes that new uppercase string and displays it on your screen. 

    # print(town.strip())
    # town.strip() is a string method the calls the .strip() in town var
    # This method it removes any spaces ( they call it Whitespace )
    # then prints 

    # Creating a proffessional system email generator
    
FirstName = input(" Please enter your  first name : ").strip()
Surname = input("Please enter your surname : ").strip

username = f"{FirstName[0]} {Surname}"
print (f"your email is: {username.upper()}@unversity.co.za")

