file = "app.conf"

key = input("Enter the config key: ")
value = input("Enter the config value: ")

# with open(file, 'r') as f:
#     content = f.read()
#     if config not in content:
#         print(f'No config found: {config}')
#         print(f'Adding the config...')
#         with open(file, 'a') as f:
#             f.write("\n" + config)

def add_config(file, key, value):
    found = False
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            if line.strip().startswith(f'{key}'):
                print(f'Updating the value of {key} with {value}')
                f.write(f'{key} = {value}\n')
                found = True
            else:
                f.write(f'{line}')
                    
    if not found:
        with open(file, 'a') as f:
            f.write(f'{key} = {value}\n')

add_config(file, key, value)