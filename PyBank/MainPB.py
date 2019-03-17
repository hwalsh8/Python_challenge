#import python modules
import csv
import os

#initialize variables for calulations
total_months = 0
sum_revenue = 0
revenue_change = 0

#create file path
budgetdata = os.path.join("Resources", "budget_data.csv")

#assign data to variables
with open(budgetdata) as pybank_data:
    reader = csv.reader(pybank_data)
    header = next(reader)

    #create loop statement for calulations
    for current_row in reader:
        total_months = total_months + 1     
        #sum up revenue
        sum_revenue = sum_revenue + (int(current_row[1]))
        #revenue = float(current_row[1]) <-output is the last row :(
        #print(type(current_row[1])) <-is this type str or int

  
        

#printing outputs for file
print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$"+str(sum_revenue))
#print("Average Change: "("enter variable"))
#print("Greatest Increase in Profits: "("enter variable"))
#print("Greatest Decrease in Profits: "("enter variable"))

#creating variable to print output to file and print screen test
Output = (   
f("Financial Analysis: ")
f("-------------------------")
f("Total Months: " + str(total_months)")
f("Total Revenue: " + "$"+str(sum_revenue)"))
print(Output)

outputtxt = os.path.join('PyBank/TestSolutions.txt')
with open(outputtxt, 'w') as txtfile:
    txtwriter = txtfile.write(Output)

print("end session")




