import os
import mysql.connector
import time
import shutil
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
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
    db_cursor.execute("CREATE TABLE tb (name VARCHAR(50), ID int PRIMARY KEY AUTO_INCREMENT)")

def view_world():
    print("view world")
def delete_world():
    print("delete world")


def main_choice(choice):
    if choice == 'a':
        make_world(input("what is the name of your world?\n"))
    elif choice == 'b':
        view_world()
    elif choice == 'c':
        delete_world()
    else:
        print("invalid response")
        choice()