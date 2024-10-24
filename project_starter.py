import csv
from datetime import datetime

# TODO 2: Define the product_data dictionary with product IDs, names, and unit prices
product_data = {
    "P001": {"product_name": "Wireless Headphones", "unit_price": 100},
    "P002": {"product_name": "Laptop Backpack", "unit_price": 60},
    "P003": {"product_name": "Bluetooth Speaker", "unit_price": 50},
    "P004": {"product_name": "USB Flash Drive", "unit_price": 20},
    "P005": {"product_name": "Mobile Phone Case", "unit_price": 15},
    "P006": {"product_name": "Wireless Mouse", "unit_price": 30},
    "P007": {"product_name": "Laptop Stand", "unit_price": 40},
    "P008": {"product_name": "HDMI cable", "unit_price": 15},
    "P009": {"product_name": "Smartphone", "unit_price": 600},
    "P010": {"product_name": "External Hard Drive", "unit_price": 100},
}


# Function to get today's date as a string
def get_current_date():
    return datetime.today().strftime("%Y-%m-%d")


# Function to read product IDs from the sales file
def get_product_ids_from_sales_file(file_path="product_sales.txt"):
    try:
        with open(file_path, "r") as sales_file:
            return sales_file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []


# Function to generate the product row details based on product ID
def generate_product_row_details(product_id, counter, product_data):
    product_info = product_data.get(product_id)
    if product_info:
        product_name = product_info["product_name"]
        unit_price = product_info["unit_price"]
        return [counter, get_current_date(), product_id, product_name, unit_price]
    else:
        print(f"Warning: Product ID {product_id} not found in product_data.")
        return None


# Function to compile all product details into a list of lists
def compile_product_details(product_ids, product_data):
    list_of_product_details = []
    counter = 1
    for product_id in product_ids:
        product_row_details = generate_product_row_details(
            product_id, counter, product_data
        )
        if product_row_details:
            list_of_product_details.append(product_row_details)
            counter += 1
    return list_of_product_details


# Function to write the product details to a CSV file
def write_product_details_to_csv(product_details, output_file="product_sales.csv"):
    headers = ["Sale ID", "Date", "Product ID", "Product Name", "Unit Price"]
    try:
        with open(output_file, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            writer.writerows(product_details)
        print(f"Data successfully written to {output_file}.")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")


# Main function to coordinate the process
def main():
    product_ids = get_product_ids_from_sales_file()  # Read product IDs from file
    if not product_ids:
        return  # If the file is missing or empty, exit the script

    product_details = compile_product_details(
        product_ids, product_data
    )  # Compile product details
    write_product_details_to_csv(product_details)  # Write details to CSV


# Entry point of the script
if __name__ == "__main__":
    main()
