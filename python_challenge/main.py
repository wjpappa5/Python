#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:50:57 2020

@author: williampappas
"""
#%%
import os
import csv
path = "/Users/williampappas/Desktop/GitLab/02-Homework/03-Python/02-Case-Assignment/Instructions/PyBank/Resources/budget_data.csv"

bd = os.path.join(path)

month = []
value = []
average = []
maxi = []
mini = []

with open(bd, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    for row in csvreader:
        ref = len(list(csvreader))
        month = str(row[0])
        integer = [int(row[1]) for row in csvreader]
        value = sum(integer)
        average = sum(integer) / ref
        maxi = max(integer)
        mini = min(integer)
        
print(f"Financial Analysis")
print(f"-----------------------------------")
print(f"Total Months: {ref}")
print(f"Total: ${value}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {month} (${maxi})")
print(f"Greatest Decrease in Profits: {month} (${mini})")
     
# %%
output = "/Users/williampappas/Desktop/Python/python_challenge/Resources/Budget.csv"
data = zip(month, value, average, maxi, mini)
output_file = os.path.join(output)
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Total Months", "Net Profit", "Average Change","Greatest Increase in Profits","Greatest Decrease in Profits"])
    writer.writerows(data)
         
