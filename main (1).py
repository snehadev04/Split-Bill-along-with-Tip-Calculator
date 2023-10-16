
print("welcome to the tip calculator")
total_bill = float(input("what is the total bill?\n $"))
tip_percentage = int(input("what percentage of tip would you like to add to the bill 10, 12, 15?\n"))
number_of_people_splitting = int(input("number of people splitting the bill?\n"))
complete_bill = float(tip_percentage/100*total_bill+total_bill)
bill_split = round(complete_bill/number_of_people_splitting, 2)
dec = "{:.2f}".format(bill_split)
print(f"the total bill for each person is ${dec}")