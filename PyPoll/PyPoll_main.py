# Import the python csv and os modules
import csv
import os

# Establish the variable to hold the string of the election_data csv path
pollData_csv = os.path.join("Resources", "election_data_(RP).csv")
#print(pollData_csv)

# Open the pollData_csv file and read it with each row be a new line
with open(pollData_csv, newline="") as csvFile:
    
    # Get wrapper and store it as a reader using the .reader() function
    pollData = csv.reader(csvFile, delimiter=",") # use the "," as a delimiter

    # Create variable to hold header and to check file is reading properly
    pollDataHeader = next(pollData)
    #print(pollDataHeader)

    # Create list to collect the ballot ID (votes)
    votes = []

    # Create list to collect the counties where votes were cast
    county = []
    
    # Create list to collect the candidates who received votes
    candidates = []

    # Create lists to collect the voting instances per candidate
    CharlesCasperStockham = []
    DianaDeGette = []
    RaymonAnthonyDoane = []

    # Create the vote counters for each candidate and initialize them at 0
    CharlesCasperStockhamVotes = 0
    DianaDeGetteVotes = 0
    RaymonAnthonyDoaneVotes = 0

    # Use a for loop to read the vote, county, and candidate information of each row in dataset
    for rows in pollData:
        
        # Append the votes list based on Ballot ID column and convert to integer
        votes.append(int(rows[0]))

        # Append the county list based on the County column
        county.append(rows[1])

        # Append the candidates list based on the Candidate column
        candidates.append(rows[2])

    # Determine the total votes by using len() function on votes list
    totalVotes = len(votes)
    #print(totalVotes)

    # Use a for loop with a nested conditional statement to determine the total votes won per candidate
    for candidate in candidates:
        # Use a condition checking if Charles is the current candidate in the loop
        if candidate == "Charles Casper Stockham":
            # Then append Charles' voting instance list with result
            CharlesCasperStockham.append(candidates)
            # Update Charles' total vote count using len() function to Charles' voting instance list
            CharlesCasperStockhamVotes = len(CharlesCasperStockham)

        elif candidate == "Diana DeGette":
            # Then append Diana's voting instance list with result
            DianaDeGette.append(candidates)
            # Update Diana's total vote count using len() function to Diana's voting instance list
            DianaDeGetteVotes = len(DianaDeGette)

        else:
            # Append Raymon's voting instance list with result
            RaymonAnthonyDoane.append(candidates)
            # Update Raymon's total vote count using len() function to Raymon's voting instance list
            RaymonAnthonyDoaneVotes = len(RaymonAnthonyDoane)

    #print(CharlesCasperStockhamVotes)
    #print(DianaDeGetteVotes)
    #print(RaymonAnthonyDoaneVotes)

    # Calculate the percentages of votes each candidate won using total votes won per candidate
    # divided by the total votes; format to 3 decimal places
    CharlesCasperStockhamPct = round(((CharlesCasperStockhamVotes / totalVotes) * 100), 3)
    DianaDeGettePct = round(((DianaDeGetteVotes / totalVotes) * 100), 3)
    RaymonAnthonyDoanePct = round(((RaymonAnthonyDoaneVotes / totalVotes) * 100), 3)

    #print(CharlesCasperStockhamPct)
    #print(DianaDeGettePct)
    #print(RaymonAnthonyDoanePct)

    # Use a conditional statement comparing the total votes per candidate using the max()
    if CharlesCasperStockhamVotes > max(DianaDeGetteVotes, RaymonAnthonyDoaneVotes):
        winner = "Charles Casper Stockham"
    elif DianaDeGetteVotes > max(CharlesCasperStockhamVotes, RaymonAnthonyDoaneVotes):
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
    
    #print(winner)



# Print the output
print("Election Results")

print("-------------------------------------------------------")

print(f"Total Votes: {totalVotes}")

print("-------------------------------------------------------")

print(f"Charles Casper Stockham: {CharlesCasperStockhamPct}% ({CharlesCasperStockhamVotes})")

print(f"Diana DeGette: {DianaDeGettePct}% ({DianaDeGetteVotes})")

print(f"Raymon Anthony Doane: {RaymonAnthonyDoanePct}% ({RaymonAnthonyDoaneVotes})")

print("-------------------------------------------------------")

print(f"Winner: {winner}")

print("-------------------------------------------------------")



# Create a text file and write the output of the analysis script (similar to print above)
textFile = open("PyPoll_Analysis.txt", "w")

# For the following code, copied the above output and pasted below replacing "print" with
# "textFile.write" and added the escape character "\n" for new lines after each line
textFile.write("Election Results\n")

textFile.write("-------------------------------------------------------\n")

textFile.write(f"Total Votes: {totalVotes}\n")

textFile.write("-------------------------------------------------------\n")

textFile.write(f"Charles Casper Stockham: {CharlesCasperStockhamPct}% ({CharlesCasperStockhamVotes})\n")

textFile.write(f"Diana DeGette: {DianaDeGettePct}% ({DianaDeGetteVotes})\n")

textFile.write(f"Raymon Anthony Doane: {RaymonAnthonyDoanePct}% ({RaymonAnthonyDoaneVotes})\n")

textFile.write("-------------------------------------------------------\n")

textFile.write(f"Winner: {winner}\n")

textFile.write("-------------------------------------------------------\n")