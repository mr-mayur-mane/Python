file = "app.conf"
config = "This is the new config"

with open(file, 'r') as f:
    content = f.read()
    if config not in content:
        with open(file, 'a') as f:
            f.write("\n" + config)
            
