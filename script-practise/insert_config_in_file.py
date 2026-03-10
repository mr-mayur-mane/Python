file = input("Enter the file name: ")

config = "node_env = prod"

with open(file, 'r')as f:
    content= f.read()
    if config not in content:
        print("No config found")
        print(f'Adding config: {config}')
        with open(file, 'a') as f:
            f.write(f'\n{config}')
            print("Config added.")
