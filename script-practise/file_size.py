import os

file = input("Enter the file name: ")

file_size = os.path.getsize(file)/(1024 * 1024)

print(f'File size of {file}: {round(file_size,4)} M')