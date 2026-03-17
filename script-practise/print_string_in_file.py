
file = "error.log"

search = input("Enter the keywod to search: ")

print()

with open(file, 'r') as reader:
    lines = reader.readlines()
    found = False
    for line in lines:
        if search in line.lower():
            found = True
            print(f'The keyword {search} found:\n {line}')
    
    if not found:
        print("No keyword found in the file:")