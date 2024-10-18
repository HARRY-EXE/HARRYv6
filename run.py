import platform
import os
import socket
import subprocess

arc = None

print(f' •\x1b[38;5;196m ->\x1b[37m CHECKING FOR UPDATES ')
os.system('git pull --quiet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        exit(f' •\x1b[38;5;196m ->\x1b[37m 32BIT NOT SUPPORTED')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f' •\x1b[38;5;196m ->\x1b[37m 64BIT DETECTED')
        print(f' •\x1b[38;5;196m ->\x1b[37m STARTING HARRYv6 ')
        import data.HARRY64
    else:
        arc = "INVALID"
        exit("•\x1b[38;5;196m ->\x1b[37m UNKNOWN DEVICE TYPE")


if __name__ == "__main__":
    main()
