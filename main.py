import sys
test = open(r"test.txt","r")
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
    sub_divider()
    name = input("What's the name?\n")
    test = open("test.txt", "a")
    test.write(name+"\n")
    test.close()
    sub_divider()
    A()

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
    option = ["A) New save", "B) Delete Save", "C) Return"]
    test = open(r"test.txt","r+")
    print("YOUR WORLDS")
    sub_divider()
    
    for i in range(line_count):
        print(i+1, test.readline().strip())
    
    
    
    sub_divider()
    for i in option:
        print(i)
    def choice(option):
        if option =="a":
            new_save()
        elif option =="b":
            delete_save()
        elif option =="c":
            close()
            
    divider()
    choice(input("what do you want to do?\n"))
    divider()
    

#Menu
def choice(option):
    
    divider()
    if option == "a":
        A()
    elif option == "b":
        close()
    else:
        print("retry")
        choice()

choice(input(""))