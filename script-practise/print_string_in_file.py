
file = "error.log"

search = input("Enter the keywod to search: ")

print()

with open(file, 'r') as reader:
    lines = reader.readlines()
    found = False
    for line_no, line in enumerate(lines, start=1):
        if search in line.lower():
            found = True
            print(f'The keyword {search} found at line {line_no}: line: {line.strip()}')
    
    if not found:
        print("No keyword found in the file:")