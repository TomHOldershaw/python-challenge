#PyBank homework

#Import dependencies
import os
import csv

#Set empty lists
months = []
profloss = []
profloss_change = []

#Read in file
data_csv = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(data_csv, "r") as datacsv:
    bankdata = csv.reader(datacsv, delimiter=",")

#Store header row
    header = next(bankdata)

#Read data from file
    for bankrow in bankdata:
        #Read data into arrays
        months.append(bankrow[0])
        profloss.append(int(bankrow[1]))

#Calculations:
#Total number of months in dataset
nummonths = len(months)

#Net total amount of "Profit/Losses"
profloss_total = sum(profloss)

#Changes and averages in "Profit/Losses"
for i in range(len(profloss)-1):
    profloss_change.append(profloss[i+1] - profloss[i])
profloss_change_average = sum(profloss_change)/len(profloss_change)

#Greatest increase in profits
maxprofit = max(profloss)
maxmonth = months[profloss.index(maxprofit)]

#Greatest decrease in profits
maxloss = min(profloss)
minmonth = months[profloss.index(maxloss)]

#Print to terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total months: {nummonths}")
print(f"Total: ${profloss_total}")
print(f"Average Change: ${round(profloss_change_average,2)}")
print(f"Greatest Increase in Profits: {maxmonth} (${maxprofit})")
print(f"Greatest Decrease in Profits: {minmonth} (${maxloss})")

#Export to file
#Open file
output_file = os.path.join("PyBank", "analysis", "analysis.txt")

with open(output_file, "w") as analysis_file:

#Export data
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("------------------------------\n")
    analysis_file.write("Total months: " + str(nummonths) + "\n")
    analysis_file.write("Total: $" + str(profloss_total) + "\n")
    analysis_file.write("Average Change: $" + str(round(profloss_change_average,2)) + "\n")
    analysis_file.write("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxprofit) + ")\n")
    analysis_file.write("Greatest Decrease in Profits: " + minmonth + " ($" + str(maxloss) + ")\n")
