from test_functions import *
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
contents = os.listdir(folder_path)
prompt1 = ('[A] Make World', '[B] Enter Worlds', '[C] Delete World')
def main():
    clear_terminal()
    for item in contents:
        print(item)
    print("what can I help you with today?")
    multiples(prompt1)
    answer1 = input("\n")
    choice(answer1, make_world(), enter_world(), delete_world())
def make_world():
    pass
def enter_world():
    pass
def delete_world():
    pass
main()