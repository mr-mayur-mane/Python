import os

dir = "C:\\"

file = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]

print(f'Files ending with .log in dir {dir}: {file}')