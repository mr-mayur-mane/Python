# file = "app.conf"
# config = "This is the new config"

# with open(file, 'r') as f:
#     content = f.read()
#     if config not in content:
#         with open(file, 'a') as f:
#             f.write("\n" + config)


# update the config value if present else add the config

def add_config(file,key,value):
    with open(file,'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            if line.strip().startswith(f"{key}"):
                f.write(f"{key} = {value}\n")
            else:
                f.write(line)
add_config("app.conf","max_connection","500")