# # The Challenge: “The Smart ATM Withdrawal Simulator”
# Simulate a bank transaction checking if a user has enough money.

# 1. Set a fixed variable representing a bank balance, for example: balance = 500.

# 2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).

# 3. If the request is less than or equal to the balance, deduct the amount and print:
# “Withdrawal successful! Remaining balance: RX”.

# 4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.

# 5. Otherwise (else), print: “Declined. Insufficient funds”B

Balance = 500
withdraw_amount = float(input("What is the amount you would like to withdraw:  "))
new_Balance = (withdraw_amount - Balance ) or (withdraw_amount + Balance )

if (withdraw_amount <= Balance ):
    # ( Balance - withdraw_amount ) = new_Balance
    print( f"Withdrawal successful! Remaining balance: R{new_Balance}")
    
elif (withdraw_amount <= 0 ):
    print("Invalid amount. You must withdraw more than R0.")
    
else:
    print("Declined. Insufficient funds.")

        
    
    