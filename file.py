plaintext = b'This is a secret message.'
file_size = 100* 1024 * 1024  # 500 MB

# Obliczanie liczby kopii wiadomości potrzebnych do uzyskania żądanego rozmiaru pliku
num_copies = (file_size // len(plaintext)) + 1
encrypted_text = plaintext * num_copies

# Tworzenie pliku i zapisanie do niego zawartości
file_path = 'secret_message.txt'
with open(file_path, 'wb') as file:
    file.write(encrypted_text)

print(f'Plik {file_path} został utworzony z sukcesem.')
