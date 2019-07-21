#import python modules
import csv
import os

#initialize variables for calulations
total_months = 0
sum_revenue = 0
revenue_change = 0

#file to read and file to output
budgetdata = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis.txt")

#assign data to variables
with open(budgetdata) as pybank_data:
    reader = csv.reader(pybank_data)
    header = next(reader)
    # print(header)

    #create loop statement for calulations
    for current_row in reader:
        total_months = total_months + 1 
        # print(total_months)    
        #sum up revenue
        sum_revenue = sum_revenue + (int(current_row[1]))

        #revenue = float(current_row[1]) <-output is the last row :(
        #print(type(current_row[1])) 

  
    # print(total_months)
    # print(sum_revenue)        


#creating variable to print output to file and print screen test
output = (   
f"\nFinancial Analysis:\n"
f"-------------------------\n"
f"Total Months: {total_months}\n"
f"Total Revenue: ${sum_revenue}\n"
f"-------------------------\n")
print(output)

outputtxt = os.path.join('PyBank/analysis.txt')
with open(file_to_output, 'w') as txt_file:
    txt_file.write(output)

print("end session")




