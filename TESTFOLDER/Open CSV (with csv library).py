import csv
file = open(r'C:\Users\brend\Downloads\City_Of_Trenton_-_2019_Certified_Tax_List.csv')
rows = []
header = []
csvreader = csv.reader(file)
header = next(csvreader)
for row in csvreader:
    rows.append(row)
file.close()

   
