#import modules
import csv
import os

#declare variables
total_votes = 0
candidates = []
cand_votes = []

#list for county and candidate
election_data = ["1", "2"]

#create a path for data
election_data = os.path.join("Resources", "election_data.csv")

#open the file
with open(election_data) as pypoll_data:
    reader = csv.reader(pypoll_data)
    #skip header
    header = next(reader)
    #print(header) <-print to check
    
     #read results
    for current_row in reader:
        #grab total vote count
        total_votes = total_votes + 1
        #candidate choice
        candidate = current_row[2]
        
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            cand_votes[candidate_index] = cand_votes[candidate_index] + 1
            
        else:
            candidates.append(candidate)
            cand_votes.append(1)
            #print(cand_votes) <- calulation check
            


#printing Election Results for file
print("Election Results")
print("-----------------------")
print("Total Votes: "+str(total_votes))
candidate_total = [candidates, cand_votes]
for totals in zip(*candidate_total):
    print(*totals)
print("-----------------------")
print("end session")