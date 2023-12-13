# Przykładowy program I/O w Pythonie

def process_file(input_file, output_file):
    try:
        # Otwieranie pliku do odczytu
        with open(input_file, 'r') as file:
            # Odczyt danych z pliku
            data = file.read()

            # Przykładowa operacja na danych (zamiana liter na duże)
            processed_data = data.upper()

        # Otwieranie pliku do zapisu
        with open(output_file, 'w') as file:
            # Zapis przetworzonych danych do pliku
            file.write(processed_data)

        print("Operacje I/O zakończone pomyślnie.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")