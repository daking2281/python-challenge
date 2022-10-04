import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
date=[]
money=[]
changes=[]
counter=0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvfile)
    print(header)

    for row in csvreader:
        if counter==0: 
            date.append(row[0])
            money.append(int(row[1]))
        else:
            date.append(row[0])
            money.append(int(row[1]))
            difference= int(row[1])- money[counter-1]
            changes.append(difference)
        counter= counter+1
    minimum=min(changes)
    maximum=max(changes)
    max_index= changes.index(maximum)
    min_index= changes.index(minimum)
    max_month= date[max_index+1]
    min_month= date[min_index+1]
months= len(date)
    
   
            

average_pl= round(sum(changes)/(counter-1),2)
total=sum(money)

print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total}")
print(f"Average Change: {average_pl}") 
print(f"Greatest Increase in Profits: {max_month} (${maximum})")
print(f"Greatest Decrease in Profits: {min_month} (${minimum})")

f= open('Financial_Analysis.txt','w')
f.write("Financial Analysis")
f.write('\n')
f.write("---------------------------------")
f.write('\n')
f.write(f"Total Months: {months}")
f.write('\n')
f.write(f"Total: ${total}")
f.write('\n')
f.write(f"Average Change: {average_pl}") 
f.write('\n')
f.write(f"Greatest Increase in Profits: {max_month} (${maximum})")
f.write('\n')
f.write(f"Greatest Decrease in Profits: {min_month} (${minimum})")