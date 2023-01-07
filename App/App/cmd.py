import time
import math
import os
import sys

key = "D:\\App\\App"
os.chdir(key)
keys = open(key)
key_key_sys = keys.read()
boot_code = "JARVIS-Start-system = yes"
boot_code_no = "JARVIS-Start-system = no"
status = "?"
Algorytm = status
command = input("New cmd command: ")

if key_key_sys == boot_code:
    status = "Ok"
    Algorytm = status

    while status == Algorytm:
        if command == "echo" + echo= input(""):
            print(echo)
        if command == "neofetch":
            os.chdir(key)
            os.startfile("neo.png")
if key_key_sys == boot_code_no:
    print("Sorry I can't start system. File is not compatibile!!!")


