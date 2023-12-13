plaintext = b'This is a secret message.'
file_size = 100 * 1024 * 1024  # 100 MB

# Calculating the number of copies of the message needed to achieve the desired file size
num_copies = (file_size // len(plaintext)) + 1
encrypted_text = plaintext * num_copies

# Creating a file and saving the content to it
file_path = 'secret_message.txt'
with open(file_path, 'wb') as file:
    file.write(encrypted_text)

print(f'The file {file_path} has been successfully created.')

