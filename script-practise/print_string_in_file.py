search = input("Enter the keyword to search: ")

file = "error.log"

def search_keyword(search, file):
    found = False
    with open(file, 'r') as f:
        config=f.readlines()
        for line_no, line in enumerate(config, start=1):
            if search in line.lower():
                print(f'Keyword Found: "{search}" found at {line_no}\n {line}')
                found = True

        if not found:
            print(f'{search}: Not found')
search_keyword(search,file)