# Sample I/O program in Python

def process_file(input_file, output_file):
    try:
        # Opening the file for reading
        with open(input_file, 'r') as file:
            # Reading data from the file
            data = file.read()

            # Sample data operation (converting letters to uppercase)
            processed_data = data.upper()

        # Opening the file for writing
        with open(output_file, 'w') as file:
            # Writing the processed data to the file
            file.write(processed_data)

        print("I/O operations completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
