file = "app.conf"

config_key = input("Enter the config key: ")
config_value = input("Enter the config value: ")

def update_config(file,config_key,config_value):
    found = False
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            with open(file, 'w') as w:
                if line.startswith(config_key):
                    print("Config found, updating")
                    w.write(f'{config_key} = {config_value}\n')
                    found = True
                else:
                    w.write(line)

                if not found:
                    print("No config found, Adding config")
                    w.write(f'\n{config_key} = {config_value}')

update_config(file,config_key,config_value)