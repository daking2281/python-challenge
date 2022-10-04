from audioop import avg
from enum import unique
import os
import csv
#import CVS file as variable csvpath
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
election_print=("Election Results")
print(election_print)
#define variables and blank lists
votes=[]
candidates=[]
cand_list=[]
vote_count={}
percentage=[]
vote=0
#open csv
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvfile)
    #loop through each row
    for row in csvreader:
        votes.append(row[0])
        #create a unique list of candidates and create a dictionary containing the amount of votes per candidate (key=Candidate name, Value= Total Votes)
        if row[2] not in cand_list:
            cand_list.append(row[2])
            vote_count[row[2]]=0
        vote_count[row[2]] +=1
    total_votes=sum(vote_count.values())
    total=(f"Total Votes: {total_votes}")
    print(total)

    #loop through the keys and values of the created dictionary and printing desired output
    for key, value in vote_count.items():
       percents=round((value/sum(vote_count.values()))*100,3)
       percentage.append(percents)
       print(key, ':', value, ',', percents,"%")
       

    #Find the max amount of votes
    max= max(vote_count.values())

    #create a list of keys and values
    key_list= list(vote_count.keys())
    value_count= list(vote_count.values())

    #identify the index of the created list where it equals the maximum votes
    winner= value_count.index(max)
    
    #using the index from the values to find the name of the Winner
    Win=(f"winner: ***{key_list[winner]}***")
    print(Win)
f= open ("Election_Results.txt",'w')
f.write("Election Results")
f.write('\n')
f.write("---------------------------------")
f.write('\n')
f.write(f"Total Months: {total_votes}")
f.write('\n')
f.write("---------------------------------")
f.write('\n')
for key, value in vote_count.items():
       percents=round((value/sum(vote_count.values()))*100,3)
       percentage.append(percents)
       f.write(f'{key}:{value}, {percents}%\n')
f.write("---------------------------------")
f.write('\n')
f.write(f"{Win}")
f.write('\n')
f.write("---------------------------------")

