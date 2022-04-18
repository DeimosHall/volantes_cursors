import os

path = "/usr/share/icons/volantes_cursors"
name = "volantes_cursors"

def install():
    print(f"Creating {name} directory...")
    os.system("sudo mkdir /usr/share/icons/volantes_cursors")
    print("Copying files...")
    os.system("sudo cp -r cursors/ index.theme /usr/share/icons/volantes_cursors")
    print("Theme succesfully installed")

def not_install():
    exit = False

    print("Icon theme is already installed")

    while(not exit):
        x = input("Do you want to install it again? y / n: ")

        if (x == "y"):
            # Deletes the directory
            os.system("sudo rm -r /usr/share/icons/volantes_cursors")
            install()
            exit = True
        elif (x == "n"):
            exit = True

if (os.path.exists(path)):
    not_install()
else:
    install()