import os

dir = input("Enter the dir path: ")

if os.path.isdir(dir):
    file = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]

    print(f'File ending with .log: {file}')

else:
    print(f'{dir}: Invalid dir or dir not exists')