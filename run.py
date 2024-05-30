import platform
import os
from os import system as import_
login = "python"

global arch , file

def check_python_architecture():
    global arch , file
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        file = "HARRY32.cpython-311.so"
        arch = "32BIT"
    elif architecture[0] == '64bit':
        file = "HARRY64.cpython-311.so"
        arch = "64BIT"
    else:
        arch = "INVALID"

def main():
    global arch , file
    print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES")
    os.system("git pull --quiet")
    if arch == "32BIT":
        print(f"\x1b[37m •\x1b[38;5;196m ->\x1b[37m {arch} DETECED")
        print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6")
        import_(f'{login} data/{file}')
    elif arch == "64BIT":
        print(f"\x1b[37m •\x1b[38;5;196m ->\x1b[37m {arch} DETECED")
        print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6")
        import_(f'{login} data/{file}')
if __name__ == "__main__":
    check_python_architecture()
    main()
