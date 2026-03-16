file = "app.conf"

key = input("Enter the config key name: ")
value = input("Enter the config value: ")

def app_config(file, key, value):
    found = False
    with open(file, 'r') as reader:
        config = reader.readlines()
        with open(file, 'w') as writer:
            for line in config:
                if line.strip().startswith(f'{key}'):
                    print("Config key found, updating")
                    writer.write(f'{key} = {value}\n')
                    found = True
                    print(f'Config updated: {key} = {value}')
                else:
                    writer.write(line)
            if not found:
                writer.write(f'{key} = {value}')
                print("Config appending")

app_config(file,key,value)