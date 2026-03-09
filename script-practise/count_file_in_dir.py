import os

dir = input("Enter the valid dir path: ")

if os.path.isdir(dir):
    file = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]
    print("Files ending with .log", file)
else:
    print("Invalid dir", dir)
