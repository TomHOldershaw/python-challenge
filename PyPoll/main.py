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
#Define dictionary to hold voting numbers
for candidate in candidates_list:
    candidate_votes = {candidate: 0}

#Total votes
total_votes = len(candidates)

#Votes for each candidate
#N.B. Results not required by county
#For each vote, retrieve number of votes held in dictionary and advance by one
for candidate in candidates:
    candidate_votes[candidate] = candidate_votes[candidate] + 1

#Calculate results

#Print to terminal

#Print to text file