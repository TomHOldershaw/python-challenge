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

#Sort by votes
sorted_candidates = sorted(candidate_votes.items(), key=lambda x: x[1])

#write output
output = "Election Results\n"
output = output + "--------------------\n"
output = output + "Total Votes: " + str(total_votes) + "\n"
output = output + "--------------------\n"
for (cand, votes) in sorted_candidates:
    output = output + cand +": " + str(round(votes/total_votes,4)) + "% (" + str(votes) + ")\n"
output = output + "--------------------\n"
#output = output + "Winner: " = sorted_candidates[0]
output = output + "--------------------\n"

#Print to terminal
print(candidates_list)
print(candidate_votes)
print(sorted_candidates)
print(output)

#Print to text file