#Import dependencies
import os
import csv

#Setup lists etc
candidates = []

#Open file and read header
poll_path = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(poll_path, "r") as poll_csv:
    poll_data = csv.reader(poll_csv, delimiter=",")
    poll_header = next(poll_data)

#Process data
#Get candidate votes
# Other data not required for this purpose
    for pollrow in poll_data:
        candidates.append(pollrow[2])

#List of candidates
candidates_list = list(set(candidates))
#Total votes
total_votes = len(candidates)
#Define dictionary to hold voting numbers
candidate_votes = {"Votes": total_votes}
#Add candidates to dictionary
for candidate in candidates_list:
    candidate_votes[candidate]=0

#Votes for each candidate
#N.B. Results not required by county
#For each vote, retrieve number of votes held in dictionary and advance by one
for candidate in candidates:
    candidate_votes[candidate] = candidate_votes[candidate] + 1

#Calculate percentage


#Print to terminal
print(candidates_list)
print(candidate_votes)
for (cand, votes) in sorted(candidate_votes.items(), key=lambda x: x[1]):
    print(f"{cand}: {votes}")

#Print to text file