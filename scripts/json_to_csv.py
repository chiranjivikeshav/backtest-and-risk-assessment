import json
import csv

# Function to convert the JSON to CSV
def json_to_csv(json_filename, csv_filename):
    try:
        # Open the JSON file with utf-16 encoding (to handle BOM)
        with open(json_filename, 'r', encoding='utf-16') as json_file:
            data = json.load(json_file)

        # Access the relevant part of the JSON data
        result_data = data.get("result", {})
        ticks = result_data.get("ticks", [])
        open_prices = result_data.get("open", [])
        high_prices = result_data.get("high", [])
        low_prices = result_data.get("low", [])
        close_prices = result_data.get("close", [])
        volume_data = result_data.get("volume", [])
        
        # Check if any of the lists are empty
        if not (ticks and open_prices and high_prices and low_prices and close_prices and volume_data):
            print("Missing data in the JSON.")
            return

        # Open the CSV file in write mode
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write the header
            csv_writer.writerow(['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])

            # Extract and write the data into CSV
            for i in range(len(ticks)):
                csv_writer.writerow([ticks[i], open_prices[i], high_prices[i], low_prices[i], close_prices[i], volume_data[i]])

            print(f"CSV file '{csv_filename}' has been created successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Call the function with your file names
json_filename = "data/test_deribit_data.json"  # Path to your JSON file
csv_filename = "data/test_deribit_data.csv"  # Output CSV file
json_to_csv(json_filename, csv_filename)