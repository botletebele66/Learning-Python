# Practical Task
 
# Task Overview
# Username and Message Formatter
# Write a Python script called string_formatter.py that takes a user’s first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.

# Requirements
# Collect first name, last name, and bio message using input()
# Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)
# Display the full name in Title Case using .title()
# Strip leading/trailing whitespace from the bio before displaying it using .strip()
# Count and display the number of characters in the bio using len()
# Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()
# Display all output using f-strings
 

# Outcome of Task
# At the end of this task, you should be competent in creating and running a Python script that accepts user input, manipulates and formats strings using key string methods, creates usernames through string concatenation, counts characters using len(), and displays clean, formatted output using f-strings.

FirstName = input("Please enter your first name: ")
LastName = input("Please enter your last name: ")
Bio_message = input("Please enter your short bio message: ")

# 1. Create username: first initial + last name in lowercase
username = (FirstName[0] + LastName).lower()

# 2. Full name in Title Case - apply .title() to the combined string
full_name_title = (FirstName + " " + LastName).title()

# 3. Strip leading/trailing whitespace from bio
stripped_bio = Bio_message.strip()

# 4. Count characters in the stripped bio
bio_length = len(stripped_bio)

# 5. Replace "I am" with "I'm" in the stripped bio
replaced_bio = stripped_bio.replace("I am", "I'm")

# Display all outputs using f-strings
print("\n--- User Profile ---")
print(f"Username: {username}")
print(f"Full Name (Title Case): {full_name_title}")
print(f"Bio (stripped): {stripped_bio}")
print(f"Bio character count: {bio_length}")
print(f"Bio with contractions: {replaced_bio}")



# Step‑by‑Step Process )
# 1. Getting the user’s input
# The program asks the user for three pieces of information: their first name, their last name, and a short bio message. It waits for the user to type each one and press Enter.

# 2. Creating a username
# The program builds a username by taking just the very first letter of the first name and joining it directly to the full last name. It then converts the whole result to lowercase letters.
# For example: First name “Thabo” + last name “Dlamini” becomes “tdlamini”.

# 3. Formatting the full name
# The program combines the first and last names with a space in between, then capitalises the first letter of each part (making all other letters lowercase). This ensures the name always appears properly capitalised, no matter how the user typed it.

# 4. Cleaning up the bio message
# The bio text often has accidental extra spaces at the beginning or end (e.g., from the user pressing the space bar). The program trims away all those leading and trailing spaces so that the bio is neat and tidy.

# 5. Counting the characters in the bio
# After trimming the extra spaces, the program counts how many characters (letters, numbers, punctuation, and spaces between words) are left in the bio. This gives an accurate length that isn’t inflated by stray spaces.

# 6. Replacing a common phrase
# The program looks through the cleaned‑up bio and finds every occurrence of the exact phrase “I am” (with a capital I and a space). It changes those to the contracted form “I’m”. This is a typical text‑normalisation step to make the bio sound more natural.

# 7. Displaying the final profile
# Finally, the program prints out all the results in a neat, titled block. It shows:
