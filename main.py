from database_manager import DatabaseManager
from data_processor import DataProcessor
import random

# Function that creates a list of five random numbers between 1 and 1000
# Using this to randomize the art peices chosen
def get_random_numbers():
    return random.sample(range(1, 1000), 5)

art_objects = get_random_numbers()

for piece in art_objects:
    api_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{piece}"
    
    # Create instances of the classes
    data_processor = DataProcessor()
    database_manager = DatabaseManager()
    
    # Retrieve and process data
    raw_data = data_processor.fetch_data(api_url)
    filtered_data = data_processor.extract_fields(raw_data)

    # Insert data into the database
    if filtered_data:
        database_manager.insert_data(filtered_data)
        print("Data saved successfully to the database.")

# Print the table contents
database_manager.print_table()

# Close the database connection
database_manager.close_connection()


