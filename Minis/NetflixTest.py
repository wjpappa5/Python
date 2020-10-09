# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

title = input("Which movie are you looking for? ")
found = True
    
import os
import csv
path = "/Users/williampappas/Desktop/netflix_ratings.csv"
csvpath = os.path.join(path)
found = False
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
       if row[0] == title: 
        print(f"\nThe {title} is currently rated {row[1]} {row[2]} (the current user rating is {row[5]}). ")
        found = True
        break
    if found == False:
        print("\nSorry! We couldn't find that title.")

        
        