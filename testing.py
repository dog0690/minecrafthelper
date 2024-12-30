import os
import stat

def get_permissions(path):
    st = os.stat(path)
    return oct(st.st_mode)[-3:]

print(get_permissions(r"C:\Users\charl\OneDrive\Desktop\coding\minecrafthelper\worlds"))