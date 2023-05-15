#import modules
import os
import csv

election_path = os.path.join( "Resources", "election_data.csv" ) #set path for source file

#declare lists
ballot_id = []  #store ballot ids in list
candidate = []  #store candidate colum in list

with open(election_path) as csvfile: #open and read source file
    
    csv_reader = csv.reader(csvfile) #reference for reader

    csv_header = next(csv_reader)    #store header

    for row in csv_reader: #loop through the rest of the file

        ballot_id.append(row[0]) #store ballot ids in list
        candidate.append(row[2]) #store candidate colum in list

        #ignored row[1] as not needed for assignment

    totalVotes = len(ballot_id) #get the number of votes by getting the amount of values stored in ballot_id list

    uniqueCandidate = {} #declare dictionary


    lastEntry = str(candidate[0])                   #set lastEntry to the first entry
    uniqueCandidate.update({str(lastEntry): []})    #create a list using the candidates name and store in uniqueCandidate dictionary
    
    for unique in candidate:                        #loop through candidate list and store each unique candidate as a list in the uniqueCandidate dictionary
        
        if unique != lastEntry:                     #if current entry does not equal last store entry then
            uniqueCandidate.update({str(unique):[]})    #create a list using the name of the candidate and store it in the uniqueCandidate dictionary

    i = 0 #set i to 0 - counter/tracker

    for yyy in candidate:                           #loop through every entry in candidate list
        uniqueCandidate[yyy].append(ballot_id[i])   #store the ballot id to the corespoding candidate
        i += 1                                      #add 1 to i to keep track of ballot id associated with the current vote

#set to 0
numVotes = 0        #variable for number of votes per candidate
winningVote = 0     #variable for the winning number of votes


output_path = os.path.join("analysis","ElectionResults.txt")  #set path of output txt file

with open(output_path,  'w') as txtfile:    #open and write to determined path
     

    #Print total votes and write to txt file
    txtfile.write(f"\nElection Results\n")
    txtfile.write("---------------------------------------------------------")
    txtfile.write(f"\nTotal Votes: {totalVotes}\n")
    txtfile.write("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print(f"\nElection Results\n")
    print("---------------------------------------------------------")
    print(f"\nTotal Votes: {totalVotes}\n")
    print("---------------------------------------------------------")

    for each in uniqueCandidate: #go through each candidate stored in dictionary and output the results
            
            name = str(each)                              #take string of each and store as name
            numVotes = len(uniqueCandidate[name])         #get number of votes per candidate - pull from list stored in the dictionary
            percentVotes = numVotes/totalVotes            #calculate percentage of votes per candidate vs total # of votes
            
            #print and write results to text file
            txtfile.write(f"\n {str(each)}: {round(percentVotes*100,3)}% ({numVotes}) \n") # {candidate}: {percentOfVotes} {voteCount}
            print(f"\n {str(each)}: {round(percentVotes*100,3)}% ({numVotes}) \n")
            
            if numVotes > winningVote: #check if current number of votes beats previous number of votes
                winningVote = numVotes      #save the number of votes
                winner = str(each)          #save candidate name
            numVotes = 0      #set numVotes to 0 for next candidate
    
    #print and write the winner to the txt file
    print("---------------------------------------------------------")
    print(f"\n Winner: {winner}\n")                                            # Winner: {winning candidate}
    print("---------------------------------------------------------"'\n') 
    txtfile.write("---------------------------------------------------------")
    txtfile.write(f"\n Winner: {winner}\n")
    txtfile.write("---------------------------------------------------------"'\n')

    print("***** Writing results into txt file 'ElectionResuls.txt' *****"'\n')
