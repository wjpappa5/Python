#%%
import os
import csv
path = "/Users/williampappas/Desktop/Python/python_challenge/Resources/budget_data.csv"

bd = os.path.join(path)

Total_Months = 0
Net_Profit = 0
Change = 0
Average_Change = 0
NatChangeList = []
GreatestInc = ["",0]
GreatestDec = ["",999999]

with open(bd, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader)
    first_data = next(csvreader)
    Total_Months = Total_Months + 1  
    Net_Profit = Net_Profit + int(first_data[1])
    previous_data = int(first_data[1])
    for row in csvreader:
        Total_Months = Total_Months + 1
        Net_Profit = Net_Profit + int(row[1])
        Change = int(row[1]) - previous_data
        previous_data = int(row[1])
        NatChangeList.append(Change)
        if Change > GreatestInc[1]:
            GreatestInc[1] = Change
            GreatestInc[0] = row[0]
        if Change < GreatestDec[1]:
            GreatestDec[1] = Change
            GreatestDec[0] = row[0]
        
Average_Change = round(sum(NatChangeList) / len(NatChangeList), 2)

output = (
    "\nFinancial Analysis\n"
    "---------------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Net Profit: ${Net_Profit}\n"
    f"Average Change: ${Average_Change}\n"
    f"Greatest Increase in Profits: {GreatestInc[0]}, ${GreatestInc[1]}\n"
    f"Greatest Decrease in Profits: {GreatestDec[0]}, ${GreatestDec[1]}")
print(output)

file = "/Users/williampappas/Desktop/Python/python_challenge/Analysis/Budget.txt"
filetooutput = os.path.join(file)
with open(file, "w", newline='') as datafile:
    datafile.write(output)


