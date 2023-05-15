import os
import csv

election_path = os.path.join( "Resources", "election_data.csv" )

ballot_id = []
county = []
candidate = []

with open(election_path) as csvfile:
    
    csv_reader = csv.reader(csvfile)

    csv_header = next(csv_reader)

    for row in csv_reader:

        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    totalVotes = len(ballot_id)

    uniqueCandidate = {}

    numCandidate  = 1

    lastEntry = str(candidate[0])
    uniqueCandidate.update({str(lastEntry): []})
    i = 0


    for unique in candidate:
        if unique != lastEntry:
            uniqueCandidate.update({str(unique):[]})

    for yyy in candidate:
        uniqueCandidate[yyy].append(ballot_id[i])
        i += 1


numVotes = 0
winningVote = 0


output_path = os.path.join("ElectionResults.txt")

with open(output_path,  'w') as txtfile:
     
    txtfile.write(f"\nElection Results\n")
    txtfile.write("---------------------------------------------------------")
    txtfile.write(f"\nTotal Votes: {totalVotes}\n")
    txtfile.write("---------------------------------------------------------")
    winningVote = 0 
    print(f"\nElection Results\n")
    print("---------------------------------------------------------")
    print(f"\nTotal Votes: {totalVotes}\n")
    print("---------------------------------------------------------")


    for each in uniqueCandidate:
            name = str(each)
            numVotes = len(uniqueCandidate[name])
            percentVotes = numVotes/totalVotes
            txtfile.write(f"\n {str(each)}: {round(percentVotes*100,3)}% ({numVotes}) \n")
            print(f"\n {str(each)}: {round(percentVotes*100,3)}% ({numVotes}) \n")
            if numVotes > winningVote:
                winningVote = numVotes
                winner = str(each)    
            numVotes = 0
    print("---------------------------------------------------------")
    print(f"\n Winner: {winner}\n")
    print("---------------------------------------------------------"'\n')

    print("Writing results into txt file 'ElectionResuls.txt'")
    txtfile.write("---------------------------------------------------------")
    txtfile.write(f"\n Winner: {winner}\n")
    txtfile.write("---------------------------------------------------------"'\n')
