file = "app.conf"

key = input("Enter the config key name: ")
value = input("Enter the config value name: ")
def app_config(file,key,value):
    found = False
    with open(file, 'r') as read:
        config = read.readlines()
        for line in config:
            with open(file, 'w') as write:
                if line.strip().startswith(key):
                    write.write(f'{key} = {value}')
                    found = True
                    print(f'Config found.\n Updating condif: {key} = {value}')
                else:
                    write.write(f'{line}')
                    

                if not found:
                    print(f'No config found.\n Adding config: {key} = {value}')
                    write.write(f'\n{key} = {value}')

app_config(file,key,value)
