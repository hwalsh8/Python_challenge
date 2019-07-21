#import modules
import csv
import os

#declare variables
total_votes = 0
candidates = []
cand_votes = {}

#list for county and candidate
election_data = ["1", "2"]

#create a path for data, sample of 10,000 for git repo upload
election_data = os.path.join("Resources", "election_data_sample.csv")

#open the file
with open(election_data) as pypoll_data:
    reader = csv.reader(pypoll_data)
    #skip header
    header = next(reader)
    # print(header) <-print to check
    
     #read results
    for current_row in reader:
        #grab total vote count
        total_votes = total_votes + 1
        #candidate choice
        candidate = current_row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            cand_votes[candidate] = 0
            # print(cand_votes)
        
        cand_votes[candidate] = cand_votes[candidate] + 1
    # print(cand_votes)
    # print(candidate)
    print("Election Results")
    print("-----------------------")
    print("Total Votes: "+str(total_votes))
    print("-----------------------")

    #Calculate winning candidate and produce list of all candidate counts and percentage of vote totals
    winning_count = 0
    winning_candidate = ""

    for candidate1 in cand_votes:
        votes = cand_votes.get(candidate1)
        votes_percentage = float(votes)/float(total_votes) * 100
        # print(votes)
        # print(votes_percentage)

        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate1

        #print tally of candidates, votes and percentage of votes
        voter_output = f"{candidate1}: ({votes}) {votes_percentage:.3f}%\n"
        print(voter_output)
            
print("-----------------------")
print("Winner: " + str(winning_candidate))
print("-----------------------")
print("end session")