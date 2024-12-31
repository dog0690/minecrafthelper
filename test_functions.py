import os
import mysql.connector
import time
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
contents = os.listdir(folder_path)
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database = 'testdatabase'
)
mycursor = db.cursor()

#COSMETICS
def multiples(option):
    for i in range(len(option)):
        print(f"{option[i]}")
def clear_terminal():
    os.system('cls')    

#OPTIONS
def make_world(name):
    worlds = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
    wor = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +name )
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    db_world = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='root',
        database = name
    )
    db_cursor = db_world.cursor()
    os.chdir(worlds)
    with open(name, "w+") as file:
        file.write("first save")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    db_cursor.execute("CREATE TABLE Building Generation (name VARCHAR(50), building_size VARCHAR(50), purpose VARCHAR(50), block_palette VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")
    db_cursor.execute("CREATE TABLE Terrain Generation (name VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")
    db_cursor.execute("CREATE TABLE tb Cosmetic Generation (name VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")
def view_world(name):
    db_world = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='root',
        database = name
    )
    print(f"You have entered {name} what do you wnat to do now?\n")
    return(db_world)
def print_worlds():
    for item in contents:
        print(item)
def delete_world(name):
    worlds = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
    wor = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +name )
    db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database= name,
    )
    os.chdir(worlds)
    os.remove(wor)
    mycursor = db.cursor()
    mycursor.execute(f"DROP DATABASE {name}")
#CHOICES 
def main_choice(choice):
    if choice == 'a':
        make_world(input("what is the name of your world?\n"))
    elif choice == 'b':
        view_choice(input("what world do you want to view?\n"))
    elif choice == 'c':
        print_worlds()
        delete_world(input("what world do you want to delete?\n"))
    else:
        print("invalid response")
        choice()
main_prompt = ('[A] MAKE WORLDS', '[B] ENTER WORLDS', '[C] DELETE WORLDS')
view_prompt = ('[A] T-GEN', '[B] B-GEN', '[C] C-GEN', '[D] RETURN')
def view_choice(name):
    db_world = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='root',
        database = name
    )
    cursor = db_world.cursor()
    cursor.execute('SHOW TABLES')
    multiples(view_prompt)
    choice = input("what do you want to do?")
    if choice == 'a':
        pass
    elif choice == 'b':
        pass
    elif choice == 'c':
        multiples(main_prompt)
        main_choice(input(""))
    else:
        print("invalid response")
        choice()
view_choice("testing_world1")