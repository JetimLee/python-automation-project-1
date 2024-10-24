import csv

with open("expensive_pets.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # calling next here removes the header row
    next(csv_reader)
    for row in csv_reader:
        # Accesses the whole row object which becomes a list, can access with index as you would in any other list
        print(row[1])
