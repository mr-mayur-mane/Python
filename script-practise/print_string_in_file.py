file = input("Enter the file name: ")
keyword = input("Enter the keyword to search in file: ")

with open(file, 'r') as r:
    found = False
    for line in r:
        if keyword in line:
            print(line)
            found = True
        
    if not found:
        print(f'Keyword `{keyword}` not found in file `{file}`')
