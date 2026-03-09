file = "app.conf"
config = "node_env = prod"

with open(file, 'r') as file:
    content = file.read()
    if config not in content:
        print(f'No config found: {config}')
        print(f'Adding the config...')
        
