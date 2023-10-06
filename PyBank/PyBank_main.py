# Import the os and csv modules
import os
import csv

# Establish the variable to hold the string of the budget_data csv path
budgetData_csv = os.path.join("Resources", "budget_data_(RP).csv")
#print(budgetData_csv)

# Open the budget_data csv file and read it
with open(budgetData_csv, newline="") as csvFile:
    
    # Get wrapper and store it as a reader using the .reader() function
    budgetData = csv.reader(csvFile, delimiter=",") # use the "," as a delimiter

    # Create variable to hold header and to check file is reading properly
    budgetDataHeader = next(budgetData)
    #print(budgetDataHeader)

    # Create a list to collect the months in each row in the dataset
    months = []

    # Create a list to collect the profit/loss amount of each row in the dataset
    profitLoss = []

    # Use a for loop to read each row of the budgetData csv reader object
    for rows in budgetData:
        
        # Append the month for the row to the months list
        months.append(rows[0])

        # Append the integer value of the profit/loss for the row  to the profitLoss list
        profitLoss.append(int(rows[1]))

    # Calculate the total number of months in the dataset
    totalMonths = len(months)

    # Create a list to collect the profit/loss changes between consecutive rows
    profitLossChange = []

    # Use a for loop to iterate through the profitLoss list
    for amt in range(1, len(profitLoss)):

        # Calculate the profit/loss changes between consecutive rows
        profitLossChange.append((int(profitLoss[amt]) - int(profitLoss[amt-1])))

    # Calculate the average of the profit/loss changes calculated above
    profitLossChangeAvg = sum(profitLossChange) / len(profitLossChange)
    profitLossChangeAvg_round = round(profitLossChangeAvg, 2)

    # Determine the greatest increase in profits (amount and month) during entire period
    greatestProfitAmount = max(profitLossChange)
    greatestProfitMonth = months[profitLossChange.index(max(profitLossChange))+1]
    
    # Determine the greatest decrease in profits (amount and month) during entire period
    greatestLossAmount = min(profitLossChange)
    greatestLossMonth = months[profitLossChange.index(min(profitLossChange))+1]



# Print the output
print("Financail Analysis")

print("-------------------------------------------------------")

print(f"Total Months: {totalMonths}")

print(f"Total: ${sum(profitLoss)}")

print(f"Average Change: ${profitLossChangeAvg_round}")

print(f"Greatest Increase in Profits: {greatestProfitMonth} (${greatestProfitAmount})")

print(f"Greatest Decrease in Profits: {greatestLossMonth} (${greatestLossAmount})")



# Create a text file and write the output of the analysis script (similar to print above)
textFile = open("PyBank_Analysis.txt", "w")

# For the following code, I copied the above output and pasted below replacing "print" with
# "textFile.write" and added the escape character "\n" for new lines after each line
textFile.write("Financial Analysis\n")

textFile.write("---------------------------------------------\n")

textFile.write(f"Total Months: {totalMonths}\n")

textFile.write(f"Total: ${sum(profitLoss)}\n")

textFile.write(f"Average Change: ${profitLossChangeAvg_round}\n")

textFile.write(f"Greatest Increase in Profits: {greatestProfitMonth} (${greatestProfitAmount})\n")

textFile.write(f"Greatest Decrease in Profits: {greatestLossMonth} (${greatestLossAmount})\n")
