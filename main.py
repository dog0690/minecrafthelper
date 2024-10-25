import sys
import os
test = open(r"test.txt","r")
folder_path = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
contents = os.listdir(folder_path)
def divider():
    print("==========================")
def sub_divider():
    print("--------------------------")
print(f"Hello, this is your minecraft helper\nHow can I help you?")
divider()
option = ["A) View Saves", "B) Exit"]
saved_world = []
#function
lines = test.readlines()
line_count = len(lines)
def close():
    sys.exit
def main():
    for i in option:
        print (i)     
    sub_divider()
main()
def world_list():
    for i in range(line_count):
        (i+1, test.readline())
#Option A Menu
def new_save():
    clear_terminal()
    sub_divider()
    name = input("What's the name?\n")
    test = open("test.txt", "a")
    os.chdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
    os.mkdir(name)
    os.chdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +name )
    with open(name, "w+") as file:
        folder(file, name)
    sub_divider()
#folder management system
def folder(file, name):
    file.write(name)
    lines = file.readlines()
    line_count = len(lines)
    for i in range(line_count):
        print(i+1, file.readline().strip())
def delete_save():
    world_pos = int(input("Which world do you want to delete?\n"))
    world_name = lines[world_pos -1]
    print(f"are you sure you want to delete {world_pos}, {world_name}?")
    def delete_world():
        world_type = input("Please type to confirm:")
        with open("test.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != world_type:
                    f.write(line)
        print("Deleted!")
        A()
    def choice(option):
        if option == "y":
            delete_world()
        elif option == "n":
            print("No")
        else:
            print("retry")
            choice()
    choice(input("(Y) Yes or N (No)\n"))
#Main Menu
def A():
    test = open(r"test.txt","r")
    option = ["A) New save", "B) Delete Save","C) Enter world", "D) Return"]
    print("YOUR WORLDS")
    sub_divider()
    for item in contents:
        print(item)
    sub_divider()
    for i in option:
        print(i)
    def choice(option):
        if option =="a":
            new_save()
        elif option =="b":
            delete_save()
        elif option == "c":
            C()
        elif option =="d":
            close()
            
    divider()
    choice(input("what do you want to do?\n"))
    divider()
def C():
    clear_terminal()
    divider()
    for item in contents:
        print(item)
    sub_divider()
    name = input("What world do you want to enter?\n")
    world = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds"+"\\"+name)
    os.chdir(world)
    with open(name, "a+") as file:
        content = file.read()
        print(content)
        choices = ["A) Add information", "B) Delete Information", "C) Return"]
        for i in choices:  
            print(i)
        c_choice(input("what do you want to do? \n"), name)
    pass
def c_choice(option, name):
    if option == "a":
        with open(name, "a") as file:
            information = input("what do you want to add?\n")
            file.write(information + "\n")
            file.close()
    else:
        pass
#Menu
def choice(option):
    
    divider()
    for item in contents:
        print(item)
    sub_divider()
    if option == "a":
        clear_terminal()
        A()
    elif option == "b":
        clear_terminal()
        close()
    elif option == "c":
        C()
    else:
        print("retry")
        clear_terminal()
        choice()
def clear_terminal():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")
choice(input(""))