import os

dir = input("Enter the dir: ")

file = [ f for f in os.listdir(dir) ]

print("Files in ", dir, " : ", file)