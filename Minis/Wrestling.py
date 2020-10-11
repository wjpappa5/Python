import os
import csv

# Path to collect data from the Resources folder
path = "/Users/williampappas/Desktop/GitLab/01-Class-Activities/03-Python/3/Activities/08-HW_WrestlingWithFunctions/Resources/WWE-Data-2016.csv"
wrestlerData = os.path.join(path)
def print_percentages(wrestlerData):
            name = str(wrestlerData[0])
            wins = int(wrestlerData[1])
            losses = int(wrestlerData[2])
            draws = int(wrestlerData[3])
            total_matches = wins + losses + draws
            win_percent = (wins / total_matches) * 100
            loss_percent = (losses / total_matches) * 100
            draw_percent = (draws / total_matches) * 100
            if loss_percent > 50:
                type_of_wrestler = "Jobber"
            else:
                type_of_wrestler = "Superstar"
            print(f"Stats for {name}: ")
            print(f"Win Percent: {win_percent}")
            print(f"Loss Percent: {loss_percent}")
            print(f"Draw Percent: {draw_percent}")
            print(f"{name} is a {type_of_wrestler}")
with open(wrestlerData, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    name_to_check = input("What wrestler do you want to look for? ")
    for row in csvreader:
        if(name_to_check == row[0]):
            print_percentages(row)
        
            
