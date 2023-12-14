import requests
import json

def process_api_data(api_url, output_file):
    try:
        # Fetching data from the API
        response = requests.get(api_url)
        data = response.json()

        # Writing data to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

        print(f"Data has been successfully written to {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")
