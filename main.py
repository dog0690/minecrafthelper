from test_functions import *
folder_path = (r'C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds')
contents = os.listdir(folder_path)
main_prompt = ('[A] MAKE WORLDS', '[B] ENTER WORLDS', '[C] DELETE WORLDS')
def main():
    clear_terminal()
    for item in contents:
        print(item)
    print("what can I help you with today?\n")
    multiples(main_prompt)
    main_choice(input(""))

main()