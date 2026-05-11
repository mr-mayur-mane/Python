import os

dir = input("Enter the directory path: ")

if os.path.isdir(dir):
    file = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]
    print(f'Files ending with .log in dir {dir}: {file}')
    print()
    print("Count: ", len(file))
else:
    print(f'Directory not found: {dir}')