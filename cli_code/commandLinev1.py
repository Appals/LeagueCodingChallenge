import os

path = input("Please enter the path: ")
os.chdir(path)

user_input = input("Please enter file name")

if os.path.exists(user_input):
    f = open(user_input, 'r')
    c = f.read()
    print(c)
    f.close
else:
    print("file not exist")
    
        