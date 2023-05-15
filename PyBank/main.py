#import modules
import os
import csv

#create reference path
budget_path = os.path.join( "Resources", "budget_data.csv" )

#create lists
months = []
profitLoss = []
changeProf = []

#Set variable to 0
totalProfit = 0.00          #total of all profit and losses
greatestIncrease = 0.00     #variable for greatest percentage increase
greatestDecrease = 0.00     #variable for greatest percentage decrease

#open file
with open(budget_path) as csvfile: 
    
    csv_reader = csv.reader(csvfile)    #set reader reference

    csv_header = next(csv_reader)       #set header to ignore

    for row in csv_reader:              #assign values to lists

        months.append(row[0])           #add date values to "months" list
        profitLoss.append(row[1])       #add profit/loss values to "profitLoss" list

    numMonths = len(months) #number of months = the amount of values in "months" list

    i = 0 # set i to 0

    for entry in profitLoss: #for every value in "profitLoss" list
       
        if i >= 1: #i needs to start at 1 so that changeProf can be found

            changeProf.append(float(profitLoss[i]) - float(profitLoss[i-1])) #add the value of this profit value - the last profit value

        totalProfit += float(entry) #find totalProfit by adding every entry together

        i += 1 #increase i by 1 

changeTotal = 0.00 #set changeTotal to 0 for starting value
x = 0 #set x to 0 for starting value

for changes in changeProf: #loop through each value stored in changeProf list

    if float(changes) > greatestIncrease: #check if current value is greater than the stored value in greatestIncrease
            
            greatestIncrease = float(changes)  #set new value as greatest increase
            gtiMonth = months[x+1]             #save Month where change occured. add 1 to the index to get the month the change ocurred instead of the prior month

    elif float(changes) < greatestDecrease: #check if current value is lesser than the stored value in greatestDecrease
           
            greatestDecrease = float(changes)  #set new value as greatest decrease
            gtdMonth = months[x+1]             #save Month where change occured. add 1 to the index to get the month the change ocurred instead of the prior month

    changeTotal += float(changes)   #add all the changes stored in changeProf list
    x += 1                          #add 1 to x to keep track of the position of the month

changeAvg = float(changeTotal / len(changeProf))  #calculate the average change by dividing changeTotal by the number of changes
    
#set path for txt file   
output_path = os.path.join("analysis","FinancialAnalysis.txt") 

with open(output_path,  'w') as txtfile: #write to file and print results
     
    print('\n'"-------------------------------------------"'\n')
    txtfile.write('\n'"Financial Analysis"'\n')
    print("Financial Analysis"'\n')
    txtfile.write('\n'"-------------------------------------------"'\n')
    print("-------------------------------------------"'\n')
    txtfile.write(f"\nTotal Months: {numMonths}\n")
    print(f"Total Months: {numMonths}\n")
    txtfile.write(f"\nTotal: ${round(totalProfit)}\n")
    print(f"Total: ${round(totalProfit)}\n")
    txtfile.write(f"\nAverage Change: ${round(changeAvg,2)}\n")
    print(f"Average Change: ${round(changeAvg,2)}\n")
    txtfile.write(f"\nGreatest Increase in Profits = {gtiMonth} (${round(float(greatestIncrease))})\n")
    print(f"Greatest Increase in Profits = {gtiMonth} (${round(float(greatestIncrease))})\n")
    txtfile.write(f"\nGreatest Decrease in Profits = {gtdMonth} (${round(float(greatestDecrease))})\n")
    print(f"Greatest Decrease in Profits = {gtdMonth} (${round(float(greatestDecrease))})\n")
    txtfile.write('\n')
    print("***** Writing results into txt file 'FinancialAnalysis.txt' *****"'\n')

     




