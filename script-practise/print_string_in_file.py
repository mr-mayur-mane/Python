# file = input("Enter the file name: ")
# keyword = input("Enter the keyword to search in file: ")

# with open(file, 'r') as f:
#     found = False
#     lines = f.readlines()
#     for line in lines:
#         if keyword in line:
#             print(line)
#             found = True
        
#     if not found:
#         print(f'Keyword `{keyword}` not found in file `{file}`')

search = input("Enter the keyword to search: ")

file = "error.log"

def search_keyword(search, file):
    found = False
    with open(file, 'r') as f:
        config=f.readlines()
        for line in config:
            if search in line.lower():
                print(f'Keyword Found: {search}\n {line}')
                found = True

        if not found:
            print(f'{search}: Not found')
search_keyword(search,file)