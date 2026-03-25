search = input("Enter the keyword to be search: ").strip()

file = "error.log"

with open(file, 'r') as reader:
    lines= reader.readlines()
    found = False
    for line_no, line in enumerate(lines, start=1):
        if search in line.lower():
            print(f'Line no: {line_no}')
            print(line)
            found = True
    
    if not found:
        print(f'Keyword not found: {search}')


    