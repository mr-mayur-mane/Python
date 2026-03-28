file = input("Enter the file name: ")
keyword = input("Enter the keyword to search in file: ")

with open(file, 'r') as f:
    found = False
    lines = f.readlines()
    for line in lines:
        if keyword in line:
            print(line)
            found = True
        
    if not found:
        print(f'Keyword `{keyword}` not found in file `{file}`')
