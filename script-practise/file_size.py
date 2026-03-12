import os

file = "app.conf"

size = os.path.getsize(file)/(1024 * 1024)
print(f'File size of {file} is {round(size,4)} M')