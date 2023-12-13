import requests

def process_api_data(api_url):
    try:
        # Fetching data from the API
        response = requests.get(api_url)
        data = response.json()

        # Sample data operation (displaying information)
        for item in data:
            print(item)

        print("Processing completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

