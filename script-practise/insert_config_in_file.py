file = "app.conf"

key = input("Enter the config key name: ")
value = input("Enter the config value: ")

def app_config(file,key,value):
    found=False
    with open(file,'r') as reader:
        lines=reader.readlines()
        with open(file, 'w') as writer:
            for line in lines:
                if line.strip().startswith(f'{key}'):
                    writer.write(f'{key} = {value}\n')
                    found=True
                else:
                    writer.write(line)
        if not found:
            writer.write(f'{key} = {value}\n')

app_config(file,key,value)


        