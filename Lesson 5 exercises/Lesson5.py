# This lesson is about loops while loops and for loops 
# A while loop is a continuous if statements that gose on and on until a certain condition is met.          

# the countdown using a while loop

count = 20

while count > 0 :
    print( count )
    count = count - 1
    
print("Blast off !!! ")
    

# This is a for loop this is used when you know when the exact number that is need for the program to stop.
for rep in range(1, 2020 ):
    print( f" This is the rep no. {rep} ") 
    
    
print( "Reps are complete when done")

# I wll be combinin loops with basic if statements.
# A guessing game 

secret_word  = "python"

while True:
    guess = input("Guess the  programming languge we are using : ").lower()


    if (guess == secret_word):
        print("You got the correct languge !!!")
        break 
    
    else:
        print("Please try again !! ")
    


