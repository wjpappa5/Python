#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 10:41:45 2020

@author: williampappas
"""


import csv
import os
path = "/Users/williampappas/Desktop/GitLab/01-Class-Activities/03-Python/3/Activities/01-Stu_CerealCleaner/Resources/cereal_bonus.csv"
csvpath = os.path.join(path)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        if float(row[7]) >= 5:
            print(row[0])
            
            
        

