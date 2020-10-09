#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:34:15 2020

@author: williampappas
"""
x = "y"

print("Hello! Welcome to the House of Pies! Please take a look at our menu below: \n")

pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffe", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

pie_purchases = [0,0,0,0,0,0,0,0,0,0]

while x == "y":

    print("-----------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffe, " +
          " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
          "(9) Tamale (10) Steak ")
        
    choice = input("Which pie would you like? ")
    
    pie_purchases[int(choice)-1] = pie_purchases[int(choice)-1] + 1
    
    print("-----------------------------------------------------------------")
    
    print("\nGreat! We'll have the " + pie_list[int(choice) - 1] + " pie right out for you. ")
        
    x= input(f"Would you like us to take another order? (y)es or (n)o? ")
    
    print("-----------------------------------------------------------------")
    
print("\nThank you for you purchase! Your receipt is below: \n")

for pie_index in range(len(pie_list)):
    print(str(pie_purchases[pie_index]) + " " + str(pie_list[pie_index]))


    
    