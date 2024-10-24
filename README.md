# Product Sales Automation Script

## Overview

This Python script automates the process of reading product sales data from a text file, compiling sales records based on a predefined product database, and exporting the processed data to a CSV file. The script is designed to be modular, with object-oriented programming (OOP) principles in mind. It features error handling for missing products and files, and uses Python's `dataclasses` to structure the product and sale records.

## Features

- Reads product IDs from a sales file (`product_sales.txt`).
- Looks up product details (name and unit price) from a predefined product database.
- Generates structured sales records using `Sale` and `Product` data classes.
- Outputs sales records to a CSV file (`product_sales.csv`).
- Handles missing product IDs and sales files with appropriate error messages.
- Uses object-oriented programming (OOP) and custom exceptions for maintainability and clarity.

## Files

1. **`product_sales.txt`**: A text file containing the list of product IDs sold. Each product ID should be on a new line.
   
2. **`product_sales.csv`**: The output CSV file that contains processed sales data, including:
   - Sale ID
   - Sale Date
   - Product ID
   - Product Name
   - Unit Price

3. **`product_sales_automation.py`**: The Python script that reads the product sales, compiles the data, and exports it to a CSV file.

## Requirements

- **Python 3.7+**
- No external libraries are required (uses only Python's built-in libraries such as `csv`, `datetime`, and `dataclasses`).

## How It Works

1. **Product Data**: The script contains a predefined `product_data` dictionary with product IDs, names, and unit prices.
   
2. **Sales Data**: It reads a list of product IDs from a text file (`product_sales.txt`). The file is expected to contain one product ID per line, representing each product that has been sold.

3. **Data Compilation**: For each product ID in the sales file:
   - It looks up the corresponding product name and unit price from the predefined `product_data` dictionary.
   - If the product ID is not found, the script logs a warning but continues processing the other product IDs.

4. **CSV Export**: The script writes the compiled sales records to a CSV file (`product_sales.csv`), which includes:
   - Sale ID (an incrementing integer)
   - Sale Date (the current date)
   - Product ID
   - Product Name
   - Unit Price

## Classes and Functions

### Classes

1. **`Product`**: A data class that represents a product with:
   - `product_id`: The unique ID of the product.
   - `product_name`: The name of the product.
   - `unit_price`: The unit price of the product.

2. **`Sale`**: A data class that represents a sale with:
   - `sale_id`: The unique sale ID.
   - `sale_date`: The date the sale occurred.
   - `product`: A `Product` object associated with the sale.

3. **`ProductDatabase`**: A class that manages product data. It loads product information and provides methods to fetch a product by its ID. If the product is not found, a custom `ProductNotFoundError` is raised.

4. **`SalesManager`**: A class that manages sales operations, including:
   - Reading the sales file.
   - Compiling sales records.
   - Writing sales data to a CSV file.

### Functions

1. **`get_current_date()`**: Returns the current date as a string in the format `YYYY-MM-DD`.
   
2. **`generate_sale()`**: Generates a `Sale` object based on a product ID and sale counter. If the product is not found, it logs a warning and returns `None`.

3. **`compile_sales()`**: Compiles all the sales data from the list of product IDs into `Sale` objects.

4. **`write_sales_to_csv()`**: Writes the compiled sales records to a CSV file.

5. **`main()`**: The main driver function that:
   - Initializes the product database and sales manager.
   - Reads product IDs from the sales file.
   - Compiles sales data.
   - Writes the sales data to a CSV file.

## How to Run

1. **Ensure You Have the Required Files**:
   - Make sure you have a `product_sales.txt` file in the same directory as the script. This file should contain one product ID per line.

2. **Run the Script**:
   - Run the Python script from the terminal or command line:
     ```bash
     python product_sales_automation.py
     ```

3. **Check Output**:
   - The script will create a `product_sales.csv` file in the same directory. This file will contain the processed sales data.

4. **Handling Errors**:
   - If the `product_sales.txt` file is missing, the script will notify you with an error message.
   - If a product ID in the sales file is not found in the product data, the script will continue processing but log a warning message.

## Example

### Example `product_sales.txt`:

```
P001
P003
P006
P010
P999  # Invalid product ID, will trigger a warning
```

### Example Output in `product_sales.csv`:

| Sale ID | Date       | Product ID | Product Name         | Unit Price |
|---------|------------|------------|----------------------|------------|
| 1       | 2024-10-24 | P001       | Wireless Headphones  | 100        |
| 2       | 2024-10-24 | P003       | Bluetooth Speaker    | 50         |
| 3       | 2024-10-24 | P006       | Wireless Mouse       | 30         |
| 4       | 2024-10-24 | P010       | External Hard Drive  | 100        |

## Potential Improvements

- **Database Integration**: Replace the hardcoded `product_data` dictionary with an external data source like a database or API.
- **User Input**: Allow users to input the file paths for the sales file and the CSV output.
- **Enhanced Error Handling**: Provide options to log errors to a file rather than printing them to the console.

## License

This project is open-source and free to use under the MIT License. See the LICENSE file for more details.

---
