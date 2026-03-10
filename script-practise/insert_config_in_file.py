file = input("Enter the file name: ")

key = input("Enter the config key: ")

value= input("Enter the config value: ")
def add_config(file, key, value):
    found = False
    with open(file, 'r') as reader:
        lines =reader.readlines()
        for line in lines:
            with open(file, 'w') as writer:
                if line.strip().startswith(f'{key}'):
                    writer.write(f'{key} = {value}')
                    found = True
                    print("Config key found, updating the value")
                else:
                    writer.write(f'{line}')
                if not found:
                    print("No config found, appending the config")
                    writer.write(f'\n{key} = {value}')

add_config(file, key, value)