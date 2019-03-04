import os
import csv

financial_csv=os.path.join("financial_data.csv")

with open(financial_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
        
    net_profit=1852539
    row_number=0
    change_in_profit=[]

    for row in csvreader:
        if row_number == 0:
            print(f"Headings are: {csv_header}")
        else:
            if row_number == 1:
                previous_profit=int(row[1])
            else:
                current_profit=int(row[1])
                net_profit += current_profit
                if row_number > 1:
                    change_in_profit.append(current_profit-previous_profit)
                    prev_profit=current_profit 
        row_number += 1
    Average_change=(sum(change_in_profit, 116771))/sum((len(change_in_profit), 1))
    Max_dec=min(change_in_profit)
    Max_inc=max(change_in_profit)
    print(f"Total Months:{row_number}")
    print(f"Total: {net_profit}")
    print(f"Average Change: {Average_change}")
    print(f"Max Decrease: {Max_dec}")
    print(f"Max Increase: {Max_inc}")
with open(output_path, 'w', newline'') as csvfile:
    csvwriter=csv.writer(csvfile, delimiter=',')
    csvwriter.writerow
