#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:30:27 2020

@author: williampappas
"""


import csv
import os
path = "/Users/williampappas/Desktop/GitLab/01-Class-Activities/03-Python/2/Activities/11-HW_UdemyZip/Resources/web_starter.csv"
output = "/Users/williampappas/Desktop/UDemy.csv"
title = []
price = []
subscriber_count = []
number_of_reviews = []
review_percent = []
course_length = []
csvpath = os.path.join(path)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        title.append(row[1])
        price.append(row[4])
        subscriber_count.append(row[5])
        number_of_reviews.append(row[6])
        percent = round(int(row[6])/int(row[5]),2)
        review_percent.append(percent)
        num_course = row[9].split(" ")
        course_length.append(float(num_course[0]))
data = zip(title, price, subscriber_count,number_of_reviews,review_percent,course_length)
output_file = os.path.join(output)
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Title", "Price", "Subscriber Count","Number of Reviews","Review Percent","Course Length"])
    writer.writerows(data)



