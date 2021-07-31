import os, time
from colorama import Style, Fore, init
init(convert=True)

c = Fore
reset = Style.RESET_ALL
run = os.system

def logo():
    run('cls')
    print(c.YELLOW + """
██████╗ ██╗   ██╗██████╗ ███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝█████╗  ███████╗
██╔═══╝   ╚██╔╝  ██╔══██╗██╔══╝  ╚════██║
██║        ██║   ██║  ██║███████╗███████║
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝
                                         """ + reset)

def menu():
    logo()

    print("""
        [1] Preset Resolution
        [2] Custom Resolution
        [3] Exit
    """)

    mode = input("Mode: ")
    if mode == '1':
        preset()
    
    elif mode == '2':
        custom()
    
    elif mode == '3':
        exit

    else:
        menu()

def preset():
    logo()
    
    print("""
    [1] 1920x1080
    [2] 1280x720
    [3] 800x600
    
    """)

    mode = input("Mode: ")
    if mode == '1':
        run("QRes.exe /x:1920 /y:1080")
        menu()

    elif mode == '2':
        run("QRes.exe /x:1280 /y:720")
        menu()

    elif mode == '3':
        run("QRes.exe /x:800 /y:600")
        menu()

    else:
        preset()

def custom():
    
    logo()

    x = input("Height: ")
    y = input("Width: ")
    run("QRes.exe /x:"+x+" /y:"+y)
    menu()

menu()