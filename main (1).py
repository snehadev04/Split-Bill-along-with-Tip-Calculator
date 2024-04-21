# Print a welcome message
print("Welcome to the tip calculator")

# Ask user for the total bill amount and convert it to float
total_bill = float(input("What is the total bill?\n $"))

# Ask user for the tip percentage they want to add and convert it to integer
tip_percentage = int(input("What percentage of tip would you like to add to the bill? (10, 12, 15)\n"))

# Ask user for the number of people splitting the bill and convert it to integer
number_of_people_splitting = int(input("Number of people splitting the bill?\n"))

# Calculate the complete bill including tip
complete_bill = float(tip_percentage / 100 * total_bill + total_bill)

# Calculate the bill amount for each person
bill_split = round(complete_bill / number_of_people_splitting, 2)

# Format the bill split to display 2 decimal places
dec = "{:.2f}".format(bill_split)

# Print the total bill for each person
print(f"The total bill for each person is ${dec}")
