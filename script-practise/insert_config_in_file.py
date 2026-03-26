file = "app.conf"

key = input("Enter the config key: ")
value= input("Enter hte config value: ")
def app_conf(file,key,value):
    found = False
    with open(file, 'r') as reader:
        config = reader.readlines()
        with open(file, 'w') as writer:
            for line in config:
                if line.startswith(key):
                    print(f'Config found, updaing the value: \n{key} = {value}')
                    writer.write(f'{key} = {value}\n')
                    found = True
                else:
                    writer.write(line)

            if not found:
                print("Config not found, adding the config")
                writer.write(f'\n{key}={value}')

        
app_conf(file,key,value)