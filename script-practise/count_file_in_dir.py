import os

dir = input("Enter the dir name: ")

if os.path.isdir(dir):
    print(f'Valid dir: {dir}')
    file = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]
    print(f'File count in dir {dir}: {len(file)}')

else:
    print(f'Invalid dir path/ Dir not exits: {dir.strip()}')