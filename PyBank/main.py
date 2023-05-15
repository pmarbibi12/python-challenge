import os
import csv

budget_path = os.path.join( "Resources", "budget_data.csv" )

months = []
profitLoss = []
changeProf = []

totalProfit = 0.00

greatestIncrease = 0.00
greatestDecrease = 0.00

with open( budget_path ) as csvfile:
    
    csv_reader = csv.reader( csvfile )

    csv_header = next(csv_reader)

    for row in csv_reader:

        months.append(row[0])
        profitLoss.append(row[1])

    numMonths = len(months)

    i = 0

    for entry in profitLoss:
        
        lastEntry = profitLoss[i]
       
        if i >= 1:
            changeProf.append(float(profitLoss[i]) - float(profitLoss[i-1]))

        totalProfit += float(entry)

        i += 1

    print (totalProfit)

changeTotal = 0.00

x = 0
for changes in changeProf:
    if float(changes) > greatestIncrease:
            greatestIncrease = float(changes)
            gtiMonth = months[x+1]
    elif float(changes) < greatestDecrease:
            greatestDecrease = float(changes)
            gtdMonth = months[x+1]
    changeTotal += float(changes)
    x += 1

changeAvg = 0.00
changeAvg = float(changeTotal / len(changeProf))
    


print("")
print("Financial Analysis")
print("")
print("-------------------------------------------")
print("")
print(f"Total Months: {numMonths}")
print("")
print(f"Total: ${round(totalProfit)}")
print("")
print(f"Average Change: ${round(changeAvg,2)}")
print("")
print(f"Greatest Increase in Profits = {gtiMonth} (${round(float(greatestIncrease))})")
print("")
print(f"Greatest Decrease in Profits = {gtdMonth} (${round(float(greatestDecrease))})")
print("")
print("Writing results into txt file 'FinancialAnalysis.txt'")

output_path = os.path.join("FinancialAnalysis.txt")

with open(output_path,  'w') as txtfile:
     
    txtfile.write('\n'"Financial Analysis"'\n')
    txtfile.write('\n'"-------------------------------------------"'\n')
    txtfile.write(f"\nTotal Months: {numMonths}\n")
    txtfile.write(f"\nTotal: ${round(totalProfit)}\n")
    txtfile.write(f"\nAverage Change: ${round(changeAvg,2)}\n")
    txtfile.write(f"\nGreatest Increase in Profits = {gtiMonth} (${round(float(greatestIncrease))})\n")
    txtfile.write(f"\nGreatest Decrease in Profits = {gtdMonth} (${round(float(greatestDecrease))})\n")
    txtfile.write('\n')

     




