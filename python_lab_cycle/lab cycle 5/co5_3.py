#MARTIN ABRAHAM
#21MCA030
import csv
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
