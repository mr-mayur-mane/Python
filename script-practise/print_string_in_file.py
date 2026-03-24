search = input("Enter the keyword to search: ").strip()
file = "error.log"

with open(file, 'r') as reader:
    lines = reader.readlines()
    found = False
    for line in lines:
        if search in line.lower():
            print(f'Keyword found: {search}')
            print()
            print(line)
            found = True

    if not found:
       print("No keyword found")
    