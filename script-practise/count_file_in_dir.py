import os

dir = input("Enter the dir: ")

if os.path.isdir(dir):

    file = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) and f.endswith(".log")]

print("Files in ", dir, " : ", file)