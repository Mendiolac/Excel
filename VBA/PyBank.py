
# coding: utf-8

# In[1]:


import os
import csv
from pathlib import Path

filepath = Path("../HW3/budget_data.csv")


# In[2]:


Totals = []
Average = []
value = []
date = []
minimum = 0
maximum = 0
Total = 0
count = 0

with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #data loop
    for row in csvreader:
        count +=1
        Total += int(row[1])
        value.append(int(row[1]))
        date.append(row[0])
        Totals = list(zip(value, date))
        


   
    
    


# In[ ]:


#Average
for i in range((len(value)-1)):
    differenceValue = int((value[i+1] - value[i]))
    Average.append(differenceValue)
    
for i in range(len(Totals) -1):
    if int(Totals[i][0]) >= maximum:
        maximum = int(Totals[i][0])
        greatest_increase = maximum - int(Totals[i-1][0])
        MaxMonth = Totals[i][1]
    elif int(Totals[i][0])<minimum:
        minimum = int(Totals[i][0])
        greatest_decrease = minimum - int(Totals[i-1][0])
        MinMonth = Totals[i][1]
    


# In[ ]:


print("Budget Data")
print("-------------------")
print("Total: $" + str(Total))
print("Total Months: " + str(count))
print("Average Change: " + str((sum(Average)/len(Average))))
print("Greatest Increase in Profits: " + MaxMonth + " $" + str(greatest_increase))
print("Greatest Decrease in Profits: " + MinMonth + " $" + str(greatest_decrease))

