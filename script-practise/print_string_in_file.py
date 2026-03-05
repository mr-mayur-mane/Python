file_name = input("Enter the file name: ")

found = False
with open(file_name, 'r') as content:
    for line in content:
        if 'error' in line.lower():
            print(line.strip())
            found = True

if not found:
    print("No error found in", file_name)
