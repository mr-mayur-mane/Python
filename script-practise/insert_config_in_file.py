file = input("Enter the file name: ")

key = input("Enter the config key: ")

value= input("Enter the config value: ")
def add_config(file, key, value):
    found = False
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            with open(file, 'w') as f:
                if line.strip().startswith(f'{key}'):
                    f.write(f'{key} = {value}')
                    found = True
                    print("Config key found, updating the value")
                else:
                    f.write(f'{line}')
        if not found:
            print("No config found, appending the config")
            with open(file, 'a') as f:
                f.write(f'\n{key} = {value}')

add_config(file, key, value)