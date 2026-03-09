
file= input("Enter the file name: ")
search = input(f'Enter the key word to search in file {file}: ')

with open(file, 'r') as file:
    found=False
    for line in file:
        if search in line.lower():
            print(f'Key word found: {line}')
            found = True

if not found:
    print(f'No keyword found: {search}')
