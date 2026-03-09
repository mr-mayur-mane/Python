file = "app.conf"
config = "node_env = prod"

with open(file, 'r') as f:
    content = f.read()
    if config not in content:
        print(f'No config found: {config}')
        print(f'Adding the config...')
        with open(file, 'a') as f:
            f.write("\n" + config)

