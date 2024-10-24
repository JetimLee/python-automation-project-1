# ['Max','Dog', 'bacon strips',4754]
# ['Julius','Cat','catnip',3215]
# ['Cal','Cat','anything edible',71142]
# ['Lena','Cat','Sheba',142]
# ['Bruiser','Featherfin Catfish','fish pellets',54]

import csv

with open("expensive_pets.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    # writes the headers
    csv_writer.writerow(["name", "species", "favorite_snack", "monthly_cost"])
    # start putting in rows data
    # this is singular
    csv_writer.writerow(["Max", "Dog", "bacon strips", 4754])

    # this is multiple
    csv_writer.writerows(
        [
            ["Julius", "Cat", "catnip", 3215],
            ["Cal", "Cat", "anything edible", 71142],
            ["Lena", "Cat", "Sheba", 142],
            ["Bruiser", "Featherfin Catfish", "fish pellets", 54],
        ]
    )
