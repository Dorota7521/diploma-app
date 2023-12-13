import requests

def process_api_data(api_url):
    try:
        # Pobieranie danych z API
        response = requests.get(api_url)
        data = response.json()

        # Przykładowa operacja na danych (wyświetlanie informacji)
        for item in data:
            print(item)

        print("Przetwarzanie zakończone pomyślnie.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
