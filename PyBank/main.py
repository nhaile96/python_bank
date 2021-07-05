<<<<<<< HEAD
import os
import csv

pybank_csv = os.path.join("budget_data.csv")

#Create lists 
total_months = []
total_profit = []
month_change = []

#Open csv and read in
with open(pybank_csv) as budget_data:
    
    #Store contents of budget data in csvreader
    csvreader =csv.reader(budget_data,delimiter=",")

    #skip the header
    header=next(csvreader)

    #Iterate through the "rows"
    for row in csvreader:

        #Append total months and total profit over period
        #to their matching lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Iterate through profits to find out the biggest change
    for i in range(len(total_profit)-1):
        #Take difference between two months
        month_change.append(total_profit[i+1]-total_profit[i])
#create variable for max and min values
max_increase = max(month_change)
max_decrease = min(month_change)

#bring together max and min to matching month list and
#index from max and min, adding plus 1 becuase month that 
#changes is the next (+1) month
max_month_increase = month_change.index(max(month_change))+1
max_month_decrease = month_change.index(min(month_change))+1

#Print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")                   #giving two decimal spaces
print(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${(str(max_decrease))})")

#Output file
pybank_summary = ("Financial_Analysis.txt")

with open(pybank_summary,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${(str(max_decrease))})")



=======
import os
import csv

pybank_csv = os.path.join("budget_data.csv")

#Create lists 
total_months = []
total_profit = []
month_change = []

#Open csv and read in
with open(pybank_csv) as budget_data:
    
    #Store contents of budget data in csvreader
    csvreader =csv.reader(budget_data,delimiter=",")

    #skip the header
    header=next(csvreader)

    #Iterate through the "rows"
    for row in csvreader:

        #Append total months and total profit over period
        #to their matching lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Iterate through profits to find out the biggest change
    for i in range(len(total_profit)-1):
        #Take difference between two months
        month_change.append(total_profit[i+1]-total_profit[i])
#create variable for max and min values
max_increase = max(month_change)
max_decrease = min(month_change)

#bring together max and min to matching month list and
#index from max and min, adding plus 1 becuase month that 
#changes is the next (+1) month
max_month_increase = month_change.index(max(month_change))+1
max_month_decrease = month_change.index(min(month_change))+1

#Print data
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")                   #giving two decimal spaces
print(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${(str(max_decrease))})")

#Output file
pybank_summary = ("Financial_Analysis.txt")

with open(pybank_summary,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(month_change)/len(month_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_month_increase]} (${(str(max_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_month_decrease]} (${(str(max_decrease))})")



>>>>>>> d5b03f9ee6d5c1c018a2ce14b9bbf2859d53be0e
