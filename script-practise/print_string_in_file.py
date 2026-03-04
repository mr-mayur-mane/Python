
file_name = input("Enter the file path: ")

with open(file_name, 'r') as f:
    for line in f:
        print(line)
