import csv



def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = 'abysmal'
    elif rating <= -1:
        category = 'awful'
    else:
        category = 'bad'

    return category



def get_ratings():
    with open("dad_jokes.csv","r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        #calling next here removes the header row
        next(csv_reader)
        modified_rows = []

        for row in csv_reader:
            id = row[0]
            joke = row[1]
            rating = row[2]
            category = rating_category(rating)
            new_row = [id,joke,rating,category]
            modified_rows.append(new_row)

        return modified_rows

def create_new_dad_jokes_file_with_categories(modified_rows):

    with open("dad_jokes_with_categories.csv","w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow((["id","joke","rating","category"]))

        csv_writer.writerows(modified_rows)

create_new_dad_jokes_file_with_categories(get_ratings())


    # #this is multiple
    # csv_writer.writerows([['Julius','Cat','catnip',3215],
    #                       ['Cal','Cat','anything edible',71142],
    #                       ['Lena','Cat','Sheba',142],
    #                       ['Bruiser','Featherfin Catfish','fish pellets',54]])
