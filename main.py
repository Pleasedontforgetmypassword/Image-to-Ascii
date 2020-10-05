from sys import argv
from Ascii import valid, write, conversion

def check(args):
    if len(args) != 3:
        return False

    elif args[1] not in ["10", "70"]:
        return False

    return valid(args[2])

def main():
    if check(argv) == False:
        print("Usage: python main.py (70 or 10) (Image name)")
        return 1
    else:
        print("Writing...")
        write(int(argv[1]), conversion(argv[2]), "Image.txt")
        print("Done")
        return 0

if __name__ == '__main__':
    main()
