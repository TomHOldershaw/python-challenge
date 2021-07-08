#PyBank homework

#Import dependencies
import os
import csv

#Set empty lists
months = []
profloss = []

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
profloss_average = sum(profloss)/len(profloss)

#Greatest increase in profits
profits = [profit for profit in profloss if profit > 0]
maxprofit = max(profits)
maxmonth = months[profloss.index(maxprofit)]

#Greatest decrease in profits
losses = [loss for loss in profloss if loss <0]
maxloss = min(losses)
minmonth = months[profloss.index(maxloss)]

#Print to terminal
print(f"Total months: {nummonths}")
print(f"Total: ${profloss_total}")
print(f"Average Change: ${profloss_average}")
print(f"Greatest Increase in Profits: {maxmonth} (${maxprofit}")
print(f"Greatest Decrease in Profits: {minmonth} (${maxloss}")

#Export to file
#Open file

#Export data