# The Challenge: “The South African Fuel Cost Calculator”
# With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:

# 1. Ask the user how many kilometers they want to drive.

# 2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).

# 3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
# (Formula: liters_needed = kilometers / 10).

# 4. Calculate the total cost (liters_needed * petrol_price).

# 5. Use type casting to ensure your numbers work, and use round() to format the
# final cost to 2 decimal places.
 
        # Me and you are goinng to make a Fual gas calculator.
 
        # ---
 
kilometers = (float(input("How many kilometers will you be driving today? : Km ")))
petrol_price = (float(input("What is the current petrol price per liter? : R ")))

# if kilometers and petrol_price == str :
#  print("Invalid input. Please enter numeric values.")


liters_needed = kilometers / 10
total_cost = (liters_needed * petrol_price)

print(f"The final cost for your petrol is : R {round(total_cost, 2)}")

# print(round(num1 + num2, 2.00))


# Ask the user for the distance and petrol price 
kilometers = float(input("Enter the number of kilometers you want to drive: ")) 
petrol_price = float(input("Enter the current petrol price per liter (R): ")) 
# Calculate liters needed 
liters_needed = kilometers / 10 
# Calculate total cost 
total_cost = liters_needed * petrol_price 
# Display the results 
print(f"nKilometers to drive: {kilometers} km") 
print(f"Petrol price: R{petrol_price}") 
print(f"Liters needed: {round(liters_needed, 2)} L") 
print(f"Total fuel cost: R{round(total_cost, 2)}")






 
 

 
 
 