
file_name = input("Enter the file path: ")

with open(file_name, 'r') as file:
    for line in file:
        if 'error' in line.lower():
            print("Error found: ", line.strip())
        else:
            print("No error found")
