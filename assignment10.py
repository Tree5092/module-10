import os #imports os library

print("Hello there! I can save a new file with your name, address, and phone number, in a specified directory for you!" )

userpath = input("Give me the path to the directory that you want to save the file in: \n ")

if not os.path.isdir(userpath):
    print("Sorry but that specified directory path does not exist.")
    quit()
newfile = input("What do you want to name the file?\n")
filepath = os.path.join(userpath, newfile)
name = input("What's your name?\n")
address = input("What is your address?\n")
number = input("What is your phone number?\n")

try:
    with open(filepath, 'w') as file_object: #create the new file
        data = (name + ',' + address + ',' + number)
        file_object.write(data) #writing to file
except Exception:
    print('Error creating the new file')
    quit()
try:
    with open(filepath) as file_object:
        print('Today we created a new file, ' + newfile + 'and the following information was added to the file:')
        print(file_object.read())
except Exception:
    print('Error reading the file.')
    quit()
