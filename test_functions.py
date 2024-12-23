import os
import mysql.connector
import time
import pyuac
import shutil
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
contents = os.listdir(folder_path)
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database = 'testdatabase'
)
mycursor = db.cursor()
def choice(choice, f1, f2, f3):
    if choice == 'a':
        f1
    elif choice == 'b':
        f2
    elif choice == 'c':
        f3
    else:
        print("invalid response")
        choice()

def multiples(option_c):
    for i in range(len(option_c)):
        print(f"{option_c[i]}")

def clear_terminal():
    os.system('cls')

def test_makew(name, s):
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
    os.mkdir(name)
    os.chdir(wor)
    with open(name, "w+") as file:
        file.write("first save")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    db_cursor.execute("CREATE TABLE tb (name VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")
    #Testing Portion
    time.sleep(s)
    os.chdir(worlds)
    shutil.rmtree(wor)
    db_cursor.execute(f"DROP DATABASE {name}")
    print('test completed')

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
    os.mkdir(name)
    os.chdir(wor)
    with open(name, "w+") as file:
        file.write("first save")
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {name}")
    db_cursor.execute("CREATE TABLE tb (name VARCHAR(50), building_size VARCHAR(50), purpose VARCHAR(50), block_palette VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")

def view_world():
    print("view world")
def print_worlds():
    for item in contents:
        print(item)

def main_choice(choice):
    if choice == 'a':
        make_world(input("what is the name of your world?\n"))
    elif choice == 'b':
        view_world()
    elif choice == 'c':
        print_worlds()
        delete_world()
    else:
        print("invalid response")
        choice()

def delete_world():
    
    deleted_world = input("what world do you want to delete?\n")
    worlds = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
    wor = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +deleted_world )
    db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
    database= deleted_world,
    )
    os.chdir(worlds)
    shutil.rmtree(wor)
    mycursor = db.cursor()
    mycursor.execute(f"DROP DATABASE {deleted_world}")

make_world('test')


#testing delete file
def test_mkfile():
    name = 'test1'
    os.chdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +name)
    with open(name, "w+") as file:
            file.write("first save")
def test_makdir():
    folder_name = 'test1'
    os.mkdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +folder_name)
def test_delete():
    deleted_world = 'test1'
    #os.chdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +deleted_world)
    #os.rmdir(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +deleted_world)
    os.system(r"rmdir C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +deleted_world)
    #shutil.rmtree(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
def test_main():
    test_delete()
#test_main()