# -*- coding: UTF-8 -*-
"""
PyBank Homework
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('./Resources/budget_data(2).csv')

# Initialize variable to hold dates, money and rate
date = []
pnl = []
rate = []

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:     
        
        # Set the each fields variable equal to the value in the 'n'th column of each row
        dates = str(row[0])
        pnls = int(row[1])
        rates = int(row[2])
       
        # Append the row the each fields value to the list of date, pl, rate
        date.append(dates)
        pnl.append(pnls)
        rate.append(rates)
    
# Initialize metric variables    
index_max = 0
index_min = 0
cnt = 0
total_months = 0
total_money = 0
avg_sum = 0
greatest_increase = 0
greatest_decrease = 0

# Calculate the total months, total money, average, increase, decrease of the list of budget 
for pnls in pnl:
    total_months += 1
    total_money += pnls
            
for rates in rate:
    avg_sum += rates
    cnt+=1
    if greatest_decrease == 0:
        greatest_decrease = rates
    
    # Logic to determine min and max rates        
    elif rates > greatest_increase:
        greatest_increase = rates
        index_max =cnt
    elif rates < greatest_decrease:
        greatest_decrease = rates
        index_min = cnt

# Calculate the average, round to the nearest 2 decimal places
avg = round(avg_sum/(total_months - 1), 2)


"""
# code chenk with debug 
print("Financial Analysis")
print("----------------------------")
print("Total Months:", total_months
print("Total:", "$", total_money)
print("Average Change:", avg)
print("Greatest Increase in Profits: ", date[index_max],"($",greatest_increase,")", sep="")
print("Greatest Decrease in Profits: ", date[index_min],"($", greatest_decrease,")", sep ="")
"""

#write out report to a text file
many_lines = f"""Total Months: {total_months}
Total: ${total_money}
Average change: {avg}
Greatest Increase in Profits: {date[index_max]}, ${greatest_increase}
Greatest Decrease in Profits: {date[index_min]}, ${greatest_decrease}
"""
# print(many_lines) <----- check many_lines for print code

f = open("PyBank.txt", "w")
f.writelines("Financial Analysis\n----------------------------\n")
f.writelines(many_lines)
f.close()

