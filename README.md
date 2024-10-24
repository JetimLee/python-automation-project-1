Here’s the updated README that reflects the correct script name:

# Product Sales Automation Script

## Overview

This Python script (`project.py`) automates the process of reading product sales data from a text file, generating sale records using predefined product information, and writing the processed data to a CSV file. The script reads product IDs from the `product_sales.txt` file, matches them against a predefined product catalog (`product_data`), and outputs a sales report to a CSV file (`product_sales.csv`).

## Features

- Reads product IDs from a sales file (`product_sales.txt`).
- Matches product IDs to the product catalog containing product names and unit prices.
- Compiles sales data for each product, including sale ID, sale date, product ID, product name, and unit price.
- Exports the compiled sales data to a CSV file (`product_sales.csv`).
- Handles missing product IDs and missing sales files with appropriate error handling and logging.

## Files

1. **`product_sales.txt`**: Input text file containing product IDs of sold products. Each product ID should be on a new line.
   
2. **`product_sales.csv`**: Output CSV file containing the following fields:
   - Sale ID (unique sale number)
   - Date (the date when the script was run)
   - Product ID (from the input file)
   - Product Name (fetched from the predefined product catalog)
   - Unit Price (from the predefined product catalog)

3. **`project.py`**: The Python script that reads the sales data, processes the product information, and writes the output to a CSV file.

## Requirements

- **Python 3.7+**
- No external libraries are required (uses only Python's built-in libraries: `csv` and `datetime`).

## How It Works

### 1. Product Data

The script includes a predefined product catalog stored in the `product_data` dictionary. This catalog contains product IDs, names, and unit prices.

Example `product_data`:
```python
product_data = {
    "P001": {"product_name": "Wireless Headphones", "unit_price": 100},
    "P002": {"product_name": "Laptop Backpack", "unit_price": 60},
    "P003": {"product_name": "Bluetooth Speaker", "unit_price": 50},
    # more products...
}
```

### 2. Sales Data

The script reads a list of product IDs from a text file called `product_sales.txt`. Each line in this file should contain a valid product ID. The script processes each product ID by looking it up in the predefined product catalog.

Example `product_sales.txt`:
```
P001
P003
P002
P999  # This product doesn't exist in the product catalog, a warning will be logged.
```

### 3. Data Compilation

For each product ID, the script:
- Fetches the product name and unit price from the product catalog.
- Assigns a unique Sale ID to each product.
- Records the current date using the `datetime` module.

### 4. Output to CSV

The sales data is written to a CSV file named `product_sales.csv`, with the following columns:
- **Sale ID**: A unique identifier for each sale, starting from 1.
- **Date**: The current date when the script was run.
- **Product ID**: The ID of the sold product.
- **Product Name**: The name of the product.
- **Unit Price**: The unit price of the product.

### 5. Error Handling

- **File Not Found**: If the `product_sales.txt` file is not found, the script will print an error message and exit.
- **Product Not Found**: If a product ID in the sales file does not exist in the product catalog, the script logs a warning and continues processing the remaining product IDs.

## Functions

1. **`get_current_date()`**: Returns today's date as a string in the format `YYYY-MM-DD`.

2. **`get_product_ids_from_sales_file(file_path="product_sales.txt")`**: Reads the `product_sales.txt` file and returns a list of product IDs. If the file is not found, it logs an error and returns an empty list.

3. **`generate_product_row_details(product_id, counter, product_data)`**: Generates a list containing the sale details (Sale ID, date, product ID, product name, and unit price). If a product ID is not found in the `product_data` dictionary, it logs a warning and returns `None`.

4. **`compile_product_details(product_ids, product_data)`**: Loops through the list of product IDs and uses `generate_product_row_details()` to compile the list of sale records. This function returns a "list of lists" of all the sale records.

5. **`write_product_details_to_csv(product_details, output_file="product_sales.csv")`**: Writes the sale records to a CSV file, including a header row. If there is an issue writing to the file, it logs an error.

6. **`main()`**: The main driver function. It coordinates the following steps:
   - Reads the product IDs from the sales file.
   - Compiles the product details into a list.
   - Writes the list to a CSV file.

## How to Run

1. **Prepare the Input File**:
   - Create a `product_sales.txt` file in the same directory as the script. The file should contain one product ID per line.

2. **Run the Script**:
   - Run the Python script from the terminal or command line:
     ```bash
     python project.py
     ```

3. **Check Output**:
   - After running the script, a `product_sales.csv` file will be created in the same directory, containing the processed sales data.

## Example

### Example `product_sales.txt`:

```
P001
P003
P002
P999  # Invalid product ID, will trigger a warning
```

### Example Output in `product_sales.csv`:

| Sale ID | Date       | Product ID | Product Name         | Unit Price |
|---------|------------|------------|----------------------|------------|
| 1       | 2024-10-24 | P001       | Wireless Headphones   | 100        |
| 2       | 2024-10-24 | P003       | Bluetooth Speaker     | 50         |
| 3       | 2024-10-24 | P002       | Laptop Backpack       | 60         |

### Error Handling:
- If `P999` is included in `product_sales.txt` but does not exist in the product catalog, the script logs a warning and continues processing other product IDs.

## Potential Improvements

- **Dynamic Product Data**: The product data could be loaded dynamically from an external source such as a database or API, instead of being hardcoded in the script.
- **CLI Arguments**: Allow users to specify the input and output file paths as command-line arguments.
- **Logging**: Instead of printing warnings and errors to the console, errors and logs could be written to a log file.

## License

This project is open-source and free to use under the MIT License. See the LICENSE file for more details.

---

Let me know if you need further adjustments or clarification!
