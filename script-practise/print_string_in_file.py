find = input("Enter the keyword to search: ")

file = "error.log"

def search_def(find, file):
    found = False
    with open(file, 'r') as f:
        content=f.readlines()
        for line_no, line in enumerate(content, start=1):
            if find in line.lower():
                print(f'Keyword found: "{find}" at {line_no}\n{line}')
                found= True

    if not found:
        print(f'{find}: Not found in {file}')

search_def(find, file)