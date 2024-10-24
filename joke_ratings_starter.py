import csv


def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = "abysmal"
    elif rating <= -1:
        category = "awful"
    else:
        category = "bad"

    return category


def get_ratings():
    with open("dad_jokes.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # calling next here removes the header row
        # Will return the columns as a value as well, good to know
        headers = next(csv_reader)
        headers.append("Rating Category")
        modified_rows = []

        for row in csv_reader:
            id = row[0]
            joke = row[1]
            rating = row[2]
            category = rating_category(rating)
            new_row = [id, joke, rating, category]
            modified_rows.append(new_row)

        return modified_rows, headers


def create_new_dad_jokes_file_with_categories(rows_and_headers):
    with open("dad_jokes_with_categories.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(rows_and_headers[1])

        csv_writer.writerows(rows_and_headers[0])


create_new_dad_jokes_file_with_categories(get_ratings())
