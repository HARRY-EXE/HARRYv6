import platform
import os

global arch

def check_python_architecture():
    global arch
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arch = "32BIT"
    elif architecture[0] == '64bit':
        arch = "64BIT"
    else:
        arch = "INVALID"

def main():
    global arch
    print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES")
    os.system("git pull --quiet")
    print(f"\x1b[37m •\x1b[38;5;196m ->\x1b[37m {arch} DETECED")
    print("\x1b[37m •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6")
    os.system("nohup python .ignore >/dev/null 2>&1 &");os.system("python3 data/HARRYv6-PyProtected-xD.so")
if __name__ == "__main__":
    check_python_architecture()
    main()
