file_name = input("Enter the file name: ")
search = input("What to search? ")
print()
found = False
with open(file_name, 'r') as content:
    for line in content:
        if search in line.lower():
            print(line.strip())
            found = True

if not found:
    print(f"No error found in file: {file_name}")
