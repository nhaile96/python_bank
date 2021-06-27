import os
import csv

#grab data file
election_csv = os.path.join("election_data.csv")

#set initial variables to zero sincce we are counting each one
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open csv file and read it in
with open(election_csv) as election_data:

    #store csv data in csvreader variable and skip header
    csvreader = csv.reader(election_data,delimiter=",")
    header = next(csvreader)

    #start iteration to go through each row
    for row in csvreader:
        #count total votes 
        #counts each row in the set
        total_votes +=1
        #count total votes for each candidate
        if row[2] == "Khan":
            khan_votes +=1
        elif row [2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

#create dictionary to tally candidate votes
candidates = ["Khan","Correy","Li","O'tooley"]
votes= [khan_votes,correy_votes,li_votes,otooley_votes]
#zip or join together candidates dictionary key and total votes
results_dictionary = dict(zip(candidates,votes))
#return winner by using max and get function
key = max(results_dictionary,key=results_dictionary.get)


#calculate percentages
khan_percent= (khan_votes/total_votes)*100
correy_percent= (correy_votes/total_votes)*100
li_percent=(li_votes/total_votes)*100
otooley_percent=(otooley_votes/total_votes)*100

#print summary table of results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#output/export results file
election_summary = os.path.join("Election_Results.txt")
with open(election_summary,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")





