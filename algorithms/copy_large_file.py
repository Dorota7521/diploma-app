import shutil

def copy_large_file(source_file, destination_file):
    try:
        # Kopiowanie pliku
        shutil.copy(source_file, destination_file)
        print("Kopiowanie zakończone pomyślnie.")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
