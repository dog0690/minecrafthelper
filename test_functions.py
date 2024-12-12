import os
import mysql.connector
import time
import shutil
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='root',
)
mycursor = db.cursor()
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
def choice(choice, f1, f2, f3):
    if choice == 'a':
        f1
    elif choice == 'b':
        f2
    elif choice == 'c':
        f3

def multiples(option_c):
    for i in range(len(option_c)):
        print(f"{option_c[i]}")

def clear_terminal():
    os.system('cls')

def test_makew(name, s):
    worlds = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds")
    wor = (r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds" + r"\\" +name )
    os.chdir(worlds)
    os.mkdir(name)
    os.chdir(wor)
    with open(name, "w+") as file:
        file.write("first save")
    #Testing Portion
    time.sleep(s)
    os.chdir(worlds)
    shutil.rmtree(wor)
    print('test completed')
world_name = 'test1'
test_makew(world_name, 5)