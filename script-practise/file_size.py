import os

file = "app.conf"

size = os.path.getsize(file)/(1024 * 1024)
print(f'File size of {file}: {round(size,4)} M')